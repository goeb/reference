#!/bin/sh

usage() {
	echo "usage: $0 [option] FILE ..."
	exit 1
}

while getopts "vo:" option; do
	case $option in
		v) verbose=1;;
		o) output=$OPTARG;;
		*) usage;;
	esac
done
shift $((OPTIND-1))

echo verbose=$verbose
echo output=$output

while [ $# -ne 0 ]; do
	echo arg=$1
	shift
done

