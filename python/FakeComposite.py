
class FakeComposite:

    def __init__(self, path=''):
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
        return 'FakeComposite-%s' % (self.path)

    def __getitem__(self, i):
        return FakeComposite(self.path + '[%s]' % i)

    def __setitem__(self, key, value):
        pass

    def x__getattr__(self, key):
        print 'key=', key
        if key == '__call__': self.__call__()
        return FakeComposite(self.level+1)

x = FakeComposite(55)
print x
for c in x:
    print "c=", c
    for d in c:
        print "    d=", d

print "x[23]=", x[23]
print "x['foo']=", x['foo']
print "x[x]=", x[x]
#print "x.bar=", x.bar
x[1] = 'abc'
