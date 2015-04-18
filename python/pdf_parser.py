
import sys

index = 0

contents = file(sys.argv[1]).read()

def is_blank(c) :
	if c in '\x00\t\n\x0c\r ' : return True
	else : return False

def skip_blanks() :
	global index
	while is_blank(contents[index]) :
		index = index + 1

def is_special(c) :
	if c in '()<>[]{}/%' : return True
	else : return False

def skip_to_eol() :
	global index
	while contents[index] not in '\r\n' :
		index = index + 1

def view_token() :
	global index
	save_index = index
	t = read_token()
	index = save_index
	return t

def read_token() :
	global index
	skip_blanks()
	token = ''
	c = contents[index]
	if is_special(c) :
		if contents[index:index+2] in [ '<<', '>>' ] :
			token = contents[index:index+2]
			index = index + 2
		else :
			token = c
			index = index + 1
	else :
		while not is_blank(c) and not is_special(c) :
			token = token + c
			index = index + 1
			c = contents[index]

	return token

def read_dictionnary() :
	d = { }
	while view_token() != '>>' :
		name = read_element() # should be /name
		element = read_element()
		#print "++", "element=", element
		try :
			d[name] = element
		except :
			print 'name=', name
			raise
	
	read_token() # consume '>>'
	return d

def read_string() :
	global index
	level = 0
	s = ''
	c = contents[index]
	while level >= 0 :
		if c == ')' : level = level - 1
		if c == '(' : level = level + 1
		if level >=0 : s = s + c
		index = index + 1
		c = contents[index]
	
	index = index + 1 # consume ')'
	return s

def read_array() :
	a = [ ]
	while view_token() != ']' :
		element = read_element()
		a.append(element)
	
	read_token() # consume ']'
	return a
	
	
def read_element() :
	global index
	t = read_token()
	if t == '<<' : element = read_dictionnary()
	elif t == '/' : element = '/' + read_token()
	#elif t == '<' : element = read_hexstring()
	elif t == '[' : element = read_array()
	elif t == '(' : element = read_string()
	else :
		if t.isdigit() : # find out if is it a reference
			save_index = index
			a = read_token()
			r = read_token()
			if r == 'R' : # it is a reference
				element = [ 'R', t, a ]
			else :
				index = save_index
				element = t
		else :
			element = t

	return element
	
def skip_to_endstream() :
	global index
	while contents[index:index+9] != 'endstream' :
		index = index + 1

	index = index + 9

def read_obj(id) :
	id = int(id)
	id_gen = int(read_token())
	t = read_token()
	if t != 'obj' :
		# error
		raise Exception('obj expected ! (found %s)' % t)

	read_element()
	t = read_token()
	if t == 'stream' :
		#print 'stream'
		skip_to_endstream()
		read_token() # should be endobj
		#print 'endobj'
	elif t == 'endobj' :
		#print 'endobj'
		None
	else :
		raise Exception('not supported %s in read_obj()' % t)
	

def read_startxref() :
	t = read_token() # should be 'startxref'
	t = read_token()

def read_trailer() :
	t = read_token() # should be '<<'
	print 'read_trailer: t=', t
	read_dictionnary()
	read_startxref()

def read_xref() :
	while read_token() != 'trailer' :
		None

	read_trailer()

while True :
	t = read_token()
	if t == 'xref' :
		read_xref()
	elif t == '%' :
		if contents[index:index+4] == '%EOF' : break
		print 'comment'
		skip_to_eol()
	else :
		# obj
#		print 'tok=', t
		read_obj(t)


