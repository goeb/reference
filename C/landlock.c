/*
 * Restrict read & write permissions to files under /tmp
 *
 * Usage:
 *     gcc landlock.c -o landlock
 *
 *     ./landlock touch ~/x
 *     touch: cannot touch '/home/.../x': Permission denied
 *
 *     ./landlock touch /tmp/x
 * 
 * Compatible with Linux kernel 6.5.0
 */

#define _GNU_SOURCE
#include <errno.h>
#include <fcntl.h>
#include <linux/landlock.h>
#include <linux/prctl.h>
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/prctl.h>
#include <sys/stat.h>
#include <sys/syscall.h>
#include <unistd.h>

int main(const int argc, char *const argv[], char *const *const envp)
{
	const char *command;
	char *const *command_argv;
	int ruleset_fd;
	int err;
	struct landlock_ruleset_attr ruleset_attr = {
		.handled_access_fs = \
        		LANDLOCK_ACCESS_FS_EXECUTE | \
        		LANDLOCK_ACCESS_FS_READ_FILE | \
        		LANDLOCK_ACCESS_FS_READ_DIR | \
        		LANDLOCK_ACCESS_FS_WRITE_FILE | \
        		LANDLOCK_ACCESS_FS_REMOVE_DIR | \
        		LANDLOCK_ACCESS_FS_REMOVE_FILE | \
        		LANDLOCK_ACCESS_FS_MAKE_CHAR | \
        		LANDLOCK_ACCESS_FS_MAKE_DIR | \
        		LANDLOCK_ACCESS_FS_MAKE_REG | \
        		LANDLOCK_ACCESS_FS_MAKE_SOCK | \
        		LANDLOCK_ACCESS_FS_MAKE_FIFO | \
        		LANDLOCK_ACCESS_FS_MAKE_BLOCK | \
        		LANDLOCK_ACCESS_FS_MAKE_SYM,
	};

	ruleset_fd = syscall(__NR_landlock_create_ruleset, &ruleset_attr, sizeof(ruleset_attr), 0);
	if (ruleset_fd < 0) {
		perror("Failed to create a Landlock ruleset");
		return 1;
	}

	struct landlock_path_beneath_attr path_beneath = {
    		.allowed_access =
                        LANDLOCK_ACCESS_FS_EXECUTE | \
                        LANDLOCK_ACCESS_FS_READ_FILE | \
                        LANDLOCK_ACCESS_FS_READ_DIR | \
                        LANDLOCK_ACCESS_FS_WRITE_FILE | \
                        LANDLOCK_ACCESS_FS_REMOVE_DIR | \
                        LANDLOCK_ACCESS_FS_REMOVE_FILE | \
                        LANDLOCK_ACCESS_FS_MAKE_CHAR | \
                        LANDLOCK_ACCESS_FS_MAKE_DIR | \
                        LANDLOCK_ACCESS_FS_MAKE_REG | \
                        LANDLOCK_ACCESS_FS_MAKE_SOCK | \
                        LANDLOCK_ACCESS_FS_MAKE_FIFO | \
                        LANDLOCK_ACCESS_FS_MAKE_BLOCK | \
                        LANDLOCK_ACCESS_FS_MAKE_SYM,
		.parent_fd = -1,
	};

	const char *path[] = { "/usr", "/tmp", NULL };
	const char **ptr = path;

	while (*ptr) {

		path_beneath.parent_fd = open(*ptr, O_PATH | O_CLOEXEC);
		if (path_beneath.parent_fd < 0) {
    			perror("Failed to open file");
    			goto error;
		}

		err = syscall(__NR_landlock_add_rule, ruleset_fd, LANDLOCK_RULE_PATH_BENEATH, &path_beneath, 0);
		close(path_beneath.parent_fd);
		if (err) {
	    		perror("Failed to update ruleset");
	    		goto error;
		}
		ptr++;
	}

	if (prctl(PR_SET_NO_NEW_PRIVS, 1, 0, 0, 0)) {
		perror("Failed to restrict privileges");
		goto error;
	}

	err = syscall(__NR_landlock_restrict_self, ruleset_fd, 0);
	if (err) {
		perror("Failed to enforce Landlock ruleset");
		goto error;
	}
	close(ruleset_fd);

	command = argv[1];
	command_argv = argv + 1;
	execvpe(command, command_argv, envp);
	fprintf(stderr, "execvpe error on '%s': %s\n", command, strerror(errno));
	return 1;

error:
	close(ruleset_fd);
	return 1;
}
