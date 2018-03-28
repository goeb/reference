#!/bin/sh

usage() {
	echo "usage: $0 [options] FILE ..."
	echo
	echo "Options:"
	echo "    -v, --verbose"
 	echo "                    Be verbose"
	echo
	echo "    -o, --output FILE"
	echo "                    Specify an output file name"
	exit 1
}

TEMP=$(getopt -o vo: --long verbose,output: -n "$0" -- "$@")
echo TEMP=$TEMP

if [ $? != 0 ]; then exit 1; fi

eval set -- "$TEMP"

printArgs() {
	while [ $# -ne 0 ]; do
		echo printArgs: arg=$1
		shift
	done
}

printArgs "$@"

# extract options
while [ $# -ne 0 ]; do
	case "$1" in
		-o|--output) output=$2; shift 2;;
		-v|--verbose) verbose=1; shift;;
		--) shift; break;;
		*) usage;;
	esac
done

echo verbose=$verbose
echo output=$output

# non-option arguments
while [ $# -ne 0 ]; do
	echo arg=$1
	shift
done

