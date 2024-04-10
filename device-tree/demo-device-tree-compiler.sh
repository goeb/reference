#!/bin/sh

# Demo of dtc, fdtoverlay, dtdiff
#
# $ sh demo-device-tree-compiler.sh
# make_base_dtb base.dtb
# make_dtb_overlay overlay.dtb
# fdtoverlay -i base.dtb -o final.dtb overlay.dtb
# fdtdiff base.dtb final.dtb
# --- /dev/fd/63  2024-04-10 22:15:18.017777788 +0200
# +++ /dev/fd/62  2024-04-10 22:15:18.017777788 +0200
# @@ -6,8 +6,8 @@
#         images {
#  
#                 ramdisk-1 {
# -                       data = < 0x68656c6c 0x6f31310a >;
# -                       some-bytes = < 0x00 0x11 0x22 0xffffffff 0xff >;
# +                       data = [ 68 65 6c 6c 6f 32 2d 77 6f 72 6c 64 0a ];
# +                       some-bytes = < 0x00 0x11 0x22 0x00 0xff >;
#                 };
#         };
#  };
# 

echo hello11 > data1.txt # multiple of 4 bytes, to trigger <...> display
echo hello2-world > data2.txt

make_dtb_base() {
	echo "make_base_dtb $1"
	dtc -I dts -O dtb > "$1" << EOF
/dts-v1/;
/ {
    some-name = "something";
    images {
        ramdisk-1 {
            some-bytes = <0 0x11 0x22 0xffffffff 255>;
            data = /incbin/("data1.txt");
        };
    };
};
EOF
}

make_dtb_overlay() {
	echo "make_dtb_overlay $1"
	dtc -I dts -O dtb > "$1" << EOF
/dts-v1/;
/plugin/;
/ {
    fragment@0 {
        target-path = "/";
        __overlay__ {
            images {
                ramdisk-1 {
                    some-bytes = <0 0x11 0x22 0 255>;
                    data = /incbin/("data2.txt");
                };
            };
        };
    };
};
EOF
}

make_dtb_base base.dtb
make_dtb_overlay overlay.dtb
echo fdtoverlay -i base.dtb -o final.dtb overlay.dtb
fdtoverlay -i base.dtb -o final.dtb overlay.dtb
echo fdtdiff base.dtb final.dtb
dtdiff base.dtb final.dtb
