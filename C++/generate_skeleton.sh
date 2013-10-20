#!/bin/sh

file=$1
if [ "$file" = "" ]; then
	echo "Usage: $0 file.h"
	exit 1
fi

ofile_h=$file.hpp
ofile_c=$file.cpp

#sed -e 's/\([^a-zA-Z_0-9:. \t]\)/ \1 /g' | sed -e 's/\([^:]\)\(:\)\([^:]\)/\1 \2 \3/g' |
cpp  -dI -P sample.cpp 2>/dev/null |
awk -v h_file=$ofile_h -v c_file=$ofile_c 'BEGIN {
	class_name = "";
	DoPrintH = 1;
	is_private = 1;
}
$1 ~ /^class/ { class_name = $2; print "class name=", class_name; }
$1 ~ /^private/ { is_private = 1; }
$1 ~ /^public/ || $1 ~ "^protected" { is_private = 0; }
NF == 0 { DoPrintH = 0;}
$1 ~ /static/ {
		printH($0);
		$1="";
		printC($0);
}
$0 ~ /(/ { ; }
DoPrintH==1 { printH($0); }
DoPrintH==0 { DoPrintH = 1; }
END {
}
function is_in_private() {
	if (class_name != "" && is_private==1) {
		return 1;
	} else {
		return 0;
	}
}
function printH(str) {
	if (is_in_private()) {
		# no print
	} else {
		print "HPP:", str;
	}
}
function printC(str) {
	if (is_in_private()) {
		# no print
	} else {
		print "CPP:", str;
	}
}'

