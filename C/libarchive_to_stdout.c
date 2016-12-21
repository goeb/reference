
/* Example using libarchive
 * gcc libarchive_to_stdout.c -larchive -g
 */
#include <archive.h>
#include <archive_entry.h>

#include <stdio.h>

int main()
{
	struct archive *a = archive_write_new();
	int ret = archive_write_set_format_zip(a);

	unsigned char buffer[1000];
	int size;
	ret = archive_write_open_memory(a, buffer, 1000, &size);

	// add a file
	struct archive_entry  *entry = archive_entry_new();

	archive_entry_set_pathname(entry, "hello.txt");
	archive_entry_set_size(entry, 5);
	archive_entry_set_filetype(entry, AE_IFREG);
	archive_entry_set_perm(entry, 0644);
	archive_write_header(a, entry);
	archive_write_data(a, "world", 5);


	// ad another file
	//
	archive_entry_clear(entry);
	archive_entry_set_pathname(entry, "somedir/yo.txt");
	archive_entry_set_size(entry, 5);
	archive_entry_set_filetype(entry, AE_IFREG);
	archive_entry_set_perm(entry, 0644);
	archive_write_header(a, entry);
	archive_write_data(a, "12345", 5);

	archive_entry_free(entry);

	archive_write_close(a);
	archive_write_free(a); 

	printf("size=%d\n", size);
	write(1, buffer, size);
}
