/*
 * Example of characters hidden in a string.
 * Unicode Variation Selectors are used:
 * name:    VS1      .. VS16
 * unicode: U+FE01   .. U+FE0F
 * hexa:    0xefb880 .. 0xefb88f
 *
 */
#include <stdio.h>
int main()
{
	printf("V1-16=︀︁︂︃︄︅︆︇︈︉︊︋︌︍︎️\n"); // this line has VS1-16 characters
}
