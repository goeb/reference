#!/usr/bin/python

from fltk import *

def equation(x, y):
	global args
	x0 = args[0]
	y0 = args[1]
	A = args[2]
	B = args[3]
	C = args[4]
	D = args[5]
	v = (x-x0)*(x-x0)*A + (y-y0)*(y-y0)*B + C*x*y + D
	return v

class Drawing(Fl_Widget) :
	def draw(self) :
		global args
		fl_push_clip(self.x(), self.y(), self.w(), self.h())
		for xi in range(0, self.w()/2):
			for yi in range(0, self.h()/2):
				pix = equation(xi/2, yi/2)
				if pix > 0 : fl_color(FL_DARK3)
				else : fl_color(FL_WHITE)
				fl_point(xi*2, yi*2)
		fl_pop_clip()


def slider_cb(widget, v) :
	global args, drawing
	args[v] = widget.value()
	drawing.redraw()

# "storage_area" is a storage array for widgets, so that
# they are not deleted if their variable name is deaffected
storage_area = []
args=[-5, 1, -2, 0, 1, 0]
name=["x0", "y0", "A", "B", "C", "D"]
window = Fl_Window(100,100,300,500)
drawing = Drawing(10, 10, 280, 280)
y = 300
for n in range(6) :
	s = Fl_Hor_Value_Slider(50, y, 240,25, name[n])
	y = y+25
	if n <= 1:
		s.minimum(-140)
		s.maximum(140)
	else :
		s.minimum(-10)
		s.maximum(10)
	s.step(1)
	s.value(args[n])
	s.align(FL_ALIGN_LEFT)
	s.callback(slider_cb, n)
	# store s, so that the s widget is not deleted on next loop
	storage_area.append(s)

window.end()
window.show()
Fl.run()
