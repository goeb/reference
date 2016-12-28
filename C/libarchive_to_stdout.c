
/* Example using libarchive
 * gcc libarchive_to_stdout.c -larchive -g
 */
#include <archive.h>
#include <archive_entry.h>

#include <stdio.h>

int test1()
{
	struct archive *a = archive_write_new();
	int ret = archive_write_set_format_zip(a);

	unsigned char buffer[100];
	int size;
	ret = archive_write_open_memory(a, buffer, 100, &size);

	// add a file
	struct archive_entry  *entry = archive_entry_new();

	archive_entry_set_pathname(entry, "hello.txt");
	archive_entry_set_size(entry, 5);
	archive_entry_set_filetype(entry, AE_IFREG);
	archive_entry_set_perm(entry, 0644);
	ret = archive_write_header(a, entry);
	printf("archive_write_header: ret=%d\n", ret);
	la_ssize_t n = archive_write_data(a, "world", 5);
	printf("archive_write_data: n=%d, error=%s\n", n, archive_error_string(a));


	// ad another file
	//
	archive_entry_clear(entry);
	archive_entry_set_pathname(entry, "somedir/yo.txt");
	archive_entry_set_size(entry, 5);
	archive_entry_set_filetype(entry, AE_IFREG);
	archive_entry_set_perm(entry, 0644);
	archive_write_header(a, entry);
	n = archive_write_data(a, "12345", 5);
	printf("archive_write_data: n=%d, error=%s\n", n, archive_error_string(a));

	archive_entry_free(entry);

	ret = archive_write_free(a);
	printf("archive_write_free: ret=%d, error=%s\n", ret, archive_error_string(a));

	printf("size=%d\n", size);
	write(1, buffer, size);
}

int myopen(struct archive *a, void *client_data)
{
	return ARCHIVE_OK;
}

la_ssize_t mywrite(struct archive *a, void *client_data, const void *buffer, size_t length)
{
	return write(1, buffer, length); // write to stdout
}

int myclose(struct archive *a, void *client_data)
{
	return ARCHIVE_OK;
}

int test2_with_write_callbacks()
{
	struct archive *a = archive_write_new();
	archive_write_set_format_zip(a);
	int ret = archive_write_open(a, NULL, myopen, mywrite, myclose);

	// add a file
	struct archive_entry  *entry = archive_entry_new();
	archive_entry_set_pathname(entry, "123.d/hello.txt");
	archive_entry_set_size(entry, 5);
	archive_entry_set_filetype(entry, AE_IFREG);
	archive_entry_set_perm(entry, 0644);
	ret = archive_write_header(a, entry);
	fprintf(stderr, "archive_write_header: ret=%d\n", ret);
	la_ssize_t n = archive_write_data(a, "world", 5);
	fprintf(stderr, "archive_write_data: n=%d, error=%s\n", n, archive_error_string(a));

	archive_entry_free(entry);

	ret = archive_write_free(a);
	fprintf(stderr, "archive_write_free: ret=%d, error=%s\n", ret, archive_error_string(a));
}

int main()
{
	test2_with_write_callbacks();
}
