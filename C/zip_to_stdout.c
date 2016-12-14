#include <stdio.h>
#include <unistd.h>

#include <zip.h>

// zip_source_callback
zip_int64_t callback(void *userdata, void *data, zip_uint64_t len, zip_source_cmd_t cmd)
{
	fprintf(stderr, "callback: cmd=");
	switch (cmd) {
		case ZIP_SOURCE_BEGIN_WRITE: fprintf(stderr, "ZIP_SOURCE_BEGIN_WRITE"); break;
		case ZIP_SOURCE_CLOSE: fprintf(stderr, "ZIP_SOURCE_CLOSE"); break;
		case ZIP_SOURCE_COMMIT_WRITE: fprintf(stderr, "ZIP_SOURCE_COMMIT_WRITE"); break;
		case ZIP_SOURCE_ERROR: fprintf(stderr, "ZIP_SOURCE_ERROR"); break;
		case ZIP_SOURCE_FREE: fprintf(stderr, "ZIP_SOURCE_FREE"); break;
		case ZIP_SOURCE_OPEN:
			fprintf(stderr, "ZIP_SOURCE_OPEN");
			break;
		case ZIP_SOURCE_READ: fprintf(stderr, "ZIP_SOURCE_READ"); break;
		case ZIP_SOURCE_REMOVE: fprintf(stderr, "ZIP_SOURCE_REMOVE"); break;
		case ZIP_SOURCE_ROLLBACK_WRITE: fprintf(stderr, "ZIP_SOURCE_ROLLBACK_WRITE"); break;
		case ZIP_SOURCE_SEEK: fprintf(stderr, "ZIP_SOURCE_SEEK"); break;
		case ZIP_SOURCE_SEEK_WRITE: fprintf(stderr, "ZIP_SOURCE_SEEK_WRITE"); break;
		case ZIP_SOURCE_STAT:
			fprintf(stderr, "ZIP_SOURCE_STAT\n");
			zip_stat_t *sb = data;
			zip_stat_init(sb);
			sb->size = 0;
			sb->valid |= ZIP_STAT_SIZE;
			return sizeof(struct zip_stat);

			break;
		case ZIP_SOURCE_SUPPORTS:
			fprintf(stderr, "ZIP_SOURCE_SUPPORTS\n");
			return zip_source_make_command_bitmap(ZIP_SOURCE_BEGIN_WRITE, ZIP_SOURCE_CLOSE, ZIP_SOURCE_COMMIT_WRITE, ZIP_SOURCE_ERROR, ZIP_SOURCE_FREE, ZIP_SOURCE_OPEN, ZIP_SOURCE_READ, ZIP_SOURCE_REMOVE, ZIP_SOURCE_ROLLBACK_WRITE, ZIP_SOURCE_SEEK, ZIP_SOURCE_SEEK_WRITE, ZIP_SOURCE_STAT, ZIP_SOURCE_SUPPORTS, ZIP_SOURCE_TELL, ZIP_SOURCE_TELL_WRITE, ZIP_SOURCE_WRITE, -1);
			 break;
		case ZIP_SOURCE_TELL: fprintf(stderr, "ZIP_SOURCE_TELL"); break;
		case ZIP_SOURCE_TELL_WRITE: fprintf(stderr, "ZIP_SOURCE_TELL_WRITE"); break;
		case ZIP_SOURCE_WRITE:
			fprintf(stderr, "ZIP_SOURCE_WRITE\n");
			write(1, data, len); // dump to stdout
			break;
		default: fprintf(stderr, "%x"); break;
	}
	fprintf(stderr, ", data=");
	int i;
	for (i=0; i<len; i++) fprintf(stderr, "%02x", ((char*)data)[i]);
	fprintf(stderr, "\n");

}

void test1()
{
	void *userdata;
	zip_error_t *error;
	zip_source_t *zsrc = zip_source_function_create(callback, userdata, error);
}

void show(zip_t *archive)
{
	int files_total = zip_get_num_files(archive);
	int i;
	for (i = 0; i<files_total; i++) {
		const char *filename =  zip_get_name(archive, i, 0);
		fprintf(stderr, "file index %d: %s\n", i, filename);
	}
}

void test2()
{
	unsigned char data[1000];
	FILE *x = fopen("x.zip", "r");
	size_t n = fread(data, 1, 1000, x);
	fprintf(stderr, "fread: n=%d\n", n);
	zip_error_t *error;
	zip_source_t *zsrc = zip_source_buffer_create(data, n, 0, error);
}

int main()
{
	void *userdata = "toto";
	zip_error_t *error;
	zip_source_t *zsrc = zip_source_function_create(callback, userdata, error);

	fprintf(stderr, "zip_open_from_source...\n");
	zip_t *archive = zip_open_from_source(zsrc, 0, error);

	show(archive);

	const char *name = "y.txt";
	zip_flags_t flags = 0;
	fprintf(stderr, "zip_file_add...\n");
	zip_int64_t i = zip_file_add(archive, name, zsrc, flags);
	fprintf(stderr, "zip_file_add(): i=%lld\n", i);
	//
	show(archive);
	int ret = zip_close(archive);
}
