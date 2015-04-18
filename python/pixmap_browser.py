#!/usr/bin/python

from fltk import *


def load_file(n) :
	if img : img.release


def file_cb(n) :
	global name, window
	if n==name : return
	load_file(n)
	name = n
	window.label(name)


def button_cb(widget) :
	fl_file_chooser_callback(file_cb)
	fl_file_chooser("Image file?", "*.{bm,bmp,gif,jpg,pbm,pgm,png,ppm,xbm,xpm}", name)
	fl_file_chooser_callback(0)

window = Fl_Window(400, 400)
box = Fl_Box(0, 0, window.w(), window.h())
box.box(FL_FLAT_BOX)
button = Fl_Button(5, 5, 100, 35, "load")
button.callback(button_cb)
window.resizable(window)
window.show()
Fl.run()

