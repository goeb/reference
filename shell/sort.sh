#!/bin/sh

get_list() {
	echo p1
	echo p6
	echo p2
	echo p23
	echo p10
}

sort_0() {
	echo "sort_0: unsorted"
	get_list
}

sort_1() {
	echo "sort_1: command 'sort'"
	get_list | sort
}

sort_2() {
	echo "sort_2: awk"
	get_list | awk '
		{i=$1; sub(/.*[^0-9]/, "", i); a[i] = $1}
		END { for (i in a) print a[i] }
	'
}

sort_3() {
	echo "sort_3: sed & grep & awk"
	get_list | while read line; do
	    # add numeric prefix
		prefix=$(echo $line | sed -e "s/.*[^0-9]//")
		echo "$prefix $line"
	done | sort -n | awk '{print $2}'
}

sort_0
sort_1
sort_2
sort_3
