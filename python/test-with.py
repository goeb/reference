#!/usr/bin/env python3

# Execution: python test-with.py
# Manager.__init__
# with...
# Manager.__enter__
# number= 43
# Manager.__exit__
# m= <__main__.Manager object at 0x7e8b1ab5a9b0>
# end

class Manager:
    def __init__(self):
        print("Manager.__init__")

    def __enter__(self):
        print("Manager.__enter__")
        return 43

    def __exit__(self, *args):
        print("Manager.__exit__")


m = Manager()
print("with...")
with m as number:
    print("number=", number)

print("m=", m)
print("end")
