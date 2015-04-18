
import os
import sys

progname = sys.argv.pop(0)
first_file = sys.argv.pop(0)

def files_which_include(this_file) :
	file_list = []
	cmd = 'grep -H '+ this_file +" t*.h | grep include | sed -e 's/:.*//'"
	#print 'cmd=', cmd
	p = os.popen3("grep -H "+ this_file +" t*.h | grep include | sed -e 's/:.*//'")
	str = p[1].read()
	return str.split()


already_processed = []

def process_file(file, level) :
	global already_processed
	indentation = ' ' * level
	print indentation + file,
	if file in already_processed :
		print '*'
	else :
		print
		already_processed.append(file)
		list = files_which_include(file)
		#print "list=", list
		while len(list) > 0 :
			process_file(list.pop(0), level+1)
	

process_file(first_file, 0)



