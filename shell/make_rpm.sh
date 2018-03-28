#!/bin/sh

usage() {
	echo "usage: $0 [options] <skeleton>"
	echo
	echo "Create a RPM package from a source directory."
	echo
	echo "Arguments:"
	echo "    <skeleton>"
	echo "        Use <skeleton> as the source directory. All files in <skeleton> shall"
   	echo "        be packaged in the RPM."
	echo
	echo "Options:"
	echo "    -o, --output <file>"
	echo "        Write the RPM package to FILE. The default is <pkg-name>-<pkg-version>.rpm."
	echo
	echo "    --pkg-name <pkg-name>"
	echo "        Use <pkg-name> as the name of the package. The default is the basename of <skeleton>."
	echo
	echo "    --pkg-version <pkg-version>"
	echo "        Use <pkg-version> as the version of the package. The default is '1.0.0'."
	echo
	exit 1
}

die() {
	msg="$*"
	if [ -n "$msg" ]; then
		echo "$msg" >&2
	fi
	echo "abort." >&2
	exit 1
}

# Generate the .spec file to stdout
# $1 : package name (ex: hello_world)
# $2 : source directory
# $3 : package version (ex: 1.0.0)
gen_spec() {
	pkg_name="$1"
	src_root_dir="$2"
	pkg_version="$3"
	cat << EOF
Summary: Sample testing package '$pkg_name'
Name: $pkg_name
Version: $pkg_version
Release: 1 
License: public domain
BuildRoot: $src_root_dir
BuildArch: noarch

%files
/

%description
description line 1 ...
description line 2 ...
description line 3 ...

%clean
# prevent rpmbuild from deleting the source directory
EOF
}

# output: $work_dir/RPMS/noarch/hello_world-1.0.0-1.noarch.rpm
rpm_build() {
	spec_file="$1"
	src_root_dir="$2"
	work_dir="$3"
	output_rpm="$4"
	rpmbuild -bb "$spec_file" --buildroot="$src_root_dir" --define "_topdir $work_dir" || die
	mv "$work_dir"/RPMS/noarch/*.rpm "$output_rpm"
}

# main

[ $# -ne 0 ] || usage

# default values
pkg_version=1.0.0

while [ $# -ne 0 ]; do
	arg="$1"; shift
	case "$arg" in
		-h|--help) usage;;
		--pkg-name) [ $# -eq 0 ] && usage; pkg_name="$1"; shift ;;
		--pkg-version) [ $# -eq 0 ] && usage; pkg_version="$1"; shift ;;
		-o|--output) [ $# -eq 0 ] && usage; output_rpm="$1"; shift ;;
		*) skeleton_dir="$arg";;
	esac
done

[ -d "$skeleton_dir" ] || die "not a directory: $skeleton_dir"

[ "$pkg_name" = "" ] && pkg_name=$(basename "$skeleton_dir")
[ "$output_rpm" = "" ] && output_rpm="$pkg_name-$pkg_version.rpm"

work_dir=$(mktemp --directory /tmp/rpmbuild_XXXX)
spec_file="$work_dir/x.spec"

gen_spec "$pkg_name" "$skeleton_dir" "$pkg_version" > "$spec_file"

rpm_build "$spec_file" "$skeleton_dir" "$work_dir" "$output_rpm"

echo rm -rf "$work_dir"
rm -rf "$work_dir"
echo "generated: $output_rpm"
