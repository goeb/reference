from fltk import *
import sys

def theCancelButtonCallback(ptr):
	print "Exiting...", ptr.label()
	sys.exit(0)

window = Fl_Window(100,100,200,180)
window.label(sys.argv[0])
button = Fl_Button(9,20,180,50)
button.label("Hello Manu")
button.callback(theCancelButtonCallback)
button = Fl_Button(9,90,180,50)
button.label("Hello Fred")
button.callback(theCancelButtonCallback)
window.end()
window.show(len(sys.argv), sys.argv)
Fl.run()
