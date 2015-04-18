class node:
	def __init__(self, name):
		self.name = name
		self.previous = None
		self.next = None
	def __str__(self):
		return self.name

	def show_next(self):
		print self, '->',
		if self.next != None: self.next.show_next()
		else: print

	def show_previous(self):
		print self, '<-',
		if self.previous != None: self.previous.show_previous()
		else: print

	def insert(self, node):
		node.next = self
		node.previous = self.previous
		if self.previous != None: self.previous.next = node
		self.previous = node

x = node('N1')
z = node('N3')
head = x
head.next = z
z.previous = head

x.show_next()
z.show_previous()

print "-- adding a node --"
y = node('N2')
z.insert(y)
x.show_next()
z.show_previous()

print "-- modifying a node --"
x.name="ZOZO"

x.show_next()
z.show_previous()
