#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

void usage()
{
    printf("Usage: rambenchmark <sizeKb> <wordSize> <nIterations>\n");
    printf("    The program writes to and reads from a buffer malloced with the given size.\n");
    printf("    <wordSize> must be 1, 2 or 4. It indicates how many bytes at a time the memory is accessed.\n");
    exit(1);
}

int main(int argc, char **argv)
{
    if (argc != 4 || 0==strcmp(argv[1], "-h")) usage();

	if (sizeof(unsigned short) != 2) {
		printf("Error: sizeof(unsigned short) != 2\n");
		exit(1);
	} else if (sizeof(unsigned int) != 4) {
		printf("Error: sizeof(unsigned int) != 4\n");
		exit(1);
	}

    int size = atoi(argv[1]) * 1024;
    int wordSize = atoi(argv[2]);
	if ((wordSize != 1) && (wordSize != 2) && (wordSize != 4)) {
		printf("Error: wordSize must be 1, 2 or 4 (given: %d)\n", wordSize);
		usage();
	}
    int nIterations = atoi(argv[3]);

    printf("Allocating %d bytes...\n", size);
    unsigned char *buffer = (unsigned char*)malloc(size);

	int iteration;
	for (iteration=0; iteration<nIterations; iteration++) {
		int j;
		unsigned long long crcWrite = 0;
		// write forward
		int nCells = size/wordSize;
		for (j=0; j<nCells; j++)
		{
			if (wordSize == 1) {
				buffer[j] = j;
			} else if (wordSize == 2) {
				unsigned short* x = (unsigned short*)(buffer+2*j);
				*x = j;
			} else { // word size 4
				unsigned int* x = (unsigned int*)(buffer+4*j);
				*x = j;
			}
			crcWrite += (unsigned long long) j % (1ULL << (wordSize*8));
			//printf("j=%d, crcWrite=%llu\n", j, crcWrite);
		}
		// read forward
		unsigned long long crcRead = 0;
		for (j=0; j<nCells; j++)
		{
			if (wordSize == 1) crcRead += buffer[j];
			else if (wordSize == 2) {
				unsigned short* x = (unsigned short*)(buffer+2*j);
				crcRead += *(unsigned short*)(buffer+2*j);
			}
			else crcRead += *(unsigned int*)(buffer+4*j);
		}
		if (crcRead != crcWrite) printf("Error (forward): crcRead=%llu, crcWrite=%llu\n", crcRead, crcWrite);
		//else printf("crc=%llu\n", crcRead);

		// access memory backward
		crcWrite = 0;
		// write backward
		for (j=nCells-1; j>=0; j--)
		{
			if (wordSize == 1) buffer[j] = j;
			else if (wordSize == 2) *(unsigned short*)(buffer+2*j) = j;
			else *(unsigned int*)(buffer+4*j) = j; // word size 4

			crcWrite += j % (1ULL << (wordSize*8));
		}
		// read backward
		crcRead = 0;
		for (j=nCells-1; j>=0; j--)
		{
			if (wordSize == 1) crcRead += buffer[j];
			else if (wordSize == 2) crcRead += *(unsigned short*)(buffer+2*j);
			else crcRead += *(unsigned int*)(buffer+4*j);
		}
		if (crcRead != crcWrite) printf("Error (backward): crcRead=%llu, crcWrite=%llu\n", crcRead, crcWrite);
	}
    printf("Done.");
}
