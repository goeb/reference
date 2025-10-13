# Test various bitbake recipes

## Setup environment

```
git clone https://github.com/openembedded/bitbake.git
export BITBAKE=$PWD/bitbake
export PATH=$PATH:$BITBAKE/bin
export PYTHONPATH=$PYTHONPATH:$BITBAKE/lib
export BBPATH=.
export BB_ENV_PASSTHROUGH_ADDITIONS=BBFILES
```

## bitbake hello

```
$ export BBFILES=hello/hello.bb
$ bitbake hello

Loading cache: 100% |...
Loaded 0 entries from dependency cache.
WARNING: hello/hello.bb: hello world
WARNING: hello/hello.bb: name=alice, age=42
WARNING: hello/hello.bb: name=bob, age=None
WARNING: hello/hello.bb: name=charlie, age=None
WARNING: hello/hello.bb: X=X10 X12 X13
Parsing recipes: 100% |#####################################################...
Parsing of 1 .bb files complete (0 cached, 1 parsed). 1 targets, 0 skipped, 0 masked, 0 errors.
NOTE: Resolving any missing task queue dependencies
Initialising tasks: 100% |##################################################...
NOTE: No setscene tasks
NOTE: Executing Tasks
WARNING: hello world
WARNING: name=alice, age=42
WARNING: name=bob, age=None
WARNING: name=charlie, age=None
WARNING: X=X10 X12 X13
WARNING: None do_xx: do_xx
WARNING: hello world
WARNING: name=alice, age=42
WARNING: name=bob, age=None
WARNING: name=charlie, age=None
WARNING: X=X10 X12 X13
WARNING: None do_build: Function do_build doesn't exist
NOTE: Tasks Summary: Attempted 2 tasks of which 0 didn't need to be rerun and all succeeded.

Summary: There were 17 WARNING messages.
```

## bitbake test-inherit

```
$ export BBFILES=test-inherit/test-inherit.bb
$ bitbake test-inherit

Loading cache: 100% |...
Loaded 0 entries from dependency cache.
WARNING: test-inherit/test-inherit.bb: in test-inherit.bb...
WARNING: test-inherit/test-inherit.bb: in test3.bbclass: A=This is A
WARNING: test-inherit/test-inherit.bb: in test1.bbclass: A=This is A
WARNING: test-inherit/test-inherit.bb: in test2.bbclass: A=This is A
Parsing recipes: 100% |#####################################################...
Parsing of 1 .bb files complete (0 cached, 1 parsed). 1 targets, 0 skipped, 0 masked, 0 errors.
NOTE: Resolving any missing task queue dependencies
Initialising tasks: 100% |##################################################...
NOTE: No setscene tasks
NOTE: Executing Tasks
WARNING: in test-inherit.bb...
WARNING: in test3.bbclass: A=This is A
WARNING: in test1.bbclass: A=This is A
WARNING: in test2.bbclass: A=This is A
WARNING: None do_build: Function do_build doesn't exist
NOTE: Tasks Summary: Attempted 1 tasks of which 0 didn't need to be rerun and all succeeded.

Summary: There were 9 WARNING messages.
```

## Troubleshooting PermissionError

When using Ubuntu 24.04, you might encounter this kind of error:

```
ERROR: PermissionError: [Errno 1] Operation not permitted

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File ".../bitbake/bin/bitbake-worker", line 286, in child
    bb.utils.disable_network(uid, gid)
  File ".../bitbake/lib/bb/utils.py", line 2032, in disable_network
    with open("/proc/self/uid_map", "w") as f:
PermissionError: [Errno 1] Operation not permitted
```

This error comes from the apparmor configuration.
See this page for configuring: <https://discourse.ubuntu.com/t/ubuntu-24-04-lts-noble-numbat-release-notes/39890>.

