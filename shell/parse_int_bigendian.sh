#!/bin/sh

# parse a 4-byte big-endian encoded int
#
# Example:
# bytes: 00 12 34 56
# integer: 0x123456
# 

cat_binary() {
	# Use env in order to use the system printf command
	# instead of the shell built-in, as some built-ins
	# cannot interpret \x..
    env printf "\x00\x12\x34\x56"
}

parse_4bytes_bigendian() {
	b0=$(cat_binary | hexdump -C | awk '{print $2; exit}')
	b1=$(cat_binary | hexdump -C | awk '{print $3; exit}')
	b2=$(cat_binary | hexdump -C | awk '{print $4; exit}')
	b3=$(cat_binary | hexdump -C | awk '{print $5; exit}')

	echo "bytes: $b0 $b1 $b2 $b3"

	result=$((0x$b0*16777216 + 0x$b1*65536 + 0x$b2*256 + 0x$b3))
	
	printf "integer: 0x%x\n" $result
}

parse_4bytes_bigendian
