#!/usr/bin/python

from fltk import *
import sys


window = Fl_Window(100,100,300,500)

s = Fl_Hor_Value_Slider(50, 300, 240,25, "hello")
s = Fl_Hor_Value_Slider(50, 350, 240,25, "hello")

window.label(sys.argv[0])
window.end()
window.show(len(sys.argv), sys.argv)
Fl.run()


