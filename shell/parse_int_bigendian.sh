#!/bin/sh

# parse a 4-byte big-endian encoded int
#
# Example:
# $ sh parse_int_bigendian.sh
# Method 1:
# bytes: 00 12 34 56
# integer: 0x123456
# Method 2:
# integer: 0x123456
# Method 3:
# integer: 0x123456
# 

cat_binary() {
	# Use env in order to use the system printf command
	# instead of the shell built-in, as some built-ins
	# cannot interpret \x..
    env printf "\x00\x12\x34\x56"
}

parse_4bytes_bigendian_1() {
	echo "Method 1:"
	b0=$(cat_binary | hexdump -C | awk '{print $2; exit}')
	b1=$(cat_binary | hexdump -C | awk '{print $3; exit}')
	b2=$(cat_binary | hexdump -C | awk '{print $4; exit}')
	b3=$(cat_binary | hexdump -C | awk '{print $5; exit}')

	echo "bytes: $b0 $b1 $b2 $b3"
	result=$((0x$b0*16777216 + 0x$b1*65536 + 0x$b2*256 + 0x$b3))
	printf "integer: 0x%x\n" $result
}

parse_4bytes_bigendian_2() {
	echo "Method 2:"
	hex=$(cat_binary | hexdump -C | awk '{print "0x" $2 $3 $4 $5; exit}')
	result=$(($hex))
	printf "integer: 0x%x\n" $result
}

parse_4bytes_bigendian_3() {
	echo "Method 3:"
	hex=$(cat_binary | hexdump -e '/1 "%02x"')
	result=$((0x$hex))
	printf "integer: 0x%x\n" $result
}

parse_4bytes_bigendian_1
parse_4bytes_bigendian_2
parse_4bytes_bigendian_3
