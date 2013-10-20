/* 
gcc -g BitCut.c -o BitCut
*/
#include <stdlib.h>
typedef struct {
	unsigned char *Bits;
	int Length;
} DataType_t;
typedef int Natural;
typedef int xptrint;
#define xPrintString printf
#define COMMENT(x)
#define BitCut_sb BitCut
#define xAlloc_SDL_Bit_String malloc

void show(DataType_t data, char *label)
{
	int i;
	if (!label) label = "Datatype_t";
	printf("%s :\n\tBits = '", label);
	for (i=0; i<data.Length; i++) printf("%02x", data.Bits[i]);
	printf("'H\n\tLength = %d\n", data.Length);
}

DataType_t BitCut(DataType_t Input, Natural first_bit, Natural bit_length, int msb)
{
        DataType_t Output;
        int byte_length, first_byte;
        int shift, mask, remaining_bits;
        unsigned char *input_ptr, *output_ptr;

	/* printf("BitCut(data(%d), %d, %d)\n", Input.Length, first_bit, bit_length); */
        byte_length = (bit_length+7)/8;
        shift = first_bit%8;
        first_byte = first_bit/8;
        if (first_byte >= Input.Length) {
                xPrintString("BitCut error : first bit out of range\n");
                return(Output);
        }
	if (Input.Length*8 < first_bit+bit_length) {
                xPrintString("BitCut error : bits out of range\n");
                return(Output);
        }

	Output.Bits = (unsigned char *)malloc(byte_length);
	Output.Length = byte_length;
        input_ptr = Input.Bits + first_byte;
        output_ptr = Output.Bits;
        remaining_bits = bit_length;

        COMMENT (( operating on whole octets of Output buffer ))
        while (remaining_bits>=8) {
                COMMENT (( this is MSB computing only ))
                *output_ptr = 0;
		if (msb) *output_ptr = *input_ptr << shift;
		else /* lsb */ *output_ptr = *input_ptr >> shift;
                input_ptr ++;
		if (msb) *output_ptr |= *input_ptr >> (8-shift);
		else /* lsb */ *output_ptr |= *input_ptr << (8-shift);
                output_ptr ++;
                remaining_bits -= 8;
        }
        COMMENT (( now operating remaining bits ))
        if (remaining_bits) {
		if (msb) *output_ptr = *input_ptr << shift;
		else /* lsb */ *output_ptr = *input_ptr >> shift;
                if (remaining_bits+shift<=8) {
			COMMENT ((this input octet is the last one))
			if (msb) {
                        	mask = (0x1 << (8-remaining_bits)) - 1;
                        	*output_ptr &= ~mask;
			} else { /* lsb */
                        	mask = (0x1 << (remaining_bits)) - 1;
                        	*output_ptr &= mask;
			}
                } else {
			COMMENT ((there remains a few bits to read in the next input octet))
                        remaining_bits -= (8-shift);
                        input_ptr ++;
                        if (msb) *output_ptr |= *input_ptr >> (8-shift);
			else /* lsb */ *output_ptr |= *input_ptr << (8-shift);
			if (msb) {
				mask = (0x1 << (shift-remaining_bits)) - 1;
				/* mask = (0x1 << (8-remaining_bits)) - 1; */
                        	*output_ptr &= ~mask;
			} else { /* lsb */
				mask = (0x1 << (8-shift+remaining_bits)) - 1;
                        	*output_ptr &= mask;
			}
                }
        }
        return(Output);
}
DataType_t BitConcat_sb(DataType_t Input1, Natural l1, DataType_t Input2, Natural l2, int msb)
{
        DataType_t Output;
        int byte_length, whole_byte_len;
        int shift, mask, remaining_bits, already_written;
        unsigned char *input_ptr, *output_ptr;

        byte_length = (l1+l2+7)/8;
        if (l1 > Input1.Length*8) {
                xPrintString("BitConcat_sb error : bits of input 1 out of range\n");
                return(Output);
        }
        if (l2 > Input2.Length*8) {
                xPrintString("BitConcat_sb error : bits of input 2 out of range\n");
                return(Output);
        }

        memset(&Output, 0, sizeof(Output));
	if (!byte_length) return Output;
        Output.Bits = (unsigned char *)xAlloc_SDL_Bit_String((xptrint)byte_length);
        Output.Length = byte_length;

        output_ptr = Output.Bits;

        COMMENT(( working through Input1))
	if (l1) {
        	input_ptr = Input1.Bits;
        	remaining_bits = l1%8;
		whole_byte_len = l1/8;
        	memcpy(output_ptr, input_ptr, whole_byte_len);
        	output_ptr += whole_byte_len;
        	input_ptr += whole_byte_len;
		already_written = 0;

        	if (remaining_bits) {
			COMMENT (( making the junction :
			the remaining bits of Input1 with the first bits of Input2 ))
                 	unsigned char c;
                 	*output_ptr = *input_ptr;
                 	shift = remaining_bits;
                 	if (msb) {
                         	c = Input2.Bits[0] >> shift;
                         	mask = (0x1 << (8-shift)) - 1;
                         	*output_ptr = (*output_ptr & ~mask) | c;
                 	} else {
                         	COMMENT (( LSB first ))
                         	c = Input2.Bits[0] << shift;
                         	mask = (0x1 << shift) - 1;
                         	*output_ptr = (*output_ptr & mask) | c;
                 	}
			already_written = 8 - remaining_bits; COMMENT ((
			this is how many bits of input2 have already
			been written ))
                 	output_ptr ++;
        	}
        	Input2 = BitCut_sb(Input2, already_written, l2-already_written, msb);
	}
        memcpy(output_ptr, Input2.Bits, Input2.Length);
        return(Output);
}

