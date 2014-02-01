#include <stdlib.h>

#include <sys/types.h>
#include <regex.h>
#include <stdio.h>

void usage()
{
    printf("Usage: regex <expr> <text>\n");
    exit(1);
}
int main(int argc, char *argv[])
{
    if (argc < 3) usage();

    regex_t regex;
    int reti;
    char msgbuf[100];

    /* Compile regular expression */
    reti = regcomp(&regex, argv[1], 0);
    if (reti) {
        fprintf(stderr, "Could not compile regex\n");
        exit(1);
    }

    /* Execute regular expression */
    reti = regexec(&regex, argv[2], 0, NULL, 0);
    if (!reti) {
        puts("Match");
    } else if (reti == REG_NOMATCH) {
        puts("No match");
    } else {
        regerror(reti, &regex, msgbuf, sizeof(msgbuf));
        fprintf(stderr, "Regex match failed: %s\n", msgbuf);
        exit(1);
    }

    /* Free compiled regular expression if you want to use the regex_t again */
    regfree(&regex);

    return 0;
}
