
#import module2

print __name__
self='tyty'

class Child:
    _id = None
    def __init__(Xself, i, manager):
        Xself._id = i
        manager.registerKey(Xself._id, "toto");


    def display(self):
        print "child: ", self._id

class Manager:
    _children = [ ]
    _keys = {}

    def registerKey(self, childId, key):
        self._keys[childId] = key

    def initChildren(Xself):
        for i in range(0, 5):
            Xself._children.append(Child(i, Xself))

    def display(self):
        print "Manager:"
        for child in self._children:
            child.display()


M = Manager()
M.initChildren()
M.display()
