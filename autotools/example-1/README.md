
This example shows how to use autools to set an alternate value at configuration time.

Run the example:

Setup:
```
$ autoreconf -ivf
$ mkdir build
$ cd build
```

First build with default value:
```
$ ../configure
$ make
$ src/example1
example-1: VAR_A=default value of var-a
```

Second build with alternate value:
```
$ ../configure --with-var-a=OTHER-VALUE
$ make
$ src/example1
example-1: VAR_A=OTHER-VALUE
```