main(int argc, char **argv) 
{
	int first_bit, bit_length;
	int msb;
	DataType_t data1, data2, data3, data4, data_concat;
	unsigned char sample1[3] = { 0xF, 0xF, 0xF };
	unsigned char sample2[4] = { 0x71, 0x71, 0x71, 0x71 };
	unsigned char sample3[15] = { 0x10, 0xAA, 0x6D, 0x09, 0x50, 0xC0, 0x80, 0x3B, 0x26, 0x07, 0x33, 0x02, 0xAF, 0xB2, 0x25 };


	/*
	if (argc != 3) {
		printf("Error\n");
		exit(1);
	}
	*/
	data1.Bits = sample1;
	data1.Length = sizeof(sample1);

	data2.Bits = sample2;
	data2.Length = sizeof(sample2);

	data3.Bits = sample3;
	data3.Length = sizeof(sample3);

#ifdef BITCUT_TEST
	/* MSB */
	msb = 1;
	data4 = BitCut(data3, 0, 4, msb);
	show(data4); printf("-> should be '10'H\n\n");
	data4 = BitCut(data3, 4, 7, msb);
	show(data4); printf("-> should be '0A'H\n\n");
	data4 = BitCut(data3, 11, 18, msb);
	show(data4); printf("-> should be '536840'H\n\n");
	data4 = BitCut(data3, 22, 8, msb);
	show(data4); printf("-> should be '42'H\n\n");
	data4 = BitCut(data3, 30, 60, msb);
	show(data4); printf("-> should be '400103EE981CCC08'H\n\n");

	/* LSB */
	msb = 0;
	data4 = BitCut(data3, 0, 4, msb);
	show(data4); printf("-> should be '00'H\n\n");
	data4 = BitCut(data3, 4, 7, msb);
	show(data4); printf("-> should be '21'H\n\n");
	data4 = BitCut(data3, 11, 18, msb);
	show(data4); printf("-> should be 'B52D01'H\n\n");
	data4 = BitCut(data3, 11, 15, msb);
	show(data4); printf("-> should be 'B52D'H\n\n");
	data4 = BitCut(data3, 11, 16, msb);
	show(data4); printf("-> should be 'B52D'H\n\n");
	data4 = BitCut(data3, 11, 12, msb);
	show(data4); printf("-> should be 'B50D'H\n\n");
	data4 = BitCut(data3, 11, 13, msb);
	show(data4); printf("-> should be 'B50D'H\n\n");
	data4 = BitCut(data3, 11, 11, msb);
	show(data4); printf("-> should be 'B505'H\n\n");
	data4 = BitCut(data3, 22, 8, msb);
	show(data4); printf("-> should be '25'H\n\n");
	data4 = BitCut(data3, 30, 60, msb);
	show(data4); printf("-> should be '400103EE981CCC08'H\n\n");
#endif
	/* LSB test */
	msb = 0;
	show(data3, "original");
	data4 = BitCut(data3, 0, 4, msb);
	data_concat = data4;
	data4 = BitCut(data3, 4, 7, msb);
	data_concat=BitConcat_sb(data_concat, 4, data4, 7, msb);
	data4 = BitCut(data3, 11, 18, msb);
	data_concat=BitConcat_sb(data_concat, 11, data4, 18, msb);
	data4 = BitCut(data3, 29, 5, msb);
	data_concat=BitConcat_sb(data_concat, 29, data4, 5, msb);
	data4 = BitCut(data3, 34, 16, msb);
	data_concat=BitConcat_sb(data_concat, 34, data4, 16, msb);
	data4 = BitCut(data3, 50, 17, msb);
	show(data_concat, "intermediate");
	data_concat=BitConcat_sb(data_concat, 50, data4, 17, msb);
	data4 = BitCut(data3, 67, 15*8-67, msb);
	data_concat=BitConcat_sb(data_concat, 67, data4, 15*8-67, msb);
	show(data_concat, "concat LSB first");
	/* MSB test */
	msb = 1;
	show(data3, "original");
	data4 = BitCut(data3, 0, 4, msb);
	data_concat = data4;
	data4 = BitCut(data3, 4, 7, msb);
	data_concat=BitConcat_sb(data_concat, 4, data4, 7, msb);
	data4 = BitCut(data3, 11, 18, msb);
	data_concat=BitConcat_sb(data_concat, 11, data4, 18, msb);
	data4 = BitCut(data3, 29, 5, msb);
	data_concat=BitConcat_sb(data_concat, 29, data4, 5, msb);
	data4 = BitCut(data3, 34, 16, msb);
	data_concat=BitConcat_sb(data_concat, 34, data4, 16, msb);
	data4 = BitCut(data3, 50, 17, msb);
	show(data_concat, "intermediate");
	data_concat=BitConcat_sb(data_concat, 50, data4, 17, msb);
	data4 = BitCut(data3, 67, 15*8-67, msb);
	data_concat=BitConcat_sb(data_concat, 67, data4, 15*8-67, msb);
	show(data_concat, "concat MSB first");
}
