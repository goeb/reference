class A:
        def printA(self):
                print 'A: Class', self.__class__.__name__

        def X(self):
                print 'X of A'

class B:
        def printB(self):
                print 'B: Class', self.__class__.__name__

        def X(self):
                print 'X of B'

class C(A, B):
        pass

a = A()
b = B()
c = C()

a.printA()
b.printB()
c.printA()
c.printB()
c.X()

