
class FakeComposite:

    def __init__(self, path=''):
        if path == '': path = hex(id(self)).replace('0x', '').replace('L', '')
        self.path = '%s' % path
        self.current = 0

    def __iter__(self):
        self.current = 0
        self.high = 3
        return self

    def next(self): # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            newpath = self.path + '[%s]' % self.current
            return FakeComposite(newpath)

    def __repr__(self):
        return 'FC_%s' % (self.path)

    def __getitem__(self, i):
        return FakeComposite(self.path + '[%s]' % i)

    def __setitem__(self, key, value):
        pass

    def __str__(self):
        return self.__repr__()

    def __getattr__(self, key):
        return FakeComposite(self.path + '.%s' % key)

    def __call__(self, *args):
        return FakeComposite('%s%s' % (self.path, args) )

x = FakeComposite()
y = FakeComposite()
print "x=", x, "y=", y
for c in x:
    print "c=", c
    for d in c:
        print "    d=", d

print "x[23]=", x[23]
print "x['foo']=", x['foo']
print "x[x]=", x[x]
print "x.bar=", x.bar
x[1] = 'abc'
print "x...=", x['foo']['bar'][1].name.x.y.z

print x.isOpen('one', 333)
print x.connect('one', 333)[55]

