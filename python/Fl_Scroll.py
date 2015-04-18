#!/usr/bin/python

from fltk import *

class background(Fl_Widget) :
	def draw(self) :
		fl_color(FL_DARK3)
		fl_rectf(self.x(), self.y(), self.w(), self.h())

window = Fl_Window(100, 100)
window.box(FL_NO_BOX)
scroll = Fl_Scroll(0, 0, 100, 100)
scroll.getScrollbar().align(FL_ALIGN_LEFT+FL_ALIGN_TOP)
inside = background(0, 0, 200, 200)
scroll.end()
window.resizable(scroll)


window.end()
window.show()
Fl.run()
