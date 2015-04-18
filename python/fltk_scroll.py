#!/usr/bin/python

from fltk import *
from math import cos, sin

class Drawing(Fl_Widget) :
	def __init__(self, X, Y, W, H, L) :
		Fl_Widget.__init__(self, X, Y, W, H, L)
		self.align(FL_ALIGN_TOP)
		self.box(FL_FLAT_BOX)
		self.color(FL_WHITE)
	def draw(self) :
		fl_color(FL_DARK3)
		fl_rectf(self.x(), self.y(), self.w(), self.h())
		fl_push_matrix()
		fl_translate(self.x()+self.w()/2, self.y()+self.h()/2)
		fl_scale(self.w()/2, self.h()/2)
		fl_color(FL_BLACK)
		for i in range(20) :
			for j in range(i+1, 20) :
				fl_begin_line()
				fl_vertex(cos(M_PI*i/10+.1), sin(M_PI*i/10+.1))
				fl_vertex(cos(M_PI*j/10+.1), sin(M_PI*j/10+.1))
				fl_end_line()
		fl_pop_matrix()


def box_cb(widget) :
	global thescroll
	if ord(widget.value()) :
		thescroll.box(FL_DOWN_FRAME)
	else :
		thescroll.box(FL_NO_BOX)

	thescroll.redraw()

def type_cb(widget, value) :
	global thescroll
	thescroll.type(value)
	thescroll.redraw()

choices = ( ( "0", 0, type_cb, 0 ),
			( "HORIZONTAL", 0, type_cb, Fl_Scroll.HORIZONTAL ),
			( "VERTICAL", 0, type_cb, Fl_Scroll.VERTICAL ),
			( "BOTH", 0, type_cb, Fl_Scroll.BOTH ),
			( "HORIZONTAL_ALWAYS", 0, type_cb, Fl_Scroll.HORIZONTAL_ALWAYS ),
			( "VERTICAL_ALWAYS", 0, type_cb, Fl_Scroll.VERTICAL_ALWAYS ),
			( "BOTH_ALWAYS", 0, type_cb, Fl_Scroll.BOTH_ALWAYS )
			)

def align_cb(widget, value) :
	global thescroll
	print "debug:align_cb: value=", value
	thescroll.align(value)
	thescroll.redraw()

align_choices = ( ( "left+top", 0, align_cb, (FL_ALIGN_LEFT+FL_ALIGN_TOP) ),
				( "left+bottom", 0, align_cb, (FL_ALIGN_LEFT+FL_ALIGN_BOTTOM) ),
				( "right+top", 0, align_cb, (FL_ALIGN_RIGHT+FL_ALIGN_TOP) ),
				( "right+bottom", 0, align_cb, (FL_ALIGN_RIGHT+FL_ALIGN_BOTTOM) )
				)

window = Fl_Window(5*75, 400)
window.box(FL_NO_BOX)
scroll = Fl_Scroll(0, 0, 5*75, 300)
n = 0
store = []
for y in range(16) :
	for x in range(5) :
		if y>=8 : dy = 5*75
		else : dy = 0
		label =  str(n)
		b = Fl_Button(x*75, y*25+dy, 75, 25, label)
		store.append(label)
		b.labelcolor(FL_WHITE)
		b.color(n)
		n = n+1
		store.append(b)

drawing = Drawing(0, 8*25, 5*75, 5*75, '')
scroll.end()
window.resizable(scroll)
box = Fl_Box(0, 300, 5*75, window.h()-300)
box.box(FL_FLAT_BOX);

but1 = Fl_Light_Button(150, 310, 200, 25, "box")
but1.callback(box_cb)
choice = Fl_Choice(150, 335, 200, 25, "type():")
choice.menu(choices)
choice.value(3)

achoice = Fl_Choice(150, 360, 200, 25, "scrollbar.align():")
achoice.menu(align_choices)
achoice.value(3)

thescroll = scroll

thescroll.align(FL_ALIGN_TOP)

window.end()
window.show()
Fl.run()
