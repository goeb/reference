# Meson example1

This example shows:

- configuration of a "hello world" project at build time
- compilation
- test

```
$ meson setup build
$ cd build

$ meson configure
....
  Project options    Current Value        Possible Values      Description                   
  -----------------  -------------        ---------------      -----------                   
  CONF_PATH          /etc/example1.conf                        Path to the configuration file

$ meson configure -DCONF_PATH=/etc/example1-other.conf
$ meson compile
$ ./example1
hello world: CONF_PATH=/etc/example1-other.conf

$ meson test
...
1/2 basic              OK              0.01s
2/2 basic error        EXPECTEDFAIL    0.00s   exit status 1

Ok:                 1   
Expected Fail:      1   
Fail:               0   
Unexpected Pass:    0   
Skipped:            0   
Timeout:            0   

Full log written to .../example1/build/meson-logs/testlog.txt
```
