
/*
 * Example using libzip (compile with -lzip)
 */
#include <stdio.h>
#include <unistd.h>

#include <zip.h>

void show(zip_t *archive, const char *text)
{
	fprintf(stderr, "--- %s ---\n", text);
	int files_total = zip_get_num_files(archive);
	int i;
	for (i = 0; i<files_total; i++) {
		const char *filename =  zip_get_name(archive, i, 0);
		fprintf(stderr, "file index %d: %s\n", i, filename);
	}
}

zip_source_t *loadFromFile()
{
	zip_error_t error;
	static unsigned char data[1000];
	FILE *x = fopen("x.zip", "r");
	size_t n = fread(data, 1, 1000, x);
	fprintf(stderr, "fread: n=%d\n", n);
	zip_source_t *zsrc = zip_source_buffer_create(data, n, 0, &error);
	return zsrc;
}

int main()
{
	zip_source_t *zsrc = loadFromFile();
	if (!zsrc) return 1;

	fprintf(stderr, "zip_open_from_source...\n");
	zip_error_t error;
	zip_error_init(&error);
	zip_t *archive = zip_open_from_source(zsrc, 0, &error);
	if (!archive) return 2;
	zip_error_fini(&error);

	show(archive, "after zip_open_from_source");

	const char *name = "y.txt";
	zip_flags_t flags = 0;
	zip_source_t *otherZsrc = zip_source_buffer_create("hello", 5, 0, &error);

	fprintf(stderr, "zip_file_add...\n");
	zip_int64_t i = zip_file_add(archive, name, otherZsrc, flags);
	fprintf(stderr, "zip_file_add(): i=%lld\n", i);
	//
	show(archive, "after zip_file_add");
	zip_source_keep(zsrc);
	int ret;
	ret = zip_close(archive);

	// print to stdout

	zip_stat_t zst;
	ret = zip_source_stat(zsrc, &zst);
	fprintf(stderr, "zip_source_stat: ret=%d, zst.size=%d\n", ret, zst.size);

	ret = zip_source_open(zsrc);
	fprintf(stderr, "zip_source_open: ret=%d\n", ret);
	unsigned char data[10000];
	zip_uint64_t n = zip_source_read(zsrc, data, sizeof(data));
	fprintf(stderr, "zip_source_read: n=%d\n", n);
	write(1, data, n); // print to stdout

	
}
