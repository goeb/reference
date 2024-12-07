# Yocto & U-Boot
Date: 2024-12-07

This page shows how to build u-boot for a qemuarm64 machine and boot it in the
emulator.

```bash
$ git clone --branch scarthgap https://git.yoctoproject.org/poky
$ . poky/oe-init-build-env
build$ export MACHINE="qemuarm64"
build$ bitbake u-boot
build$ bitbake core-image-minimal

build$ QEMU=tmp/work/x86_64-linux/qemu-helper-native/1.0/recipe-sysroot-native/usr/bin/qemu-system-aarch64
build$ ROOTFS=$PWD/tmp/deploy/images/qemuarm64/core-image-minimal-qemuarm64.rootfs.ext4
build$ UBOOT=tmp/deploy/images/qemuarm64/u-boot.bin
build$ $QEMU -drive id=disk0,file=$ROOTFS,if=none,format=raw \
             -device virtio-blk-device,drive=disk0 \
             -bios $UBOOT \
             -machine virt -cpu cortex-a57 -smp 4 -m 256 \
             -nographic
```

U-Boot starting:
```
U-Boot 2024.01 (Jan 08 2024 - 15:37:48 +0000)

DRAM:  256 MiB
Core:  51 devices, 14 uclasses, devicetree: board
Flash: 64 MiB
Loading Environment from Flash... *** Warning - bad CRC, using default environment

In:    serial,usbkbd
Out:   serial,vidconsole
Err:   serial,vidconsole
No working controllers found
Net:   eth0: virtio-net#32
starting USB...
No working controllers found
Hit any key to stop autoboot:  0

=> ls virtio 0 /
<DIR>       1024 .
<DIR>       1024 ..
<DIR>      12288 lost+found
<DIR>       3072 bin
<DIR>       1024 boot
<DIR>       1024 dev
<DIR>       1024 etc
<DIR>       1024 home
<DIR>       1024 lib
<DIR>       1024 media
<DIR>       1024 mnt
<DIR>       1024 proc
<DIR>       1024 run
<DIR>       1024 sbin
<DIR>       1024 sys
<DIR>       1024 tmp
<DIR>       1024 usr
<DIR>       1024 var
```
