#!/usr/bin/python

from fltk import *

# caveat:
# the labeltext trick is necessary so that the memory space for widget.label()
# is not freed when the box_cb function terminates
labeltext = ""

def button_cb(widget) :
	global labeltext
	# caveat : the value method return a character \0 or \1 !!
	# that is why we use ord(widget.value())
	labeltext = "value="+str(ord(widget.value()))
	widget.label(labeltext)

window = Fl_Window(120, 75)

button = Fl_Light_Button(10, 10, 100, 25, "click")
button.callback(button_cb)

window.end()
window.show()
Fl.run()
