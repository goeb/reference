
class A:
    def __len__(self):
        return 4455

    def __str__(self):
        return "[class A: toto]"

    def __repr__(self):
        return "[REPR/class A: toto]"

    def __call__(self, x):
        print "__call__: x=", x

    def __iter__(self):
        yield 'a'
        yield 'b'
        yield 'c'

a = A()
print "len(a)=", len(a)
print "a=", a
a(12)
for i in a:
    print "i=", i
