# This file was created automatically by SWIG 1.3.29.
# Don't modify this file, modify the SWIG interface instead.

"""
pyFltk, the Python bindings to the FLTK GUI toolkit.
This is an easy to use and light-weight GUI toolkit
offering basic capabilities for the creation of
graphical user interfaces.
"""

import _fltk
import new
new_instancemethod = new.instancemethod
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


class Fl_Label(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Label instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    value = property(_fltk.Fl_Label_value_get, _fltk.Fl_Label_value_set)
    image = property(_fltk.Fl_Label_image_get, _fltk.Fl_Label_image_set)
    deimage = property(_fltk.Fl_Label_deimage_get, _fltk.Fl_Label_deimage_set)
    type = property(_fltk.Fl_Label_type_get, _fltk.Fl_Label_type_set)
    font = property(_fltk.Fl_Label_font_get, _fltk.Fl_Label_font_set)
    size = property(_fltk.Fl_Label_size_get, _fltk.Fl_Label_size_set)
    color = property(_fltk.Fl_Label_color_get, _fltk.Fl_Label_color_set)
    def draw(*args): return _fltk.Fl_Label_draw(*args)
    def measure(*args): return _fltk.Fl_Label_measure(*args)
    def __init__(self, *args):
        this = _fltk.new_Fl_Label(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Label
Fl_Label.draw = new_instancemethod(_fltk.Fl_Label_draw,None,Fl_Label)
Fl_Label.measure = new_instancemethod(_fltk.Fl_Label_measure,None,Fl_Label)
_fltk.Fl_Label_swigregister(Fl_Label)

class Fl_Widget(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Widget instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Widget:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Widget(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Widget
    def draw(*args): return _fltk.Fl_Widget_draw(*args)
    def handle(*args): return _fltk.Fl_Widget_handle(*args)
    def parent(*args): return _fltk.Fl_Widget_parent(*args)
    def type(*args): return _fltk.Fl_Widget_type(*args)
    def x(*args): return _fltk.Fl_Widget_x(*args)
    def y(*args): return _fltk.Fl_Widget_y(*args)
    def w(*args): return _fltk.Fl_Widget_w(*args)
    def h(*args): return _fltk.Fl_Widget_h(*args)
    def resize(*args): return _fltk.Fl_Widget_resize(*args)
    def damage_resize(*args): return _fltk.Fl_Widget_damage_resize(*args)
    def position(*args): return _fltk.Fl_Widget_position(*args)
    def size(*args): return _fltk.Fl_Widget_size(*args)
    def align(*args): return _fltk.Fl_Widget_align(*args)
    def box(*args): return _fltk.Fl_Widget_box(*args)
    def selection_color(*args): return _fltk.Fl_Widget_selection_color(*args)
    def color(*args): return _fltk.Fl_Widget_color(*args)
    def copy_label(*args): return _fltk.Fl_Widget_copy_label(*args)
    def label(*args): return _fltk.Fl_Widget_label(*args)
    def labeltype(*args): return _fltk.Fl_Widget_labeltype(*args)
    def labelcolor(*args): return _fltk.Fl_Widget_labelcolor(*args)
    def labelfont(*args): return _fltk.Fl_Widget_labelfont(*args)
    def labelsize(*args): return _fltk.Fl_Widget_labelsize(*args)
    def image(*args): return _fltk.Fl_Widget_image(*args)
    def deimage(*args): return _fltk.Fl_Widget_deimage(*args)
    def tooltip(*args): return _fltk.Fl_Widget_tooltip(*args)
    def argument(*args): return _fltk.Fl_Widget_argument(*args)
    def when(*args): return _fltk.Fl_Widget_when(*args)
    def visible(*args): return _fltk.Fl_Widget_visible(*args)
    def visible_r(*args): return _fltk.Fl_Widget_visible_r(*args)
    def show(*args): return _fltk.Fl_Widget_show(*args)
    def hide(*args): return _fltk.Fl_Widget_hide(*args)
    def set_visible(*args): return _fltk.Fl_Widget_set_visible(*args)
    def clear_visible(*args): return _fltk.Fl_Widget_clear_visible(*args)
    def active(*args): return _fltk.Fl_Widget_active(*args)
    def active_r(*args): return _fltk.Fl_Widget_active_r(*args)
    def activate(*args): return _fltk.Fl_Widget_activate(*args)
    def deactivate(*args): return _fltk.Fl_Widget_deactivate(*args)
    def output(*args): return _fltk.Fl_Widget_output(*args)
    def set_output(*args): return _fltk.Fl_Widget_set_output(*args)
    def clear_output(*args): return _fltk.Fl_Widget_clear_output(*args)
    def takesevents(*args): return _fltk.Fl_Widget_takesevents(*args)
    def changed(*args): return _fltk.Fl_Widget_changed(*args)
    def set_changed(*args): return _fltk.Fl_Widget_set_changed(*args)
    def clear_changed(*args): return _fltk.Fl_Widget_clear_changed(*args)
    def take_focus(*args): return _fltk.Fl_Widget_take_focus(*args)
    def set_visible_focus(*args): return _fltk.Fl_Widget_set_visible_focus(*args)
    def clear_visible_focus(*args): return _fltk.Fl_Widget_clear_visible_focus(*args)
    def visible_focus(*args): return _fltk.Fl_Widget_visible_focus(*args)
    default_callback = staticmethod(_fltk.Fl_Widget_default_callback)
    def do_callback(*args): return _fltk.Fl_Widget_do_callback(*args)
    test_shortcut = staticmethod(_fltk.Fl_Widget_test_shortcut)
    def contains(*args): return _fltk.Fl_Widget_contains(*args)
    def inside(*args): return _fltk.Fl_Widget_inside(*args)
    def redraw(*args): return _fltk.Fl_Widget_redraw(*args)
    def redraw_label(*args): return _fltk.Fl_Widget_redraw_label(*args)
    def clear_damage(*args): return _fltk.Fl_Widget_clear_damage(*args)
    def damage(*args): return _fltk.Fl_Widget_damage(*args)
    def draw_label(*args): return _fltk.Fl_Widget_draw_label(*args)
    def measure_label(*args): return _fltk.Fl_Widget_measure_label(*args)
    def window(*args): return _fltk.Fl_Widget_window(*args)
    def color2(*args): return _fltk.Fl_Widget_color2(*args)
    def callback(*args): return _fltk.Fl_Widget_callback(*args)
    def user_data(*args): return _fltk.Fl_Widget_user_data(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Widget(self)
        return weakref_proxy(self)
Fl_Widget.draw = new_instancemethod(_fltk.Fl_Widget_draw,None,Fl_Widget)
Fl_Widget.handle = new_instancemethod(_fltk.Fl_Widget_handle,None,Fl_Widget)
Fl_Widget.parent = new_instancemethod(_fltk.Fl_Widget_parent,None,Fl_Widget)
Fl_Widget.type = new_instancemethod(_fltk.Fl_Widget_type,None,Fl_Widget)
Fl_Widget.x = new_instancemethod(_fltk.Fl_Widget_x,None,Fl_Widget)
Fl_Widget.y = new_instancemethod(_fltk.Fl_Widget_y,None,Fl_Widget)
Fl_Widget.w = new_instancemethod(_fltk.Fl_Widget_w,None,Fl_Widget)
Fl_Widget.h = new_instancemethod(_fltk.Fl_Widget_h,None,Fl_Widget)
Fl_Widget.resize = new_instancemethod(_fltk.Fl_Widget_resize,None,Fl_Widget)
Fl_Widget.damage_resize = new_instancemethod(_fltk.Fl_Widget_damage_resize,None,Fl_Widget)
Fl_Widget.position = new_instancemethod(_fltk.Fl_Widget_position,None,Fl_Widget)
Fl_Widget.size = new_instancemethod(_fltk.Fl_Widget_size,None,Fl_Widget)
Fl_Widget.align = new_instancemethod(_fltk.Fl_Widget_align,None,Fl_Widget)
Fl_Widget.box = new_instancemethod(_fltk.Fl_Widget_box,None,Fl_Widget)
Fl_Widget.selection_color = new_instancemethod(_fltk.Fl_Widget_selection_color,None,Fl_Widget)
Fl_Widget.color = new_instancemethod(_fltk.Fl_Widget_color,None,Fl_Widget)
Fl_Widget.copy_label = new_instancemethod(_fltk.Fl_Widget_copy_label,None,Fl_Widget)
Fl_Widget.label = new_instancemethod(_fltk.Fl_Widget_label,None,Fl_Widget)
Fl_Widget.labeltype = new_instancemethod(_fltk.Fl_Widget_labeltype,None,Fl_Widget)
Fl_Widget.labelcolor = new_instancemethod(_fltk.Fl_Widget_labelcolor,None,Fl_Widget)
Fl_Widget.labelfont = new_instancemethod(_fltk.Fl_Widget_labelfont,None,Fl_Widget)
Fl_Widget.labelsize = new_instancemethod(_fltk.Fl_Widget_labelsize,None,Fl_Widget)
Fl_Widget.image = new_instancemethod(_fltk.Fl_Widget_image,None,Fl_Widget)
Fl_Widget.deimage = new_instancemethod(_fltk.Fl_Widget_deimage,None,Fl_Widget)
Fl_Widget.tooltip = new_instancemethod(_fltk.Fl_Widget_tooltip,None,Fl_Widget)
Fl_Widget.argument = new_instancemethod(_fltk.Fl_Widget_argument,None,Fl_Widget)
Fl_Widget.when = new_instancemethod(_fltk.Fl_Widget_when,None,Fl_Widget)
Fl_Widget.visible = new_instancemethod(_fltk.Fl_Widget_visible,None,Fl_Widget)
Fl_Widget.visible_r = new_instancemethod(_fltk.Fl_Widget_visible_r,None,Fl_Widget)
Fl_Widget.show = new_instancemethod(_fltk.Fl_Widget_show,None,Fl_Widget)
Fl_Widget.hide = new_instancemethod(_fltk.Fl_Widget_hide,None,Fl_Widget)
Fl_Widget.set_visible = new_instancemethod(_fltk.Fl_Widget_set_visible,None,Fl_Widget)
Fl_Widget.clear_visible = new_instancemethod(_fltk.Fl_Widget_clear_visible,None,Fl_Widget)
Fl_Widget.active = new_instancemethod(_fltk.Fl_Widget_active,None,Fl_Widget)
Fl_Widget.active_r = new_instancemethod(_fltk.Fl_Widget_active_r,None,Fl_Widget)
Fl_Widget.activate = new_instancemethod(_fltk.Fl_Widget_activate,None,Fl_Widget)
Fl_Widget.deactivate = new_instancemethod(_fltk.Fl_Widget_deactivate,None,Fl_Widget)
Fl_Widget.output = new_instancemethod(_fltk.Fl_Widget_output,None,Fl_Widget)
Fl_Widget.set_output = new_instancemethod(_fltk.Fl_Widget_set_output,None,Fl_Widget)
Fl_Widget.clear_output = new_instancemethod(_fltk.Fl_Widget_clear_output,None,Fl_Widget)
Fl_Widget.takesevents = new_instancemethod(_fltk.Fl_Widget_takesevents,None,Fl_Widget)
Fl_Widget.changed = new_instancemethod(_fltk.Fl_Widget_changed,None,Fl_Widget)
Fl_Widget.set_changed = new_instancemethod(_fltk.Fl_Widget_set_changed,None,Fl_Widget)
Fl_Widget.clear_changed = new_instancemethod(_fltk.Fl_Widget_clear_changed,None,Fl_Widget)
Fl_Widget.take_focus = new_instancemethod(_fltk.Fl_Widget_take_focus,None,Fl_Widget)
Fl_Widget.set_visible_focus = new_instancemethod(_fltk.Fl_Widget_set_visible_focus,None,Fl_Widget)
Fl_Widget.clear_visible_focus = new_instancemethod(_fltk.Fl_Widget_clear_visible_focus,None,Fl_Widget)
Fl_Widget.visible_focus = new_instancemethod(_fltk.Fl_Widget_visible_focus,None,Fl_Widget)
Fl_Widget.do_callback = new_instancemethod(_fltk.Fl_Widget_do_callback,None,Fl_Widget)
Fl_Widget.contains = new_instancemethod(_fltk.Fl_Widget_contains,None,Fl_Widget)
Fl_Widget.inside = new_instancemethod(_fltk.Fl_Widget_inside,None,Fl_Widget)
Fl_Widget.redraw = new_instancemethod(_fltk.Fl_Widget_redraw,None,Fl_Widget)
Fl_Widget.redraw_label = new_instancemethod(_fltk.Fl_Widget_redraw_label,None,Fl_Widget)
Fl_Widget.clear_damage = new_instancemethod(_fltk.Fl_Widget_clear_damage,None,Fl_Widget)
Fl_Widget.damage = new_instancemethod(_fltk.Fl_Widget_damage,None,Fl_Widget)
Fl_Widget.draw_label = new_instancemethod(_fltk.Fl_Widget_draw_label,None,Fl_Widget)
Fl_Widget.measure_label = new_instancemethod(_fltk.Fl_Widget_measure_label,None,Fl_Widget)
Fl_Widget.window = new_instancemethod(_fltk.Fl_Widget_window,None,Fl_Widget)
Fl_Widget.color2 = new_instancemethod(_fltk.Fl_Widget_color2,None,Fl_Widget)
Fl_Widget.callback = new_instancemethod(_fltk.Fl_Widget_callback,None,Fl_Widget)
Fl_Widget.user_data = new_instancemethod(_fltk.Fl_Widget_user_data,None,Fl_Widget)
_fltk.Fl_Widget_swigregister(Fl_Widget)

Fl_Widget_default_callback = _fltk.Fl_Widget_default_callback

Fl_Widget_test_shortcut = _fltk.Fl_Widget_test_shortcut

FL_RESERVED_TYPE = _fltk.FL_RESERVED_TYPE
class Fl_Group(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Group instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Group_draw(*args)
    def begin(*args): return _fltk.Fl_Group_begin(*args)
    def end(*args): return _fltk.Fl_Group_end(*args)
    current = staticmethod(_fltk.Fl_Group_current)
    def children(*args): return _fltk.Fl_Group_children(*args)
    def child(*args): return _fltk.Fl_Group_child(*args)
    def find(*args): return _fltk.Fl_Group_find(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Group:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Group(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Group
    def add(*args): return _fltk.Fl_Group_add(*args)
    def insert(*args): return _fltk.Fl_Group_insert(*args)
    def insert_before(*args): return _fltk.Fl_Group_insert_before(*args)
    def remove(*args): return _fltk.Fl_Group_remove(*args)
    def clear(*args): return _fltk.Fl_Group_clear(*args)
    def resizable(*args): return _fltk.Fl_Group_resizable(*args)
    def add_resizable(*args): return _fltk.Fl_Group_add_resizable(*args)
    def init_sizes(*args): return _fltk.Fl_Group_init_sizes(*args)
    def focus(*args): return _fltk.Fl_Group_focus(*args)
    def _ddfdesign_kludge(*args): return _fltk.Fl_Group__ddfdesign_kludge(*args)
    def forms_end(*args): return _fltk.Fl_Group_forms_end(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Group(self)
        return weakref_proxy(self)
Fl_Group.draw = new_instancemethod(_fltk.Fl_Group_draw,None,Fl_Group)
Fl_Group.begin = new_instancemethod(_fltk.Fl_Group_begin,None,Fl_Group)
Fl_Group.end = new_instancemethod(_fltk.Fl_Group_end,None,Fl_Group)
Fl_Group.children = new_instancemethod(_fltk.Fl_Group_children,None,Fl_Group)
Fl_Group.child = new_instancemethod(_fltk.Fl_Group_child,None,Fl_Group)
Fl_Group.find = new_instancemethod(_fltk.Fl_Group_find,None,Fl_Group)
Fl_Group.add = new_instancemethod(_fltk.Fl_Group_add,None,Fl_Group)
Fl_Group.insert = new_instancemethod(_fltk.Fl_Group_insert,None,Fl_Group)
Fl_Group.insert_before = new_instancemethod(_fltk.Fl_Group_insert_before,None,Fl_Group)
Fl_Group.remove = new_instancemethod(_fltk.Fl_Group_remove,None,Fl_Group)
Fl_Group.clear = new_instancemethod(_fltk.Fl_Group_clear,None,Fl_Group)
Fl_Group.resizable = new_instancemethod(_fltk.Fl_Group_resizable,None,Fl_Group)
Fl_Group.add_resizable = new_instancemethod(_fltk.Fl_Group_add_resizable,None,Fl_Group)
Fl_Group.init_sizes = new_instancemethod(_fltk.Fl_Group_init_sizes,None,Fl_Group)
Fl_Group.focus = new_instancemethod(_fltk.Fl_Group_focus,None,Fl_Group)
Fl_Group._ddfdesign_kludge = new_instancemethod(_fltk.Fl_Group__ddfdesign_kludge,None,Fl_Group)
Fl_Group.forms_end = new_instancemethod(_fltk.Fl_Group_forms_end,None,Fl_Group)
_fltk.Fl_Group_swigregister(Fl_Group)

Fl_Group_current = _fltk.Fl_Group_current

class Fl_End(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_End instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        this = _fltk.new_Fl_End(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_End
_fltk.Fl_End_swigregister(Fl_End)

FL_NORMAL_BROWSER = _fltk.FL_NORMAL_BROWSER
FL_SELECT_BROWSER = _fltk.FL_SELECT_BROWSER
FL_HOLD_BROWSER = _fltk.FL_HOLD_BROWSER
FL_MULTI_BROWSER = _fltk.FL_MULTI_BROWSER
class Fl_Browser_(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Browser_ instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def item_first(*args): return _fltk.Fl_Browser__item_first(*args)
    def item_next(*args): return _fltk.Fl_Browser__item_next(*args)
    def item_prev(*args): return _fltk.Fl_Browser__item_prev(*args)
    def item_height(*args): return _fltk.Fl_Browser__item_height(*args)
    def item_width(*args): return _fltk.Fl_Browser__item_width(*args)
    def item_quick_height(*args): return _fltk.Fl_Browser__item_quick_height(*args)
    def item_draw(*args): return _fltk.Fl_Browser__item_draw(*args)
    def full_width(*args): return _fltk.Fl_Browser__full_width(*args)
    def full_height(*args): return _fltk.Fl_Browser__full_height(*args)
    def incr_height(*args): return _fltk.Fl_Browser__incr_height(*args)
    def item_select(*args): return _fltk.Fl_Browser__item_select(*args)
    def item_selected(*args): return _fltk.Fl_Browser__item_selected(*args)
    def draw(*args): return _fltk.Fl_Browser__draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Browser_:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Browser_(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def select(*args): return _fltk.Fl_Browser__select(*args)
    def select_only(*args): return _fltk.Fl_Browser__select_only(*args)
    def deselect(*args): return _fltk.Fl_Browser__deselect(*args)
    def position(*args): return _fltk.Fl_Browser__position(*args)
    def hposition(*args): return _fltk.Fl_Browser__hposition(*args)
    def display(*args): return _fltk.Fl_Browser__display(*args)
    def has_scrollbar(*args): return _fltk.Fl_Browser__has_scrollbar(*args)
    HORIZONTAL = _fltk.Fl_Browser__HORIZONTAL
    VERTICAL = _fltk.Fl_Browser__VERTICAL
    BOTH = _fltk.Fl_Browser__BOTH
    ALWAYS_ON = _fltk.Fl_Browser__ALWAYS_ON
    HORIZONTAL_ALWAYS = _fltk.Fl_Browser__HORIZONTAL_ALWAYS
    VERTICAL_ALWAYS = _fltk.Fl_Browser__VERTICAL_ALWAYS
    BOTH_ALWAYS = _fltk.Fl_Browser__BOTH_ALWAYS
    def textfont(*args): return _fltk.Fl_Browser__textfont(*args)
    def textsize(*args): return _fltk.Fl_Browser__textsize(*args)
    def textcolor(*args): return _fltk.Fl_Browser__textcolor(*args)
    scrollbar_width = staticmethod(_fltk.Fl_Browser__scrollbar_width)
    def scrollbar_right(*args): return _fltk.Fl_Browser__scrollbar_right(*args)
    def scrollbar_left(*args): return _fltk.Fl_Browser__scrollbar_left(*args)
    def getScrollbar(*args): return _fltk.Fl_Browser__getScrollbar(*args)
    def getHScrollbar(*args): return _fltk.Fl_Browser__getHScrollbar(*args)
    __swig_destroy__ = _fltk.delete_Fl_Browser_
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Browser_(self)
        return weakref_proxy(self)
Fl_Browser_.item_first = new_instancemethod(_fltk.Fl_Browser__item_first,None,Fl_Browser_)
Fl_Browser_.item_next = new_instancemethod(_fltk.Fl_Browser__item_next,None,Fl_Browser_)
Fl_Browser_.item_prev = new_instancemethod(_fltk.Fl_Browser__item_prev,None,Fl_Browser_)
Fl_Browser_.item_height = new_instancemethod(_fltk.Fl_Browser__item_height,None,Fl_Browser_)
Fl_Browser_.item_width = new_instancemethod(_fltk.Fl_Browser__item_width,None,Fl_Browser_)
Fl_Browser_.item_quick_height = new_instancemethod(_fltk.Fl_Browser__item_quick_height,None,Fl_Browser_)
Fl_Browser_.item_draw = new_instancemethod(_fltk.Fl_Browser__item_draw,None,Fl_Browser_)
Fl_Browser_.full_width = new_instancemethod(_fltk.Fl_Browser__full_width,None,Fl_Browser_)
Fl_Browser_.full_height = new_instancemethod(_fltk.Fl_Browser__full_height,None,Fl_Browser_)
Fl_Browser_.incr_height = new_instancemethod(_fltk.Fl_Browser__incr_height,None,Fl_Browser_)
Fl_Browser_.item_select = new_instancemethod(_fltk.Fl_Browser__item_select,None,Fl_Browser_)
Fl_Browser_.item_selected = new_instancemethod(_fltk.Fl_Browser__item_selected,None,Fl_Browser_)
Fl_Browser_.draw = new_instancemethod(_fltk.Fl_Browser__draw,None,Fl_Browser_)
Fl_Browser_.select = new_instancemethod(_fltk.Fl_Browser__select,None,Fl_Browser_)
Fl_Browser_.select_only = new_instancemethod(_fltk.Fl_Browser__select_only,None,Fl_Browser_)
Fl_Browser_.deselect = new_instancemethod(_fltk.Fl_Browser__deselect,None,Fl_Browser_)
Fl_Browser_.position = new_instancemethod(_fltk.Fl_Browser__position,None,Fl_Browser_)
Fl_Browser_.hposition = new_instancemethod(_fltk.Fl_Browser__hposition,None,Fl_Browser_)
Fl_Browser_.display = new_instancemethod(_fltk.Fl_Browser__display,None,Fl_Browser_)
Fl_Browser_.has_scrollbar = new_instancemethod(_fltk.Fl_Browser__has_scrollbar,None,Fl_Browser_)
Fl_Browser_.textfont = new_instancemethod(_fltk.Fl_Browser__textfont,None,Fl_Browser_)
Fl_Browser_.textsize = new_instancemethod(_fltk.Fl_Browser__textsize,None,Fl_Browser_)
Fl_Browser_.textcolor = new_instancemethod(_fltk.Fl_Browser__textcolor,None,Fl_Browser_)
Fl_Browser_.scrollbar_right = new_instancemethod(_fltk.Fl_Browser__scrollbar_right,None,Fl_Browser_)
Fl_Browser_.scrollbar_left = new_instancemethod(_fltk.Fl_Browser__scrollbar_left,None,Fl_Browser_)
Fl_Browser_.getScrollbar = new_instancemethod(_fltk.Fl_Browser__getScrollbar,None,Fl_Browser_)
Fl_Browser_.getHScrollbar = new_instancemethod(_fltk.Fl_Browser__getHScrollbar,None,Fl_Browser_)
_fltk.Fl_Browser__swigregister(Fl_Browser_)

Fl_Browser__scrollbar_width = _fltk.Fl_Browser__scrollbar_width

class Fl_Browser(Fl_Browser_):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Browser instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def item_first(*args): return _fltk.Fl_Browser_item_first(*args)
    def item_next(*args): return _fltk.Fl_Browser_item_next(*args)
    def item_prev(*args): return _fltk.Fl_Browser_item_prev(*args)
    def item_selected(*args): return _fltk.Fl_Browser_item_selected(*args)
    def item_select(*args): return _fltk.Fl_Browser_item_select(*args)
    def item_height(*args): return _fltk.Fl_Browser_item_height(*args)
    def item_width(*args): return _fltk.Fl_Browser_item_width(*args)
    def item_draw(*args): return _fltk.Fl_Browser_item_draw(*args)
    def full_height(*args): return _fltk.Fl_Browser_full_height(*args)
    def incr_height(*args): return _fltk.Fl_Browser_incr_height(*args)
    def remove(*args): return _fltk.Fl_Browser_remove(*args)
    def move(*args): return _fltk.Fl_Browser_move(*args)
    def load(*args): return _fltk.Fl_Browser_load(*args)
    def swap(*args): return _fltk.Fl_Browser_swap(*args)
    def clear(*args): return _fltk.Fl_Browser_clear(*args)
    def size(*args): return _fltk.Fl_Browser_size(*args)
    TOP = _fltk.Fl_Browser_TOP
    BOTTOM = _fltk.Fl_Browser_BOTTOM
    MIDDLE = _fltk.Fl_Browser_MIDDLE
    def lineposition(*args): return _fltk.Fl_Browser_lineposition(*args)
    def topline(*args): return _fltk.Fl_Browser_topline(*args)
    def bottomline(*args): return _fltk.Fl_Browser_bottomline(*args)
    def middleline(*args): return _fltk.Fl_Browser_middleline(*args)
    def select(*args): return _fltk.Fl_Browser_select(*args)
    def selected(*args): return _fltk.Fl_Browser_selected(*args)
    def show(*args): return _fltk.Fl_Browser_show(*args)
    def hide(*args): return _fltk.Fl_Browser_hide(*args)
    def visible(*args): return _fltk.Fl_Browser_visible(*args)
    def value(*args): return _fltk.Fl_Browser_value(*args)
    def text(*args): return _fltk.Fl_Browser_text(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Browser:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Browser(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Browser
    def format_char(*args): return _fltk.Fl_Browser_format_char(*args)
    def column_char(*args): return _fltk.Fl_Browser_column_char(*args)
    def displayed(*args): return _fltk.Fl_Browser_displayed(*args)
    def make_visible(*args): return _fltk.Fl_Browser_make_visible(*args)
    def replace(*args): return _fltk.Fl_Browser_replace(*args)
    def display(*args): return _fltk.Fl_Browser_display(*args)
    def add(*args): return _fltk.Fl_Browser_add(*args)
    def insert(*args): return _fltk.Fl_Browser_insert(*args)
    def get_data(*args): return _fltk.Fl_Browser_get_data(*args)
    def data(*args): return _fltk.Fl_Browser_data(*args)
    def column_widths(*args): return _fltk.Fl_Browser_column_widths(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Browser(self)
        return weakref_proxy(self)
    def full_width(*args): return _fltk.Fl_Browser_full_width(*args)
    def draw(*args): return _fltk.Fl_Browser_draw(*args)
    def item_quick_height(*args): return _fltk.Fl_Browser_item_quick_height(*args)
Fl_Browser.item_first = new_instancemethod(_fltk.Fl_Browser_item_first,None,Fl_Browser)
Fl_Browser.item_next = new_instancemethod(_fltk.Fl_Browser_item_next,None,Fl_Browser)
Fl_Browser.item_prev = new_instancemethod(_fltk.Fl_Browser_item_prev,None,Fl_Browser)
Fl_Browser.item_selected = new_instancemethod(_fltk.Fl_Browser_item_selected,None,Fl_Browser)
Fl_Browser.item_select = new_instancemethod(_fltk.Fl_Browser_item_select,None,Fl_Browser)
Fl_Browser.item_height = new_instancemethod(_fltk.Fl_Browser_item_height,None,Fl_Browser)
Fl_Browser.item_width = new_instancemethod(_fltk.Fl_Browser_item_width,None,Fl_Browser)
Fl_Browser.item_draw = new_instancemethod(_fltk.Fl_Browser_item_draw,None,Fl_Browser)
Fl_Browser.full_height = new_instancemethod(_fltk.Fl_Browser_full_height,None,Fl_Browser)
Fl_Browser.incr_height = new_instancemethod(_fltk.Fl_Browser_incr_height,None,Fl_Browser)
Fl_Browser.remove = new_instancemethod(_fltk.Fl_Browser_remove,None,Fl_Browser)
Fl_Browser.move = new_instancemethod(_fltk.Fl_Browser_move,None,Fl_Browser)
Fl_Browser.load = new_instancemethod(_fltk.Fl_Browser_load,None,Fl_Browser)
Fl_Browser.swap = new_instancemethod(_fltk.Fl_Browser_swap,None,Fl_Browser)
Fl_Browser.clear = new_instancemethod(_fltk.Fl_Browser_clear,None,Fl_Browser)
Fl_Browser.size = new_instancemethod(_fltk.Fl_Browser_size,None,Fl_Browser)
Fl_Browser.lineposition = new_instancemethod(_fltk.Fl_Browser_lineposition,None,Fl_Browser)
Fl_Browser.topline = new_instancemethod(_fltk.Fl_Browser_topline,None,Fl_Browser)
Fl_Browser.bottomline = new_instancemethod(_fltk.Fl_Browser_bottomline,None,Fl_Browser)
Fl_Browser.middleline = new_instancemethod(_fltk.Fl_Browser_middleline,None,Fl_Browser)
Fl_Browser.select = new_instancemethod(_fltk.Fl_Browser_select,None,Fl_Browser)
Fl_Browser.selected = new_instancemethod(_fltk.Fl_Browser_selected,None,Fl_Browser)
Fl_Browser.show = new_instancemethod(_fltk.Fl_Browser_show,None,Fl_Browser)
Fl_Browser.hide = new_instancemethod(_fltk.Fl_Browser_hide,None,Fl_Browser)
Fl_Browser.visible = new_instancemethod(_fltk.Fl_Browser_visible,None,Fl_Browser)
Fl_Browser.value = new_instancemethod(_fltk.Fl_Browser_value,None,Fl_Browser)
Fl_Browser.text = new_instancemethod(_fltk.Fl_Browser_text,None,Fl_Browser)
Fl_Browser.format_char = new_instancemethod(_fltk.Fl_Browser_format_char,None,Fl_Browser)
Fl_Browser.column_char = new_instancemethod(_fltk.Fl_Browser_column_char,None,Fl_Browser)
Fl_Browser.displayed = new_instancemethod(_fltk.Fl_Browser_displayed,None,Fl_Browser)
Fl_Browser.make_visible = new_instancemethod(_fltk.Fl_Browser_make_visible,None,Fl_Browser)
Fl_Browser.replace = new_instancemethod(_fltk.Fl_Browser_replace,None,Fl_Browser)
Fl_Browser.display = new_instancemethod(_fltk.Fl_Browser_display,None,Fl_Browser)
Fl_Browser.add = new_instancemethod(_fltk.Fl_Browser_add,None,Fl_Browser)
Fl_Browser.insert = new_instancemethod(_fltk.Fl_Browser_insert,None,Fl_Browser)
Fl_Browser.get_data = new_instancemethod(_fltk.Fl_Browser_get_data,None,Fl_Browser)
Fl_Browser.data = new_instancemethod(_fltk.Fl_Browser_data,None,Fl_Browser)
Fl_Browser.column_widths = new_instancemethod(_fltk.Fl_Browser_column_widths,None,Fl_Browser)
Fl_Browser.full_width = new_instancemethod(_fltk.Fl_Browser_full_width,None,Fl_Browser)
Fl_Browser.draw = new_instancemethod(_fltk.Fl_Browser_draw,None,Fl_Browser)
Fl_Browser.item_quick_height = new_instancemethod(_fltk.Fl_Browser_item_quick_height,None,Fl_Browser)
_fltk.Fl_Browser_swigregister(Fl_Browser)

class Fl_File_Browser(Fl_Browser):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_File_Browser instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    FILES = _fltk.Fl_File_Browser_FILES
    DIRECTORIES = _fltk.Fl_File_Browser_DIRECTORIES
    def __init__(self, *args):
        if self.__class__ == Fl_File_Browser:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_File_Browser(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def iconsize(*args): return _fltk.Fl_File_Browser_iconsize(*args)
    def filter(*args): return _fltk.Fl_File_Browser_filter(*args)
    def textsize(*args): return _fltk.Fl_File_Browser_textsize(*args)
    def filetype(*args): return _fltk.Fl_File_Browser_filetype(*args)
    def load(*args): return _fltk.Fl_File_Browser_load(*args)
    __swig_destroy__ = _fltk.delete_Fl_File_Browser
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_File_Browser(self)
        return weakref_proxy(self)
    def item_first(*args): return _fltk.Fl_File_Browser_item_first(*args)
    def item_next(*args): return _fltk.Fl_File_Browser_item_next(*args)
    def item_prev(*args): return _fltk.Fl_File_Browser_item_prev(*args)
    def full_width(*args): return _fltk.Fl_File_Browser_full_width(*args)
    def item_select(*args): return _fltk.Fl_File_Browser_item_select(*args)
    def item_draw(*args): return _fltk.Fl_File_Browser_item_draw(*args)
    def full_height(*args): return _fltk.Fl_File_Browser_full_height(*args)
    def incr_height(*args): return _fltk.Fl_File_Browser_incr_height(*args)
    def draw(*args): return _fltk.Fl_File_Browser_draw(*args)
    def item_quick_height(*args): return _fltk.Fl_File_Browser_item_quick_height(*args)
    def item_selected(*args): return _fltk.Fl_File_Browser_item_selected(*args)
    def item_height(*args): return _fltk.Fl_File_Browser_item_height(*args)
    def item_width(*args): return _fltk.Fl_File_Browser_item_width(*args)
Fl_File_Browser.iconsize = new_instancemethod(_fltk.Fl_File_Browser_iconsize,None,Fl_File_Browser)
Fl_File_Browser.filter = new_instancemethod(_fltk.Fl_File_Browser_filter,None,Fl_File_Browser)
Fl_File_Browser.textsize = new_instancemethod(_fltk.Fl_File_Browser_textsize,None,Fl_File_Browser)
Fl_File_Browser.filetype = new_instancemethod(_fltk.Fl_File_Browser_filetype,None,Fl_File_Browser)
Fl_File_Browser.load = new_instancemethod(_fltk.Fl_File_Browser_load,None,Fl_File_Browser)
Fl_File_Browser.item_first = new_instancemethod(_fltk.Fl_File_Browser_item_first,None,Fl_File_Browser)
Fl_File_Browser.item_next = new_instancemethod(_fltk.Fl_File_Browser_item_next,None,Fl_File_Browser)
Fl_File_Browser.item_prev = new_instancemethod(_fltk.Fl_File_Browser_item_prev,None,Fl_File_Browser)
Fl_File_Browser.full_width = new_instancemethod(_fltk.Fl_File_Browser_full_width,None,Fl_File_Browser)
Fl_File_Browser.item_select = new_instancemethod(_fltk.Fl_File_Browser_item_select,None,Fl_File_Browser)
Fl_File_Browser.item_draw = new_instancemethod(_fltk.Fl_File_Browser_item_draw,None,Fl_File_Browser)
Fl_File_Browser.full_height = new_instancemethod(_fltk.Fl_File_Browser_full_height,None,Fl_File_Browser)
Fl_File_Browser.incr_height = new_instancemethod(_fltk.Fl_File_Browser_incr_height,None,Fl_File_Browser)
Fl_File_Browser.draw = new_instancemethod(_fltk.Fl_File_Browser_draw,None,Fl_File_Browser)
Fl_File_Browser.item_quick_height = new_instancemethod(_fltk.Fl_File_Browser_item_quick_height,None,Fl_File_Browser)
Fl_File_Browser.item_selected = new_instancemethod(_fltk.Fl_File_Browser_item_selected,None,Fl_File_Browser)
Fl_File_Browser.item_height = new_instancemethod(_fltk.Fl_File_Browser_item_height,None,Fl_File_Browser)
Fl_File_Browser.item_width = new_instancemethod(_fltk.Fl_File_Browser_item_width,None,Fl_File_Browser)
_fltk.Fl_File_Browser_swigregister(Fl_File_Browser)

FL_ALPHASORT = _fltk.FL_ALPHASORT
FL_CASEALPHASORT = _fltk.FL_CASEALPHASORT
FL_CASENUMERICSORT = _fltk.FL_CASENUMERICSORT
FL_NUMERICSORT = _fltk.FL_NUMERICSORT
class Fl_File_Icon(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_File_Icon instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    ANY = _fltk.Fl_File_Icon_ANY
    PLAIN = _fltk.Fl_File_Icon_PLAIN
    FIFO = _fltk.Fl_File_Icon_FIFO
    DEVICE = _fltk.Fl_File_Icon_DEVICE
    LINK = _fltk.Fl_File_Icon_LINK
    DIRECTORY = _fltk.Fl_File_Icon_DIRECTORY
    END = _fltk.Fl_File_Icon_END
    COLOR = _fltk.Fl_File_Icon_COLOR
    LINE = _fltk.Fl_File_Icon_LINE
    CLOSEDLINE = _fltk.Fl_File_Icon_CLOSEDLINE
    POLYGON = _fltk.Fl_File_Icon_POLYGON
    OUTLINEPOLYGON = _fltk.Fl_File_Icon_OUTLINEPOLYGON
    VERTEX = _fltk.Fl_File_Icon_VERTEX
    def __init__(self, *args):
        this = _fltk.new_Fl_File_Icon(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_File_Icon
    def add(*args): return _fltk.Fl_File_Icon_add(*args)
    def add_color(*args): return _fltk.Fl_File_Icon_add_color(*args)
    def add_vertex(*args): return _fltk.Fl_File_Icon_add_vertex(*args)
    def clear(*args): return _fltk.Fl_File_Icon_clear(*args)
    def draw(*args): return _fltk.Fl_File_Icon_draw(*args)
    def label(*args): return _fltk.Fl_File_Icon_label(*args)
    labeltype = staticmethod(_fltk.Fl_File_Icon_labeltype)
    def load(*args): return _fltk.Fl_File_Icon_load(*args)
    def load_fti(*args): return _fltk.Fl_File_Icon_load_fti(*args)
    def load_image(*args): return _fltk.Fl_File_Icon_load_image(*args)
    def next(*args): return _fltk.Fl_File_Icon_next(*args)
    def pattern(*args): return _fltk.Fl_File_Icon_pattern(*args)
    def size(*args): return _fltk.Fl_File_Icon_size(*args)
    def type(*args): return _fltk.Fl_File_Icon_type(*args)
    def value(*args): return _fltk.Fl_File_Icon_value(*args)
    find = staticmethod(_fltk.Fl_File_Icon_find)
    first = staticmethod(_fltk.Fl_File_Icon_first)
    load_system_icons = staticmethod(_fltk.Fl_File_Icon_load_system_icons)
Fl_File_Icon.add = new_instancemethod(_fltk.Fl_File_Icon_add,None,Fl_File_Icon)
Fl_File_Icon.add_color = new_instancemethod(_fltk.Fl_File_Icon_add_color,None,Fl_File_Icon)
Fl_File_Icon.add_vertex = new_instancemethod(_fltk.Fl_File_Icon_add_vertex,None,Fl_File_Icon)
Fl_File_Icon.clear = new_instancemethod(_fltk.Fl_File_Icon_clear,None,Fl_File_Icon)
Fl_File_Icon.draw = new_instancemethod(_fltk.Fl_File_Icon_draw,None,Fl_File_Icon)
Fl_File_Icon.label = new_instancemethod(_fltk.Fl_File_Icon_label,None,Fl_File_Icon)
Fl_File_Icon.load = new_instancemethod(_fltk.Fl_File_Icon_load,None,Fl_File_Icon)
Fl_File_Icon.load_fti = new_instancemethod(_fltk.Fl_File_Icon_load_fti,None,Fl_File_Icon)
Fl_File_Icon.load_image = new_instancemethod(_fltk.Fl_File_Icon_load_image,None,Fl_File_Icon)
Fl_File_Icon.next = new_instancemethod(_fltk.Fl_File_Icon_next,None,Fl_File_Icon)
Fl_File_Icon.pattern = new_instancemethod(_fltk.Fl_File_Icon_pattern,None,Fl_File_Icon)
Fl_File_Icon.size = new_instancemethod(_fltk.Fl_File_Icon_size,None,Fl_File_Icon)
Fl_File_Icon.type = new_instancemethod(_fltk.Fl_File_Icon_type,None,Fl_File_Icon)
Fl_File_Icon.value = new_instancemethod(_fltk.Fl_File_Icon_value,None,Fl_File_Icon)
_fltk.Fl_File_Icon_swigregister(Fl_File_Icon)

Fl_File_Icon_labeltype = _fltk.Fl_File_Icon_labeltype

Fl_File_Icon_find = _fltk.Fl_File_Icon_find

Fl_File_Icon_first = _fltk.Fl_File_Icon_first

Fl_File_Icon_load_system_icons = _fltk.Fl_File_Icon_load_system_icons

class Fl_File_Chooser(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_File_Chooser instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    SINGLE = _fltk.Fl_File_Chooser_SINGLE
    MULTI = _fltk.Fl_File_Chooser_MULTI
    CREATE = _fltk.Fl_File_Chooser_CREATE
    DIRECTORY = _fltk.Fl_File_Chooser_DIRECTORY
    def __init__(self, *args):
        this = _fltk.new_Fl_File_Chooser(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    newButton = property(_fltk.Fl_File_Chooser_newButton_get, _fltk.Fl_File_Chooser_newButton_set)
    previewButton = property(_fltk.Fl_File_Chooser_previewButton_get, _fltk.Fl_File_Chooser_previewButton_set)
    __swig_destroy__ = _fltk.delete_Fl_File_Chooser
    def color(*args): return _fltk.Fl_File_Chooser_color(*args)
    def count(*args): return _fltk.Fl_File_Chooser_count(*args)
    def directory(*args): return _fltk.Fl_File_Chooser_directory(*args)
    def filter(*args): return _fltk.Fl_File_Chooser_filter(*args)
    def filter_value(*args): return _fltk.Fl_File_Chooser_filter_value(*args)
    def hide(*args): return _fltk.Fl_File_Chooser_hide(*args)
    def iconsize(*args): return _fltk.Fl_File_Chooser_iconsize(*args)
    def label(*args): return _fltk.Fl_File_Chooser_label(*args)
    def ok_label(*args): return _fltk.Fl_File_Chooser_ok_label(*args)
    def preview(*args): return _fltk.Fl_File_Chooser_preview(*args)
    def rescan(*args): return _fltk.Fl_File_Chooser_rescan(*args)
    def show(*args): return _fltk.Fl_File_Chooser_show(*args)
    def shown(*args): return _fltk.Fl_File_Chooser_shown(*args)
    def textcolor(*args): return _fltk.Fl_File_Chooser_textcolor(*args)
    def textfont(*args): return _fltk.Fl_File_Chooser_textfont(*args)
    def textsize(*args): return _fltk.Fl_File_Chooser_textsize(*args)
    def type(*args): return _fltk.Fl_File_Chooser_type(*args)
    def user_data(*args): return _fltk.Fl_File_Chooser_user_data(*args)
    def value(*args): return _fltk.Fl_File_Chooser_value(*args)
    def visible(*args): return _fltk.Fl_File_Chooser_visible(*args)
    add_favorites_label = property(_fltk.Fl_File_Chooser_add_favorites_label_get, _fltk.Fl_File_Chooser_add_favorites_label_set)
    all_files_label = property(_fltk.Fl_File_Chooser_all_files_label_get, _fltk.Fl_File_Chooser_all_files_label_set)
    custom_filter_label = property(_fltk.Fl_File_Chooser_custom_filter_label_get, _fltk.Fl_File_Chooser_custom_filter_label_set)
    existing_file_label = property(_fltk.Fl_File_Chooser_existing_file_label_get, _fltk.Fl_File_Chooser_existing_file_label_set)
    favorites_label = property(_fltk.Fl_File_Chooser_favorites_label_get, _fltk.Fl_File_Chooser_favorites_label_set)
    filename_label = property(_fltk.Fl_File_Chooser_filename_label_get, _fltk.Fl_File_Chooser_filename_label_set)
    filesystems_label = property(_fltk.Fl_File_Chooser_filesystems_label_get, _fltk.Fl_File_Chooser_filesystems_label_set)
    manage_favorites_label = property(_fltk.Fl_File_Chooser_manage_favorites_label_get, _fltk.Fl_File_Chooser_manage_favorites_label_set)
    new_directory_label = property(_fltk.Fl_File_Chooser_new_directory_label_get, _fltk.Fl_File_Chooser_new_directory_label_set)
    new_directory_tooltip = property(_fltk.Fl_File_Chooser_new_directory_tooltip_get, _fltk.Fl_File_Chooser_new_directory_tooltip_set)
    preview_label = property(_fltk.Fl_File_Chooser_preview_label_get, _fltk.Fl_File_Chooser_preview_label_set)
    save_label = property(_fltk.Fl_File_Chooser_save_label_get, _fltk.Fl_File_Chooser_save_label_set)
    show_label = property(_fltk.Fl_File_Chooser_show_label_get, _fltk.Fl_File_Chooser_show_label_set)
    def callback(*args): return _fltk.Fl_File_Chooser_callback(*args)
Fl_File_Chooser.color = new_instancemethod(_fltk.Fl_File_Chooser_color,None,Fl_File_Chooser)
Fl_File_Chooser.count = new_instancemethod(_fltk.Fl_File_Chooser_count,None,Fl_File_Chooser)
Fl_File_Chooser.directory = new_instancemethod(_fltk.Fl_File_Chooser_directory,None,Fl_File_Chooser)
Fl_File_Chooser.filter = new_instancemethod(_fltk.Fl_File_Chooser_filter,None,Fl_File_Chooser)
Fl_File_Chooser.filter_value = new_instancemethod(_fltk.Fl_File_Chooser_filter_value,None,Fl_File_Chooser)
Fl_File_Chooser.hide = new_instancemethod(_fltk.Fl_File_Chooser_hide,None,Fl_File_Chooser)
Fl_File_Chooser.iconsize = new_instancemethod(_fltk.Fl_File_Chooser_iconsize,None,Fl_File_Chooser)
Fl_File_Chooser.label = new_instancemethod(_fltk.Fl_File_Chooser_label,None,Fl_File_Chooser)
Fl_File_Chooser.ok_label = new_instancemethod(_fltk.Fl_File_Chooser_ok_label,None,Fl_File_Chooser)
Fl_File_Chooser.preview = new_instancemethod(_fltk.Fl_File_Chooser_preview,None,Fl_File_Chooser)
Fl_File_Chooser.rescan = new_instancemethod(_fltk.Fl_File_Chooser_rescan,None,Fl_File_Chooser)
Fl_File_Chooser.show = new_instancemethod(_fltk.Fl_File_Chooser_show,None,Fl_File_Chooser)
Fl_File_Chooser.shown = new_instancemethod(_fltk.Fl_File_Chooser_shown,None,Fl_File_Chooser)
Fl_File_Chooser.textcolor = new_instancemethod(_fltk.Fl_File_Chooser_textcolor,None,Fl_File_Chooser)
Fl_File_Chooser.textfont = new_instancemethod(_fltk.Fl_File_Chooser_textfont,None,Fl_File_Chooser)
Fl_File_Chooser.textsize = new_instancemethod(_fltk.Fl_File_Chooser_textsize,None,Fl_File_Chooser)
Fl_File_Chooser.type = new_instancemethod(_fltk.Fl_File_Chooser_type,None,Fl_File_Chooser)
Fl_File_Chooser.user_data = new_instancemethod(_fltk.Fl_File_Chooser_user_data,None,Fl_File_Chooser)
Fl_File_Chooser.value = new_instancemethod(_fltk.Fl_File_Chooser_value,None,Fl_File_Chooser)
Fl_File_Chooser.visible = new_instancemethod(_fltk.Fl_File_Chooser_visible,None,Fl_File_Chooser)
Fl_File_Chooser.callback = new_instancemethod(_fltk.Fl_File_Chooser_callback,None,Fl_File_Chooser)
_fltk.Fl_File_Chooser_swigregister(Fl_File_Chooser)
cvar = _fltk.cvar


fl_dir_chooser = _fltk.fl_dir_chooser

fl_file_chooser = _fltk.fl_file_chooser

fl_file_chooser_callback = _fltk.fl_file_chooser_callback

fl_file_chooser_ok_label = _fltk.fl_file_chooser_ok_label
class Fl(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    e_number = property(_fltk.Fl_e_number_get, _fltk.Fl_e_number_set)
    e_x = property(_fltk.Fl_e_x_get, _fltk.Fl_e_x_set)
    e_y = property(_fltk.Fl_e_y_get, _fltk.Fl_e_y_set)
    e_x_root = property(_fltk.Fl_e_x_root_get, _fltk.Fl_e_x_root_set)
    e_y_root = property(_fltk.Fl_e_y_root_get, _fltk.Fl_e_y_root_set)
    e_dx = property(_fltk.Fl_e_dx_get, _fltk.Fl_e_dx_set)
    e_dy = property(_fltk.Fl_e_dy_get, _fltk.Fl_e_dy_set)
    e_state = property(_fltk.Fl_e_state_get, _fltk.Fl_e_state_set)
    e_clicks = property(_fltk.Fl_e_clicks_get, _fltk.Fl_e_clicks_set)
    e_is_click = property(_fltk.Fl_e_is_click_get, _fltk.Fl_e_is_click_set)
    e_keysym = property(_fltk.Fl_e_keysym_get, _fltk.Fl_e_keysym_set)
    e_text = property(_fltk.Fl_e_text_get, _fltk.Fl_e_text_set)
    e_length = property(_fltk.Fl_e_length_get, _fltk.Fl_e_length_set)
    belowmouse_ = property(_fltk.Fl_belowmouse__get, _fltk.Fl_belowmouse__set)
    pushed_ = property(_fltk.Fl_pushed__get, _fltk.Fl_pushed__set)
    focus_ = property(_fltk.Fl_focus__get, _fltk.Fl_focus__set)
    damage_ = property(_fltk.Fl_damage__get, _fltk.Fl_damage__set)
    selection_owner_ = property(_fltk.Fl_selection_owner__get, _fltk.Fl_selection_owner__set)
    modal_ = property(_fltk.Fl_modal__get, _fltk.Fl_modal__set)
    grab_ = property(_fltk.Fl_grab__get, _fltk.Fl_grab__set)
    compose_state = property(_fltk.Fl_compose_state_get, _fltk.Fl_compose_state_set)
    visible_focus_ = property(_fltk.Fl_visible_focus__get, _fltk.Fl_visible_focus__set)
    dnd_text_ops_ = property(_fltk.Fl_dnd_text_ops__get, _fltk.Fl_dnd_text_ops__set)
    idle = property(_fltk.Fl_idle_get, _fltk.Fl_idle_set)
    scheme_ = property(_fltk.Fl_scheme__get, _fltk.Fl_scheme__set)
    scheme_bg_ = property(_fltk.Fl_scheme_bg__get, _fltk.Fl_scheme_bg__set)
    version = staticmethod(_fltk.Fl_version)
    arg = staticmethod(_fltk.Fl_arg)
    args = staticmethod(_fltk.Fl_args)
    display = staticmethod(_fltk.Fl_display)
    visual = staticmethod(_fltk.Fl_visual)
    gl_visual = staticmethod(_fltk.Fl_gl_visual)
    own_colormap = staticmethod(_fltk.Fl_own_colormap)
    get_system_colors = staticmethod(_fltk.Fl_get_system_colors)
    foreground = staticmethod(_fltk.Fl_foreground)
    background = staticmethod(_fltk.Fl_background)
    background2 = staticmethod(_fltk.Fl_background2)
    scheme = staticmethod(_fltk.Fl_scheme)
    reload_scheme = staticmethod(_fltk.Fl_reload_scheme)
    wait = staticmethod(_fltk.Fl_wait)
    check = staticmethod(_fltk.Fl_check)
    ready = staticmethod(_fltk.Fl_ready)
    run = staticmethod(_fltk.Fl_run)
    readqueue = staticmethod(_fltk.Fl_readqueue)
    repeat_timeout = staticmethod(_fltk.Fl_repeat_timeout)
    has_timeout = staticmethod(_fltk.Fl_has_timeout)
    remove_timeout = staticmethod(_fltk.Fl_remove_timeout)
    add_fd = staticmethod(_fltk.Fl_add_fd)
    remove_fd = staticmethod(_fltk.Fl_remove_fd)
    has_idle = staticmethod(_fltk.Fl_has_idle)
    damage = staticmethod(_fltk.Fl_damage)
    redraw = staticmethod(_fltk.Fl_redraw)
    flush = staticmethod(_fltk.Fl_flush)
    warning = property(_fltk.Fl_warning_get, _fltk.Fl_warning_set)
    error = property(_fltk.Fl_error_get, _fltk.Fl_error_set)
    fatal = property(_fltk.Fl_fatal_get, _fltk.Fl_fatal_set)
    first_window = staticmethod(_fltk.Fl_first_window)
    next_window = staticmethod(_fltk.Fl_next_window)
    modal = staticmethod(_fltk.Fl_modal)
    grab = staticmethod(_fltk.Fl_grab)
    event = staticmethod(_fltk.Fl_event)
    event_x = staticmethod(_fltk.Fl_event_x)
    event_y = staticmethod(_fltk.Fl_event_y)
    event_x_root = staticmethod(_fltk.Fl_event_x_root)
    event_y_root = staticmethod(_fltk.Fl_event_y_root)
    event_dx = staticmethod(_fltk.Fl_event_dx)
    event_dy = staticmethod(_fltk.Fl_event_dy)
    get_mouse = staticmethod(_fltk.Fl_get_mouse)
    event_clicks = staticmethod(_fltk.Fl_event_clicks)
    event_is_click = staticmethod(_fltk.Fl_event_is_click)
    event_button = staticmethod(_fltk.Fl_event_button)
    event_state = staticmethod(_fltk.Fl_event_state)
    event_key = staticmethod(_fltk.Fl_event_key)
    get_key = staticmethod(_fltk.Fl_get_key)
    event_text = staticmethod(_fltk.Fl_event_text)
    event_length = staticmethod(_fltk.Fl_event_length)
    compose = staticmethod(_fltk.Fl_compose)
    compose_reset = staticmethod(_fltk.Fl_compose_reset)
    event_inside = staticmethod(_fltk.Fl_event_inside)
    test_shortcut = staticmethod(_fltk.Fl_test_shortcut)
    handle = staticmethod(_fltk.Fl_handle)
    belowmouse = staticmethod(_fltk.Fl_belowmouse)
    pushed = staticmethod(_fltk.Fl_pushed)
    focus = staticmethod(_fltk.Fl_focus)
    copy = staticmethod(_fltk.Fl_copy)
    dnd = staticmethod(_fltk.Fl_dnd)
    selection_owner = staticmethod(_fltk.Fl_selection_owner)
    selection = staticmethod(_fltk.Fl_selection)
    paste = staticmethod(_fltk.Fl_paste)
    x = staticmethod(_fltk.Fl_x)
    y = staticmethod(_fltk.Fl_y)
    w = staticmethod(_fltk.Fl_w)
    h = staticmethod(_fltk.Fl_h)
    screen_count = staticmethod(_fltk.Fl_screen_count)
    screen_xywh = staticmethod(_fltk.Fl_screen_xywh)
    set_color = staticmethod(_fltk.Fl_set_color)
    get_color = staticmethod(_fltk.Fl_get_color)
    free_color = staticmethod(_fltk.Fl_free_color)
    get_font = staticmethod(_fltk.Fl_get_font)
    get_font_name = staticmethod(_fltk.Fl_get_font_name)
    get_font_sizes = staticmethod(_fltk.Fl_get_font_sizes)
    set_font = staticmethod(_fltk.Fl_set_font)
    set_fonts = staticmethod(_fltk.Fl_set_fonts)
    set_labeltype = staticmethod(_fltk.Fl_set_labeltype)
    get_boxtype = staticmethod(_fltk.Fl_get_boxtype)
    set_boxtype = staticmethod(_fltk.Fl_set_boxtype)
    box_dx = staticmethod(_fltk.Fl_box_dx)
    box_dy = staticmethod(_fltk.Fl_box_dy)
    box_dw = staticmethod(_fltk.Fl_box_dw)
    box_dh = staticmethod(_fltk.Fl_box_dh)
    draw_box_active = staticmethod(_fltk.Fl_draw_box_active)
    set_abort = staticmethod(_fltk.Fl_set_abort)
    atclose = property(_fltk.Fl_atclose_get, _fltk.Fl_atclose_set)
    default_atclose = staticmethod(_fltk.Fl_default_atclose)
    set_atclose = staticmethod(_fltk.Fl_set_atclose)
    event_shift = staticmethod(_fltk.Fl_event_shift)
    event_ctrl = staticmethod(_fltk.Fl_event_ctrl)
    event_alt = staticmethod(_fltk.Fl_event_alt)
    event_buttons = staticmethod(_fltk.Fl_event_buttons)
    event_button1 = staticmethod(_fltk.Fl_event_button1)
    event_button2 = staticmethod(_fltk.Fl_event_button2)
    event_button3 = staticmethod(_fltk.Fl_event_button3)
    release = staticmethod(_fltk.Fl_release)
    visible_focus = staticmethod(_fltk.Fl_visible_focus)
    dnd_text_ops = staticmethod(_fltk.Fl_dnd_text_ops)
    delete_widget = staticmethod(_fltk.Fl_delete_widget)
    do_widget_deletion = staticmethod(_fltk.Fl_do_widget_deletion)
    lock = staticmethod(_fltk.Fl_lock)
    unlock = staticmethod(_fltk.Fl_unlock)
    awake = staticmethod(_fltk.Fl_awake)
    thread_message = staticmethod(_fltk.Fl_thread_message)
    __swig_destroy__ = _fltk.delete_Fl
_fltk.Fl_swigregister(Fl)

Fl_version = _fltk.Fl_version

Fl_arg = _fltk.Fl_arg
Fl.help = _fltk.cvar.Fl_help

Fl_args = _fltk.Fl_args

Fl_display = _fltk.Fl_display

Fl_visual = _fltk.Fl_visual

Fl_gl_visual = _fltk.Fl_gl_visual

Fl_own_colormap = _fltk.Fl_own_colormap

Fl_get_system_colors = _fltk.Fl_get_system_colors

Fl_foreground = _fltk.Fl_foreground

Fl_background = _fltk.Fl_background

Fl_background2 = _fltk.Fl_background2

Fl_scheme = _fltk.Fl_scheme

Fl_reload_scheme = _fltk.Fl_reload_scheme

Fl_wait = _fltk.Fl_wait

Fl_check = _fltk.Fl_check

Fl_ready = _fltk.Fl_ready

Fl_run = _fltk.Fl_run

Fl_readqueue = _fltk.Fl_readqueue

Fl_repeat_timeout = _fltk.Fl_repeat_timeout

Fl_has_timeout = _fltk.Fl_has_timeout

Fl_remove_timeout = _fltk.Fl_remove_timeout

Fl_add_fd = _fltk.Fl_add_fd

Fl_remove_fd = _fltk.Fl_remove_fd

Fl_has_idle = _fltk.Fl_has_idle

Fl_damage = _fltk.Fl_damage

Fl_redraw = _fltk.Fl_redraw

Fl_flush = _fltk.Fl_flush

Fl_first_window = _fltk.Fl_first_window

Fl_next_window = _fltk.Fl_next_window

Fl_modal = _fltk.Fl_modal

Fl_grab = _fltk.Fl_grab

Fl_event = _fltk.Fl_event

Fl_event_x = _fltk.Fl_event_x

Fl_event_y = _fltk.Fl_event_y

Fl_event_x_root = _fltk.Fl_event_x_root

Fl_event_y_root = _fltk.Fl_event_y_root

Fl_event_dx = _fltk.Fl_event_dx

Fl_event_dy = _fltk.Fl_event_dy

Fl_get_mouse = _fltk.Fl_get_mouse

Fl_event_clicks = _fltk.Fl_event_clicks

Fl_event_is_click = _fltk.Fl_event_is_click

Fl_event_button = _fltk.Fl_event_button

Fl_event_state = _fltk.Fl_event_state

Fl_event_key = _fltk.Fl_event_key

Fl_get_key = _fltk.Fl_get_key

Fl_event_text = _fltk.Fl_event_text

Fl_event_length = _fltk.Fl_event_length

Fl_compose = _fltk.Fl_compose

Fl_compose_reset = _fltk.Fl_compose_reset

Fl_event_inside = _fltk.Fl_event_inside

Fl_test_shortcut = _fltk.Fl_test_shortcut

Fl_handle = _fltk.Fl_handle

Fl_belowmouse = _fltk.Fl_belowmouse

Fl_pushed = _fltk.Fl_pushed

Fl_focus = _fltk.Fl_focus

Fl_copy = _fltk.Fl_copy

Fl_dnd = _fltk.Fl_dnd

Fl_selection_owner = _fltk.Fl_selection_owner

Fl_selection = _fltk.Fl_selection

Fl_paste = _fltk.Fl_paste

Fl_x = _fltk.Fl_x

Fl_y = _fltk.Fl_y

Fl_w = _fltk.Fl_w

Fl_h = _fltk.Fl_h

Fl_screen_count = _fltk.Fl_screen_count

Fl_screen_xywh = _fltk.Fl_screen_xywh

Fl_set_color = _fltk.Fl_set_color

Fl_get_color = _fltk.Fl_get_color

Fl_free_color = _fltk.Fl_free_color

Fl_get_font = _fltk.Fl_get_font

Fl_get_font_name = _fltk.Fl_get_font_name

Fl_get_font_sizes = _fltk.Fl_get_font_sizes

Fl_set_font = _fltk.Fl_set_font

Fl_set_fonts = _fltk.Fl_set_fonts

Fl_set_labeltype = _fltk.Fl_set_labeltype

Fl_get_boxtype = _fltk.Fl_get_boxtype

Fl_set_boxtype = _fltk.Fl_set_boxtype

Fl_box_dx = _fltk.Fl_box_dx

Fl_box_dy = _fltk.Fl_box_dy

Fl_box_dw = _fltk.Fl_box_dw

Fl_box_dh = _fltk.Fl_box_dh

Fl_draw_box_active = _fltk.Fl_draw_box_active

Fl_set_abort = _fltk.Fl_set_abort

Fl_default_atclose = _fltk.Fl_default_atclose

Fl_set_atclose = _fltk.Fl_set_atclose

Fl_event_shift = _fltk.Fl_event_shift

Fl_event_ctrl = _fltk.Fl_event_ctrl

Fl_event_alt = _fltk.Fl_event_alt

Fl_event_buttons = _fltk.Fl_event_buttons

Fl_event_button1 = _fltk.Fl_event_button1

Fl_event_button2 = _fltk.Fl_event_button2

Fl_event_button3 = _fltk.Fl_event_button3

Fl_release = _fltk.Fl_release

Fl_visible_focus = _fltk.Fl_visible_focus

Fl_dnd_text_ops = _fltk.Fl_dnd_text_ops

Fl_delete_widget = _fltk.Fl_delete_widget

Fl_do_widget_deletion = _fltk.Fl_do_widget_deletion

Fl_lock = _fltk.Fl_lock

Fl_unlock = _fltk.Fl_unlock

Fl_awake = _fltk.Fl_awake

Fl_thread_message = _fltk.Fl_thread_message


pyFLTK_controlIdleCallbacks = _fltk.pyFLTK_controlIdleCallbacks
FL_MAJOR_VERSION = _fltk.FL_MAJOR_VERSION
FL_MINOR_VERSION = _fltk.FL_MINOR_VERSION
FL_PATCH_VERSION = _fltk.FL_PATCH_VERSION
FL_NO_EVENT = _fltk.FL_NO_EVENT
FL_PUSH = _fltk.FL_PUSH
FL_RELEASE = _fltk.FL_RELEASE
FL_ENTER = _fltk.FL_ENTER
FL_LEAVE = _fltk.FL_LEAVE
FL_DRAG = _fltk.FL_DRAG
FL_FOCUS = _fltk.FL_FOCUS
FL_UNFOCUS = _fltk.FL_UNFOCUS
FL_KEYDOWN = _fltk.FL_KEYDOWN
FL_KEYUP = _fltk.FL_KEYUP
FL_CLOSE = _fltk.FL_CLOSE
FL_MOVE = _fltk.FL_MOVE
FL_SHORTCUT = _fltk.FL_SHORTCUT
FL_DEACTIVATE = _fltk.FL_DEACTIVATE
FL_ACTIVATE = _fltk.FL_ACTIVATE
FL_HIDE = _fltk.FL_HIDE
FL_SHOW = _fltk.FL_SHOW
FL_PASTE = _fltk.FL_PASTE
FL_SELECTIONCLEAR = _fltk.FL_SELECTIONCLEAR
FL_MOUSEWHEEL = _fltk.FL_MOUSEWHEEL
FL_DND_ENTER = _fltk.FL_DND_ENTER
FL_DND_DRAG = _fltk.FL_DND_DRAG
FL_DND_LEAVE = _fltk.FL_DND_LEAVE
FL_DND_RELEASE = _fltk.FL_DND_RELEASE
FL_WHEN_NEVER = _fltk.FL_WHEN_NEVER
FL_WHEN_CHANGED = _fltk.FL_WHEN_CHANGED
FL_WHEN_RELEASE = _fltk.FL_WHEN_RELEASE
FL_WHEN_RELEASE_ALWAYS = _fltk.FL_WHEN_RELEASE_ALWAYS
FL_WHEN_ENTER_KEY = _fltk.FL_WHEN_ENTER_KEY
FL_WHEN_ENTER_KEY_ALWAYS = _fltk.FL_WHEN_ENTER_KEY_ALWAYS
FL_WHEN_ENTER_KEY_CHANGED = _fltk.FL_WHEN_ENTER_KEY_CHANGED
FL_WHEN_NOT_CHANGED = _fltk.FL_WHEN_NOT_CHANGED
FL_Button = _fltk.FL_Button
FL_BackSpace = _fltk.FL_BackSpace
FL_Tab = _fltk.FL_Tab
FL_Enter = _fltk.FL_Enter
FL_Pause = _fltk.FL_Pause
FL_Scroll_Lock = _fltk.FL_Scroll_Lock
FL_Escape = _fltk.FL_Escape
FL_Home = _fltk.FL_Home
FL_Left = _fltk.FL_Left
FL_Up = _fltk.FL_Up
FL_Right = _fltk.FL_Right
FL_Down = _fltk.FL_Down
FL_Page_Up = _fltk.FL_Page_Up
FL_Page_Down = _fltk.FL_Page_Down
FL_End = _fltk.FL_End
FL_Print = _fltk.FL_Print
FL_Insert = _fltk.FL_Insert
FL_Menu = _fltk.FL_Menu
FL_Help = _fltk.FL_Help
FL_Num_Lock = _fltk.FL_Num_Lock
FL_KP = _fltk.FL_KP
FL_KP_Enter = _fltk.FL_KP_Enter
FL_KP_Last = _fltk.FL_KP_Last
FL_F = _fltk.FL_F
FL_F_Last = _fltk.FL_F_Last
FL_Shift_L = _fltk.FL_Shift_L
FL_Shift_R = _fltk.FL_Shift_R
FL_Control_L = _fltk.FL_Control_L
FL_Control_R = _fltk.FL_Control_R
FL_Caps_Lock = _fltk.FL_Caps_Lock
FL_Meta_L = _fltk.FL_Meta_L
FL_Meta_R = _fltk.FL_Meta_R
FL_Alt_L = _fltk.FL_Alt_L
FL_Alt_R = _fltk.FL_Alt_R
FL_Delete = _fltk.FL_Delete
FL_LEFT_MOUSE = _fltk.FL_LEFT_MOUSE
FL_MIDDLE_MOUSE = _fltk.FL_MIDDLE_MOUSE
FL_RIGHT_MOUSE = _fltk.FL_RIGHT_MOUSE
FL_SHIFT = _fltk.FL_SHIFT
FL_CAPS_LOCK = _fltk.FL_CAPS_LOCK
FL_CTRL = _fltk.FL_CTRL
FL_ALT = _fltk.FL_ALT
FL_NUM_LOCK = _fltk.FL_NUM_LOCK
FL_META = _fltk.FL_META
FL_SCROLL_LOCK = _fltk.FL_SCROLL_LOCK
FL_BUTTON1 = _fltk.FL_BUTTON1
FL_BUTTON2 = _fltk.FL_BUTTON2
FL_BUTTON3 = _fltk.FL_BUTTON3
FL_BUTTONS = _fltk.FL_BUTTONS
FL_COMMAND = _fltk.FL_COMMAND
FL_NO_BOX = _fltk.FL_NO_BOX
FL_FLAT_BOX = _fltk.FL_FLAT_BOX
FL_UP_BOX = _fltk.FL_UP_BOX
FL_DOWN_BOX = _fltk.FL_DOWN_BOX
FL_UP_FRAME = _fltk.FL_UP_FRAME
FL_DOWN_FRAME = _fltk.FL_DOWN_FRAME
FL_THIN_UP_BOX = _fltk.FL_THIN_UP_BOX
FL_THIN_DOWN_BOX = _fltk.FL_THIN_DOWN_BOX
FL_THIN_UP_FRAME = _fltk.FL_THIN_UP_FRAME
FL_THIN_DOWN_FRAME = _fltk.FL_THIN_DOWN_FRAME
FL_ENGRAVED_BOX = _fltk.FL_ENGRAVED_BOX
FL_EMBOSSED_BOX = _fltk.FL_EMBOSSED_BOX
FL_ENGRAVED_FRAME = _fltk.FL_ENGRAVED_FRAME
FL_EMBOSSED_FRAME = _fltk.FL_EMBOSSED_FRAME
FL_BORDER_BOX = _fltk.FL_BORDER_BOX
_FL_SHADOW_BOX = _fltk._FL_SHADOW_BOX
FL_BORDER_FRAME = _fltk.FL_BORDER_FRAME
_FL_SHADOW_FRAME = _fltk._FL_SHADOW_FRAME
_FL_ROUNDED_BOX = _fltk._FL_ROUNDED_BOX
_FL_RSHADOW_BOX = _fltk._FL_RSHADOW_BOX
_FL_ROUNDED_FRAME = _fltk._FL_ROUNDED_FRAME
_FL_RFLAT_BOX = _fltk._FL_RFLAT_BOX
_FL_ROUND_UP_BOX = _fltk._FL_ROUND_UP_BOX
_FL_ROUND_DOWN_BOX = _fltk._FL_ROUND_DOWN_BOX
_FL_DIAMOND_UP_BOX = _fltk._FL_DIAMOND_UP_BOX
_FL_DIAMOND_DOWN_BOX = _fltk._FL_DIAMOND_DOWN_BOX
_FL_OVAL_BOX = _fltk._FL_OVAL_BOX
_FL_OSHADOW_BOX = _fltk._FL_OSHADOW_BOX
_FL_OVAL_FRAME = _fltk._FL_OVAL_FRAME
_FL_OFLAT_BOX = _fltk._FL_OFLAT_BOX
_FL_PLASTIC_UP_BOX = _fltk._FL_PLASTIC_UP_BOX
_FL_PLASTIC_DOWN_BOX = _fltk._FL_PLASTIC_DOWN_BOX
_FL_PLASTIC_UP_FRAME = _fltk._FL_PLASTIC_UP_FRAME
_FL_PLASTIC_DOWN_FRAME = _fltk._FL_PLASTIC_DOWN_FRAME
_FL_PLASTIC_THIN_UP_BOX = _fltk._FL_PLASTIC_THIN_UP_BOX
_FL_PLASTIC_THIN_DOWN_BOX = _fltk._FL_PLASTIC_THIN_DOWN_BOX
_FL_PLASTIC_ROUND_UP_BOX = _fltk._FL_PLASTIC_ROUND_UP_BOX
_FL_PLASTIC_ROUND_DOWN_BOX = _fltk._FL_PLASTIC_ROUND_DOWN_BOX
FL_FREE_BOXTYPE = _fltk.FL_FREE_BOXTYPE

fl_define_FL_ROUND_UP_BOX = _fltk.fl_define_FL_ROUND_UP_BOX

fl_define_FL_SHADOW_BOX = _fltk.fl_define_FL_SHADOW_BOX

fl_define_FL_ROUNDED_BOX = _fltk.fl_define_FL_ROUNDED_BOX

fl_define_FL_RFLAT_BOX = _fltk.fl_define_FL_RFLAT_BOX

fl_define_FL_RSHADOW_BOX = _fltk.fl_define_FL_RSHADOW_BOX

fl_define_FL_DIAMOND_BOX = _fltk.fl_define_FL_DIAMOND_BOX

fl_define_FL_OVAL_BOX = _fltk.fl_define_FL_OVAL_BOX

fl_define_FL_PLASTIC_UP_BOX = _fltk.fl_define_FL_PLASTIC_UP_BOX

fl_down = _fltk.fl_down
FL_NORMAL_LABEL = _fltk.FL_NORMAL_LABEL
FL_NO_LABEL = _fltk.FL_NO_LABEL
_FL_SHADOW_LABEL = _fltk._FL_SHADOW_LABEL
_FL_ENGRAVED_LABEL = _fltk._FL_ENGRAVED_LABEL
_FL_EMBOSSED_LABEL = _fltk._FL_EMBOSSED_LABEL
_FL_MULTI_LABEL = _fltk._FL_MULTI_LABEL
_FL_ICON_LABEL = _fltk._FL_ICON_LABEL
_FL_IMAGE_LABEL = _fltk._FL_IMAGE_LABEL
FL_FREE_LABELTYPE = _fltk.FL_FREE_LABELTYPE

fl_define_FL_SHADOW_LABEL = _fltk.fl_define_FL_SHADOW_LABEL

fl_define_FL_ENGRAVED_LABEL = _fltk.fl_define_FL_ENGRAVED_LABEL

fl_define_FL_EMBOSSED_LABEL = _fltk.fl_define_FL_EMBOSSED_LABEL
FL_ALIGN_CENTER = _fltk.FL_ALIGN_CENTER
FL_ALIGN_TOP = _fltk.FL_ALIGN_TOP
FL_ALIGN_BOTTOM = _fltk.FL_ALIGN_BOTTOM
FL_ALIGN_LEFT = _fltk.FL_ALIGN_LEFT
FL_ALIGN_RIGHT = _fltk.FL_ALIGN_RIGHT
FL_ALIGN_INSIDE = _fltk.FL_ALIGN_INSIDE
FL_ALIGN_TEXT_OVER_IMAGE = _fltk.FL_ALIGN_TEXT_OVER_IMAGE
FL_ALIGN_IMAGE_OVER_TEXT = _fltk.FL_ALIGN_IMAGE_OVER_TEXT
FL_ALIGN_CLIP = _fltk.FL_ALIGN_CLIP
FL_ALIGN_WRAP = _fltk.FL_ALIGN_WRAP
FL_ALIGN_TOP_LEFT = _fltk.FL_ALIGN_TOP_LEFT
FL_ALIGN_TOP_RIGHT = _fltk.FL_ALIGN_TOP_RIGHT
FL_ALIGN_BOTTOM_LEFT = _fltk.FL_ALIGN_BOTTOM_LEFT
FL_ALIGN_BOTTOM_RIGHT = _fltk.FL_ALIGN_BOTTOM_RIGHT
FL_ALIGN_LEFT_TOP = _fltk.FL_ALIGN_LEFT_TOP
FL_ALIGN_RIGHT_TOP = _fltk.FL_ALIGN_RIGHT_TOP
FL_ALIGN_LEFT_BOTTOM = _fltk.FL_ALIGN_LEFT_BOTTOM
FL_ALIGN_RIGHT_BOTTOM = _fltk.FL_ALIGN_RIGHT_BOTTOM
FL_ALIGN_NOWRAP = _fltk.FL_ALIGN_NOWRAP
FL_HELVETICA = _fltk.FL_HELVETICA
FL_HELVETICA_BOLD = _fltk.FL_HELVETICA_BOLD
FL_HELVETICA_ITALIC = _fltk.FL_HELVETICA_ITALIC
FL_HELVETICA_BOLD_ITALIC = _fltk.FL_HELVETICA_BOLD_ITALIC
FL_COURIER = _fltk.FL_COURIER
FL_COURIER_BOLD = _fltk.FL_COURIER_BOLD
FL_COURIER_ITALIC = _fltk.FL_COURIER_ITALIC
FL_COURIER_BOLD_ITALIC = _fltk.FL_COURIER_BOLD_ITALIC
FL_TIMES = _fltk.FL_TIMES
FL_TIMES_BOLD = _fltk.FL_TIMES_BOLD
FL_TIMES_ITALIC = _fltk.FL_TIMES_ITALIC
FL_TIMES_BOLD_ITALIC = _fltk.FL_TIMES_BOLD_ITALIC
FL_SYMBOL = _fltk.FL_SYMBOL
FL_SCREEN = _fltk.FL_SCREEN
FL_SCREEN_BOLD = _fltk.FL_SCREEN_BOLD
FL_ZAPF_DINGBATS = _fltk.FL_ZAPF_DINGBATS
FL_FREE_FONT = _fltk.FL_FREE_FONT
FL_BOLD = _fltk.FL_BOLD
FL_ITALIC = _fltk.FL_ITALIC
FL_FOREGROUND_COLOR = _fltk.FL_FOREGROUND_COLOR
FL_BACKGROUND2_COLOR = _fltk.FL_BACKGROUND2_COLOR
FL_INACTIVE_COLOR = _fltk.FL_INACTIVE_COLOR
FL_SELECTION_COLOR = _fltk.FL_SELECTION_COLOR
FL_GRAY0 = _fltk.FL_GRAY0
FL_DARK3 = _fltk.FL_DARK3
FL_DARK2 = _fltk.FL_DARK2
FL_DARK1 = _fltk.FL_DARK1
FL_BACKGROUND_COLOR = _fltk.FL_BACKGROUND_COLOR
FL_LIGHT1 = _fltk.FL_LIGHT1
FL_LIGHT2 = _fltk.FL_LIGHT2
FL_LIGHT3 = _fltk.FL_LIGHT3
FL_BLACK = _fltk.FL_BLACK
FL_RED = _fltk.FL_RED
FL_GREEN = _fltk.FL_GREEN
FL_YELLOW = _fltk.FL_YELLOW
FL_BLUE = _fltk.FL_BLUE
FL_MAGENTA = _fltk.FL_MAGENTA
FL_CYAN = _fltk.FL_CYAN
FL_DARK_RED = _fltk.FL_DARK_RED
FL_DARK_GREEN = _fltk.FL_DARK_GREEN
FL_DARK_YELLOW = _fltk.FL_DARK_YELLOW
FL_DARK_BLUE = _fltk.FL_DARK_BLUE
FL_DARK_MAGENTA = _fltk.FL_DARK_MAGENTA
FL_DARK_CYAN = _fltk.FL_DARK_CYAN
FL_WHITE = _fltk.FL_WHITE
FL_NUM_FREE_COLOR = _fltk.FL_NUM_FREE_COLOR
FL_NUM_GRAY = _fltk.FL_NUM_GRAY
FL_NUM_RED = _fltk.FL_NUM_RED
FL_NUM_GREEN = _fltk.FL_NUM_GREEN
FL_NUM_BLUE = _fltk.FL_NUM_BLUE

fl_inactive = _fltk.fl_inactive

fl_contrast = _fltk.fl_contrast

fl_color_average = _fltk.fl_color_average

fl_lighter = _fltk.fl_lighter

fl_darker = _fltk.fl_darker

fl_gray_ramp = _fltk.fl_gray_ramp

fl_color_cube = _fltk.fl_color_cube
FL_CURSOR_DEFAULT = _fltk.FL_CURSOR_DEFAULT
FL_CURSOR_ARROW = _fltk.FL_CURSOR_ARROW
FL_CURSOR_CROSS = _fltk.FL_CURSOR_CROSS
FL_CURSOR_WAIT = _fltk.FL_CURSOR_WAIT
FL_CURSOR_INSERT = _fltk.FL_CURSOR_INSERT
FL_CURSOR_HAND = _fltk.FL_CURSOR_HAND
FL_CURSOR_HELP = _fltk.FL_CURSOR_HELP
FL_CURSOR_MOVE = _fltk.FL_CURSOR_MOVE
FL_CURSOR_NS = _fltk.FL_CURSOR_NS
FL_CURSOR_WE = _fltk.FL_CURSOR_WE
FL_CURSOR_NWSE = _fltk.FL_CURSOR_NWSE
FL_CURSOR_NESW = _fltk.FL_CURSOR_NESW
FL_CURSOR_NONE = _fltk.FL_CURSOR_NONE
FL_CURSOR_N = _fltk.FL_CURSOR_N
FL_CURSOR_NE = _fltk.FL_CURSOR_NE
FL_CURSOR_E = _fltk.FL_CURSOR_E
FL_CURSOR_SE = _fltk.FL_CURSOR_SE
FL_CURSOR_S = _fltk.FL_CURSOR_S
FL_CURSOR_SW = _fltk.FL_CURSOR_SW
FL_CURSOR_W = _fltk.FL_CURSOR_W
FL_CURSOR_NW = _fltk.FL_CURSOR_NW
FL_READ = _fltk.FL_READ
FL_WRITE = _fltk.FL_WRITE
FL_EXCEPT = _fltk.FL_EXCEPT
FL_RGB = _fltk.FL_RGB
FL_INDEX = _fltk.FL_INDEX
FL_SINGLE = _fltk.FL_SINGLE
FL_DOUBLE = _fltk.FL_DOUBLE
FL_ACCUM = _fltk.FL_ACCUM
FL_ALPHA = _fltk.FL_ALPHA
FL_DEPTH = _fltk.FL_DEPTH
FL_STENCIL = _fltk.FL_STENCIL
FL_RGB8 = _fltk.FL_RGB8
FL_MULTISAMPLE = _fltk.FL_MULTISAMPLE
FL_STEREO = _fltk.FL_STEREO
FL_FAKE_SINGLE = _fltk.FL_FAKE_SINGLE
FL_DAMAGE_CHILD = _fltk.FL_DAMAGE_CHILD
FL_DAMAGE_EXPOSE = _fltk.FL_DAMAGE_EXPOSE
FL_DAMAGE_SCROLL = _fltk.FL_DAMAGE_SCROLL
FL_DAMAGE_OVERLAY = _fltk.FL_DAMAGE_OVERLAY
FL_DAMAGE_USER1 = _fltk.FL_DAMAGE_USER1
FL_DAMAGE_USER2 = _fltk.FL_DAMAGE_USER2
FL_DAMAGE_ALL = _fltk.FL_DAMAGE_ALL
# events
FL_KEYBOARD=FL_KEYDOWN

# additional boxtypes instead of defines
FL_ROUND_UP_BOX=fl_define_FL_ROUND_UP_BOX()
FL_ROUND_DOWN_BOX=fl_define_FL_ROUND_UP_BOX()+1
FL_SHADOW_BOX=fl_define_FL_SHADOW_BOX()
FL_SHADOW_FRAME=fl_define_FL_SHADOW_BOX()+2
FL_ROUNDED_BOX=fl_define_FL_ROUNDED_BOX()
FL_ROUNDED_FRAME=fl_define_FL_ROUNDED_BOX()+2
FL_RFLAT_BOX=fl_define_FL_RFLAT_BOX()
FL_RSHADOW_BOX=fl_define_FL_RSHADOW_BOX()
FL_DIAMOND_UP_BOX=fl_define_FL_DIAMOND_BOX()
FL_DIAMOND_DOWN_BOX=fl_define_FL_DIAMOND_BOX()+1
FL_OVAL_BOX=fl_define_FL_OVAL_BOX()
FL_OSHADOW_BOX=fl_define_FL_OVAL_BOX()+1
FL_OVAL_FRAME=fl_define_FL_OVAL_BOX()+2
FL_OFLAT_BOX=fl_define_FL_OVAL_BOX()+3
FL_PLASTIC_UP_BOX=fl_define_FL_PLASTIC_UP_BOX()
FL_PLASTIC_DOWN_BOX=fl_define_FL_PLASTIC_UP_BOX()+1
FL_PLASTIC_UP_FRAME=fl_define_FL_PLASTIC_UP_BOX()+2
FL_PLASTIC_DOWN_FRAME=fl_define_FL_PLASTIC_UP_BOX()+3
FL_PLASTIC_THIN_UP_BOX=fl_define_FL_PLASTIC_UP_BOX()+4
FL_PLASTIC_THIN_DOWN_BOX=fl_define_FL_PLASTIC_UP_BOX()+5

# color defines
FL_FREE_COLOR=16           
FL_NUM_FREE_COLOR=16       
FL_GRAY_RAMP=32           
FL_NUM_GRAY=24                     
FL_GRAY=FL_BACKGROUND_COLOR    
FL_COLOR_CUBE=56           
FL_NUM_RED=5                      
FL_NUM_GREEN=8                      
FL_NUM_BLUE=5

# label defines
FL_SYMBOL_LABEL=FL_NORMAL_LABEL
FL_SHADOW_LABEL=fl_define_FL_SHADOW_LABEL()
FL_ENGRAVED_LABEL=fl_define_FL_ENGRAVED_LABEL()
FL_EMBOSSED_LABEL=fl_define_FL_EMBOSSED_LABEL()


FL_PATH_MAX = _fltk.FL_PATH_MAX

fl_filename_name = _fltk.fl_filename_name

fl_filename_ext = _fltk.fl_filename_ext

fl_filename_match = _fltk.fl_filename_match

fl_filename_isdir = _fltk.fl_filename_isdir
class Fl_Valuator(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Valuator instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def bounds(*args): return _fltk.Fl_Valuator_bounds(*args)
    def minimum(*args): return _fltk.Fl_Valuator_minimum(*args)
    def maximum(*args): return _fltk.Fl_Valuator_maximum(*args)
    def range(*args): return _fltk.Fl_Valuator_range(*args)
    def step(*args): return _fltk.Fl_Valuator_step(*args)
    def precision(*args): return _fltk.Fl_Valuator_precision(*args)
    def value(*args): return _fltk.Fl_Valuator_value(*args)
    def format(*args): return _fltk.Fl_Valuator_format(*args)
    def round(*args): return _fltk.Fl_Valuator_round(*args)
    def clamp(*args): return _fltk.Fl_Valuator_clamp(*args)
    def increment(*args): return _fltk.Fl_Valuator_increment(*args)
    __swig_destroy__ = _fltk.delete_Fl_Valuator
Fl_Valuator.bounds = new_instancemethod(_fltk.Fl_Valuator_bounds,None,Fl_Valuator)
Fl_Valuator.minimum = new_instancemethod(_fltk.Fl_Valuator_minimum,None,Fl_Valuator)
Fl_Valuator.maximum = new_instancemethod(_fltk.Fl_Valuator_maximum,None,Fl_Valuator)
Fl_Valuator.range = new_instancemethod(_fltk.Fl_Valuator_range,None,Fl_Valuator)
Fl_Valuator.step = new_instancemethod(_fltk.Fl_Valuator_step,None,Fl_Valuator)
Fl_Valuator.precision = new_instancemethod(_fltk.Fl_Valuator_precision,None,Fl_Valuator)
Fl_Valuator.value = new_instancemethod(_fltk.Fl_Valuator_value,None,Fl_Valuator)
Fl_Valuator.format = new_instancemethod(_fltk.Fl_Valuator_format,None,Fl_Valuator)
Fl_Valuator.round = new_instancemethod(_fltk.Fl_Valuator_round,None,Fl_Valuator)
Fl_Valuator.clamp = new_instancemethod(_fltk.Fl_Valuator_clamp,None,Fl_Valuator)
Fl_Valuator.increment = new_instancemethod(_fltk.Fl_Valuator_increment,None,Fl_Valuator)
_fltk.Fl_Valuator_swigregister(Fl_Valuator)
pyFLTK_registerDoIdle = _fltk.pyFLTK_registerDoIdle

Fl_add_timeout = _fltk.Fl_add_timeout

Fl_add_handler = _fltk.Fl_add_handler

Fl_remove_handler = _fltk.Fl_remove_handler

Fl_add_check = _fltk.Fl_add_check

Fl_remove_check = _fltk.Fl_remove_check


fl_rgb_color = _fltk.fl_rgb_color

fl_filename_setext = _fltk.fl_filename_setext

fl_filename_expand = _fltk.fl_filename_expand

fl_filename_absolute = _fltk.fl_filename_absolute

fl_filename_relative = _fltk.fl_filename_relative

FL_VERTICAL=0
FL_HORIZONTAL=1

class Fl_Adjuster(Fl_Valuator):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Adjuster instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Adjuster_draw(*args)
    def handle(*args): return _fltk.Fl_Adjuster_handle(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Adjuster:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Adjuster(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def soft(*args): return _fltk.Fl_Adjuster_soft(*args)
    __swig_destroy__ = _fltk.delete_Fl_Adjuster
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Adjuster(self)
        return weakref_proxy(self)
Fl_Adjuster.draw = new_instancemethod(_fltk.Fl_Adjuster_draw,None,Fl_Adjuster)
Fl_Adjuster.handle = new_instancemethod(_fltk.Fl_Adjuster_handle,None,Fl_Adjuster)
Fl_Adjuster.soft = new_instancemethod(_fltk.Fl_Adjuster_soft,None,Fl_Adjuster)
_fltk.Fl_Adjuster_swigregister(Fl_Adjuster)

FL_BEEP_DEFAULT = _fltk.FL_BEEP_DEFAULT
FL_BEEP_MESSAGE = _fltk.FL_BEEP_MESSAGE
FL_BEEP_ERROR = _fltk.FL_BEEP_ERROR
FL_BEEP_QUESTION = _fltk.FL_BEEP_QUESTION
FL_BEEP_PASSWORD = _fltk.FL_BEEP_PASSWORD
FL_BEEP_NOTIFICATION = _fltk.FL_BEEP_NOTIFICATION

fl_beep = _fltk.fl_beep

fl_message = _fltk.fl_message

fl_alert = _fltk.fl_alert

fl_ask = _fltk.fl_ask

fl_choice = _fltk.fl_choice

fl_message_icon = _fltk.fl_message_icon

fl_message_font = _fltk.fl_message_font

fl_input = _fltk.fl_input

fl_password = _fltk.fl_password

fl_mt_message = _fltk.fl_mt_message

fl_mt_alert = _fltk.fl_mt_alert

fl_mt_ask = _fltk.fl_mt_ask

fl_mt_choice = _fltk.fl_mt_choice

fl_mt_input = _fltk.fl_mt_input

fl_mt_password = _fltk.fl_mt_password
class Fl_Image(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Image instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def w(*args): return _fltk.Fl_Image_w(*args)
    def h(*args): return _fltk.Fl_Image_h(*args)
    def d(*args): return _fltk.Fl_Image_d(*args)
    def ld(*args): return _fltk.Fl_Image_ld(*args)
    def count(*args): return _fltk.Fl_Image_count(*args)
    def data(*args): return _fltk.Fl_Image_data(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Image:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Image(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Image
    def copy(*args): return _fltk.Fl_Image_copy(*args)
    def color_average(*args): return _fltk.Fl_Image_color_average(*args)
    def inactive(*args): return _fltk.Fl_Image_inactive(*args)
    def desaturate(*args): return _fltk.Fl_Image_desaturate(*args)
    def label(*args): return _fltk.Fl_Image_label(*args)
    def draw(*args): return _fltk.Fl_Image_draw(*args)
    def uncache(*args): return _fltk.Fl_Image_uncache(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Image(self)
        return weakref_proxy(self)
Fl_Image.w = new_instancemethod(_fltk.Fl_Image_w,None,Fl_Image)
Fl_Image.h = new_instancemethod(_fltk.Fl_Image_h,None,Fl_Image)
Fl_Image.d = new_instancemethod(_fltk.Fl_Image_d,None,Fl_Image)
Fl_Image.ld = new_instancemethod(_fltk.Fl_Image_ld,None,Fl_Image)
Fl_Image.count = new_instancemethod(_fltk.Fl_Image_count,None,Fl_Image)
Fl_Image.data = new_instancemethod(_fltk.Fl_Image_data,None,Fl_Image)
Fl_Image.copy = new_instancemethod(_fltk.Fl_Image_copy,None,Fl_Image)
Fl_Image.color_average = new_instancemethod(_fltk.Fl_Image_color_average,None,Fl_Image)
Fl_Image.inactive = new_instancemethod(_fltk.Fl_Image_inactive,None,Fl_Image)
Fl_Image.desaturate = new_instancemethod(_fltk.Fl_Image_desaturate,None,Fl_Image)
Fl_Image.label = new_instancemethod(_fltk.Fl_Image_label,None,Fl_Image)
Fl_Image.draw = new_instancemethod(_fltk.Fl_Image_draw,None,Fl_Image)
Fl_Image.uncache = new_instancemethod(_fltk.Fl_Image_uncache,None,Fl_Image)
_fltk.Fl_Image_swigregister(Fl_Image)

class Fl_RGB_Image(Fl_Image):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_RGB_Image instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    array = property(_fltk.Fl_RGB_Image_array_get, _fltk.Fl_RGB_Image_array_set)
    alloc_array = property(_fltk.Fl_RGB_Image_alloc_array_get, _fltk.Fl_RGB_Image_alloc_array_set)
    def __init__(self, *args):
        if self.__class__ == Fl_RGB_Image:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_RGB_Image(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_RGB_Image
    def copy(*args): return _fltk.Fl_RGB_Image_copy(*args)
    def color_average(*args): return _fltk.Fl_RGB_Image_color_average(*args)
    def desaturate(*args): return _fltk.Fl_RGB_Image_desaturate(*args)
    def draw(*args): return _fltk.Fl_RGB_Image_draw(*args)
    def label(*args): return _fltk.Fl_RGB_Image_label(*args)
    def uncache(*args): return _fltk.Fl_RGB_Image_uncache(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_RGB_Image(self)
        return weakref_proxy(self)
Fl_RGB_Image.copy = new_instancemethod(_fltk.Fl_RGB_Image_copy,None,Fl_RGB_Image)
Fl_RGB_Image.color_average = new_instancemethod(_fltk.Fl_RGB_Image_color_average,None,Fl_RGB_Image)
Fl_RGB_Image.desaturate = new_instancemethod(_fltk.Fl_RGB_Image_desaturate,None,Fl_RGB_Image)
Fl_RGB_Image.draw = new_instancemethod(_fltk.Fl_RGB_Image_draw,None,Fl_RGB_Image)
Fl_RGB_Image.label = new_instancemethod(_fltk.Fl_RGB_Image_label,None,Fl_RGB_Image)
Fl_RGB_Image.uncache = new_instancemethod(_fltk.Fl_RGB_Image_uncache,None,Fl_RGB_Image)
_fltk.Fl_RGB_Image_swigregister(Fl_RGB_Image)

class Fl_Bitmap(Fl_Image):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Bitmap instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    array = property(_fltk.Fl_Bitmap_array_get, _fltk.Fl_Bitmap_array_set)
    alloc_array = property(_fltk.Fl_Bitmap_alloc_array_get, _fltk.Fl_Bitmap_alloc_array_set)
    def __init__(self, *args):
        if self.__class__ == Fl_Bitmap:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Bitmap(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Bitmap
    def copy(*args): return _fltk.Fl_Bitmap_copy(*args)
    def draw(*args): return _fltk.Fl_Bitmap_draw(*args)
    def label(*args): return _fltk.Fl_Bitmap_label(*args)
    def uncache(*args): return _fltk.Fl_Bitmap_uncache(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Bitmap(self)
        return weakref_proxy(self)
Fl_Bitmap.copy = new_instancemethod(_fltk.Fl_Bitmap_copy,None,Fl_Bitmap)
Fl_Bitmap.draw = new_instancemethod(_fltk.Fl_Bitmap_draw,None,Fl_Bitmap)
Fl_Bitmap.label = new_instancemethod(_fltk.Fl_Bitmap_label,None,Fl_Bitmap)
Fl_Bitmap.uncache = new_instancemethod(_fltk.Fl_Bitmap_uncache,None,Fl_Bitmap)
_fltk.Fl_Bitmap_swigregister(Fl_Bitmap)

class Fl_BMP_Image(Fl_RGB_Image):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_BMP_Image instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_BMP_Image:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_BMP_Image(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_BMP_Image
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_BMP_Image(self)
        return weakref_proxy(self)
_fltk.Fl_BMP_Image_swigregister(Fl_BMP_Image)

class Fl_Box(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Box instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Box_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Box:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Box(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def handle(*args): return _fltk.Fl_Box_handle(*args)
    __swig_destroy__ = _fltk.delete_Fl_Box
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Box(self)
        return weakref_proxy(self)
Fl_Box.draw = new_instancemethod(_fltk.Fl_Box_draw,None,Fl_Box)
Fl_Box.handle = new_instancemethod(_fltk.Fl_Box_handle,None,Fl_Box)
_fltk.Fl_Box_swigregister(Fl_Box)

FL_NORMAL_BUTTON = _fltk.FL_NORMAL_BUTTON
FL_TOGGLE_BUTTON = _fltk.FL_TOGGLE_BUTTON
FL_RADIO_BUTTON = _fltk.FL_RADIO_BUTTON
FL_HIDDEN_BUTTON = _fltk.FL_HIDDEN_BUTTON

fl_old_shortcut = _fltk.fl_old_shortcut
class Fl_Button(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Button instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Button_draw(*args)
    def handle(*args): return _fltk.Fl_Button_handle(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Button:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Button(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def value(*args): return _fltk.Fl_Button_value(*args)
    def set(*args): return _fltk.Fl_Button_set(*args)
    def clear(*args): return _fltk.Fl_Button_clear(*args)
    def setonly(*args): return _fltk.Fl_Button_setonly(*args)
    def down_box(*args): return _fltk.Fl_Button_down_box(*args)
    def shortcut(*args): return _fltk.Fl_Button_shortcut(*args)
    def down_color(*args): return _fltk.Fl_Button_down_color(*args)
    __swig_destroy__ = _fltk.delete_Fl_Button
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Button(self)
        return weakref_proxy(self)
Fl_Button.draw = new_instancemethod(_fltk.Fl_Button_draw,None,Fl_Button)
Fl_Button.handle = new_instancemethod(_fltk.Fl_Button_handle,None,Fl_Button)
Fl_Button.value = new_instancemethod(_fltk.Fl_Button_value,None,Fl_Button)
Fl_Button.set = new_instancemethod(_fltk.Fl_Button_set,None,Fl_Button)
Fl_Button.clear = new_instancemethod(_fltk.Fl_Button_clear,None,Fl_Button)
Fl_Button.setonly = new_instancemethod(_fltk.Fl_Button_setonly,None,Fl_Button)
Fl_Button.down_box = new_instancemethod(_fltk.Fl_Button_down_box,None,Fl_Button)
Fl_Button.shortcut = new_instancemethod(_fltk.Fl_Button_shortcut,None,Fl_Button)
Fl_Button.down_color = new_instancemethod(_fltk.Fl_Button_down_color,None,Fl_Button)
_fltk.Fl_Button_swigregister(Fl_Button)

FL_BAR_CHART = _fltk.FL_BAR_CHART
FL_HORBAR_CHART = _fltk.FL_HORBAR_CHART
FL_LINE_CHART = _fltk.FL_LINE_CHART
FL_FILL_CHART = _fltk.FL_FILL_CHART
FL_SPIKE_CHART = _fltk.FL_SPIKE_CHART
FL_PIE_CHART = _fltk.FL_PIE_CHART
FL_SPECIALPIE_CHART = _fltk.FL_SPECIALPIE_CHART
FL_FILLED_CHART = _fltk.FL_FILLED_CHART
FL_CHART_MAX = _fltk.FL_CHART_MAX
FL_CHART_LABEL_MAX = _fltk.FL_CHART_LABEL_MAX
class FL_CHART_ENTRY(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ FL_CHART_ENTRY instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    val = property(_fltk.FL_CHART_ENTRY_val_get, _fltk.FL_CHART_ENTRY_val_set)
    col = property(_fltk.FL_CHART_ENTRY_col_get, _fltk.FL_CHART_ENTRY_col_set)
    str = property(_fltk.FL_CHART_ENTRY_str_get, _fltk.FL_CHART_ENTRY_str_set)
    def __init__(self, *args):
        this = _fltk.new_FL_CHART_ENTRY(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_FL_CHART_ENTRY
_fltk.FL_CHART_ENTRY_swigregister(FL_CHART_ENTRY)

class Fl_Chart(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Chart instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Chart_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Chart:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Chart(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Chart
    def clear(*args): return _fltk.Fl_Chart_clear(*args)
    def add(*args): return _fltk.Fl_Chart_add(*args)
    def insert(*args): return _fltk.Fl_Chart_insert(*args)
    def replace(*args): return _fltk.Fl_Chart_replace(*args)
    def bounds(*args): return _fltk.Fl_Chart_bounds(*args)
    def size(*args): return _fltk.Fl_Chart_size(*args)
    def maxsize(*args): return _fltk.Fl_Chart_maxsize(*args)
    def textfont(*args): return _fltk.Fl_Chart_textfont(*args)
    def textsize(*args): return _fltk.Fl_Chart_textsize(*args)
    def textcolor(*args): return _fltk.Fl_Chart_textcolor(*args)
    def autosize(*args): return _fltk.Fl_Chart_autosize(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Chart(self)
        return weakref_proxy(self)
Fl_Chart.draw = new_instancemethod(_fltk.Fl_Chart_draw,None,Fl_Chart)
Fl_Chart.clear = new_instancemethod(_fltk.Fl_Chart_clear,None,Fl_Chart)
Fl_Chart.add = new_instancemethod(_fltk.Fl_Chart_add,None,Fl_Chart)
Fl_Chart.insert = new_instancemethod(_fltk.Fl_Chart_insert,None,Fl_Chart)
Fl_Chart.replace = new_instancemethod(_fltk.Fl_Chart_replace,None,Fl_Chart)
Fl_Chart.bounds = new_instancemethod(_fltk.Fl_Chart_bounds,None,Fl_Chart)
Fl_Chart.size = new_instancemethod(_fltk.Fl_Chart_size,None,Fl_Chart)
Fl_Chart.maxsize = new_instancemethod(_fltk.Fl_Chart_maxsize,None,Fl_Chart)
Fl_Chart.textfont = new_instancemethod(_fltk.Fl_Chart_textfont,None,Fl_Chart)
Fl_Chart.textsize = new_instancemethod(_fltk.Fl_Chart_textsize,None,Fl_Chart)
Fl_Chart.textcolor = new_instancemethod(_fltk.Fl_Chart_textcolor,None,Fl_Chart)
Fl_Chart.autosize = new_instancemethod(_fltk.Fl_Chart_autosize,None,Fl_Chart)
_fltk.Fl_Chart_swigregister(Fl_Chart)

class Fl_Check_Browser(Fl_Browser_):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Check_Browser instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Check_Browser:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Check_Browser(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Check_Browser
    def add(*args): return _fltk.Fl_Check_Browser_add(*args)
    def clear(*args): return _fltk.Fl_Check_Browser_clear(*args)
    def nitems(*args): return _fltk.Fl_Check_Browser_nitems(*args)
    def nchecked(*args): return _fltk.Fl_Check_Browser_nchecked(*args)
    def checked(*args): return _fltk.Fl_Check_Browser_checked(*args)
    def set_checked(*args): return _fltk.Fl_Check_Browser_set_checked(*args)
    def check_all(*args): return _fltk.Fl_Check_Browser_check_all(*args)
    def check_none(*args): return _fltk.Fl_Check_Browser_check_none(*args)
    def value(*args): return _fltk.Fl_Check_Browser_value(*args)
    def text(*args): return _fltk.Fl_Check_Browser_text(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Check_Browser(self)
        return weakref_proxy(self)
    def item_first(*args): return _fltk.Fl_Check_Browser_item_first(*args)
    def item_prev(*args): return _fltk.Fl_Check_Browser_item_prev(*args)
    def item_next(*args): return _fltk.Fl_Check_Browser_item_next(*args)
    def item_draw(*args): return _fltk.Fl_Check_Browser_item_draw(*args)
    def incr_height(*args): return _fltk.Fl_Check_Browser_incr_height(*args)
    def full_height(*args): return _fltk.Fl_Check_Browser_full_height(*args)
    def full_width(*args): return _fltk.Fl_Check_Browser_full_width(*args)
    def item_select(*args): return _fltk.Fl_Check_Browser_item_select(*args)
    def draw(*args): return _fltk.Fl_Check_Browser_draw(*args)
    def item_quick_height(*args): return _fltk.Fl_Check_Browser_item_quick_height(*args)
    def item_width(*args): return _fltk.Fl_Check_Browser_item_width(*args)
    def item_height(*args): return _fltk.Fl_Check_Browser_item_height(*args)
    def item_selected(*args): return _fltk.Fl_Check_Browser_item_selected(*args)
Fl_Check_Browser.add = new_instancemethod(_fltk.Fl_Check_Browser_add,None,Fl_Check_Browser)
Fl_Check_Browser.clear = new_instancemethod(_fltk.Fl_Check_Browser_clear,None,Fl_Check_Browser)
Fl_Check_Browser.nitems = new_instancemethod(_fltk.Fl_Check_Browser_nitems,None,Fl_Check_Browser)
Fl_Check_Browser.nchecked = new_instancemethod(_fltk.Fl_Check_Browser_nchecked,None,Fl_Check_Browser)
Fl_Check_Browser.checked = new_instancemethod(_fltk.Fl_Check_Browser_checked,None,Fl_Check_Browser)
Fl_Check_Browser.set_checked = new_instancemethod(_fltk.Fl_Check_Browser_set_checked,None,Fl_Check_Browser)
Fl_Check_Browser.check_all = new_instancemethod(_fltk.Fl_Check_Browser_check_all,None,Fl_Check_Browser)
Fl_Check_Browser.check_none = new_instancemethod(_fltk.Fl_Check_Browser_check_none,None,Fl_Check_Browser)
Fl_Check_Browser.value = new_instancemethod(_fltk.Fl_Check_Browser_value,None,Fl_Check_Browser)
Fl_Check_Browser.text = new_instancemethod(_fltk.Fl_Check_Browser_text,None,Fl_Check_Browser)
Fl_Check_Browser.item_first = new_instancemethod(_fltk.Fl_Check_Browser_item_first,None,Fl_Check_Browser)
Fl_Check_Browser.item_prev = new_instancemethod(_fltk.Fl_Check_Browser_item_prev,None,Fl_Check_Browser)
Fl_Check_Browser.item_next = new_instancemethod(_fltk.Fl_Check_Browser_item_next,None,Fl_Check_Browser)
Fl_Check_Browser.item_draw = new_instancemethod(_fltk.Fl_Check_Browser_item_draw,None,Fl_Check_Browser)
Fl_Check_Browser.incr_height = new_instancemethod(_fltk.Fl_Check_Browser_incr_height,None,Fl_Check_Browser)
Fl_Check_Browser.full_height = new_instancemethod(_fltk.Fl_Check_Browser_full_height,None,Fl_Check_Browser)
Fl_Check_Browser.full_width = new_instancemethod(_fltk.Fl_Check_Browser_full_width,None,Fl_Check_Browser)
Fl_Check_Browser.item_select = new_instancemethod(_fltk.Fl_Check_Browser_item_select,None,Fl_Check_Browser)
Fl_Check_Browser.draw = new_instancemethod(_fltk.Fl_Check_Browser_draw,None,Fl_Check_Browser)
Fl_Check_Browser.item_quick_height = new_instancemethod(_fltk.Fl_Check_Browser_item_quick_height,None,Fl_Check_Browser)
Fl_Check_Browser.item_width = new_instancemethod(_fltk.Fl_Check_Browser_item_width,None,Fl_Check_Browser)
Fl_Check_Browser.item_height = new_instancemethod(_fltk.Fl_Check_Browser_item_height,None,Fl_Check_Browser)
Fl_Check_Browser.item_selected = new_instancemethod(_fltk.Fl_Check_Browser_item_selected,None,Fl_Check_Browser)
_fltk.Fl_Check_Browser_swigregister(Fl_Check_Browser)

class Fl_Light_Button(Fl_Button):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Light_Button instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Light_Button_draw(*args)
    def handle(*args): return _fltk.Fl_Light_Button_handle(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Light_Button:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Light_Button(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Light_Button
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Light_Button(self)
        return weakref_proxy(self)
Fl_Light_Button.draw = new_instancemethod(_fltk.Fl_Light_Button_draw,None,Fl_Light_Button)
Fl_Light_Button.handle = new_instancemethod(_fltk.Fl_Light_Button_handle,None,Fl_Light_Button)
_fltk.Fl_Light_Button_swigregister(Fl_Light_Button)

class Fl_Check_Button(Fl_Light_Button):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Check_Button instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Check_Button:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Check_Button(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Check_Button
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Check_Button(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Check_Button_draw(*args)
Fl_Check_Button.draw = new_instancemethod(_fltk.Fl_Check_Button_draw,None,Fl_Check_Button)
_fltk.Fl_Check_Button_swigregister(Fl_Check_Button)

class Fl_Menu_(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Menu_ instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Menu_:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Menu_(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Menu_
    def item_pathname(*args): return _fltk.Fl_Menu__item_pathname(*args)
    def picked(*args): return _fltk.Fl_Menu__picked(*args)
    def find_item(*args): return _fltk.Fl_Menu__find_item(*args)
    def test_shortcut(*args): return _fltk.Fl_Menu__test_shortcut(*args)
    def size(*args): return _fltk.Fl_Menu__size(*args)
    def clear(*args): return _fltk.Fl_Menu__clear(*args)
    def replace(*args): return _fltk.Fl_Menu__replace(*args)
    def remove(*args): return _fltk.Fl_Menu__remove(*args)
    def shortcut(*args): return _fltk.Fl_Menu__shortcut(*args)
    def mode(*args): return _fltk.Fl_Menu__mode(*args)
    def mvalue(*args): return _fltk.Fl_Menu__mvalue(*args)
    def value(*args): return _fltk.Fl_Menu__value(*args)
    def text(*args): return _fltk.Fl_Menu__text(*args)
    def textfont(*args): return _fltk.Fl_Menu__textfont(*args)
    def textsize(*args): return _fltk.Fl_Menu__textsize(*args)
    def textcolor(*args): return _fltk.Fl_Menu__textcolor(*args)
    def down_box(*args): return _fltk.Fl_Menu__down_box(*args)
    def down_color(*args): return _fltk.Fl_Menu__down_color(*args)
    def copy(*args): return _fltk.Fl_Menu__copy(*args)
    def add(*args): return _fltk.Fl_Menu__add(*args)
    def menu(*args): return _fltk.Fl_Menu__menu(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Menu_(self)
        return weakref_proxy(self)
Fl_Menu_.item_pathname = new_instancemethod(_fltk.Fl_Menu__item_pathname,None,Fl_Menu_)
Fl_Menu_.picked = new_instancemethod(_fltk.Fl_Menu__picked,None,Fl_Menu_)
Fl_Menu_.find_item = new_instancemethod(_fltk.Fl_Menu__find_item,None,Fl_Menu_)
Fl_Menu_.test_shortcut = new_instancemethod(_fltk.Fl_Menu__test_shortcut,None,Fl_Menu_)
Fl_Menu_.size = new_instancemethod(_fltk.Fl_Menu__size,None,Fl_Menu_)
Fl_Menu_.clear = new_instancemethod(_fltk.Fl_Menu__clear,None,Fl_Menu_)
Fl_Menu_.replace = new_instancemethod(_fltk.Fl_Menu__replace,None,Fl_Menu_)
Fl_Menu_.remove = new_instancemethod(_fltk.Fl_Menu__remove,None,Fl_Menu_)
Fl_Menu_.shortcut = new_instancemethod(_fltk.Fl_Menu__shortcut,None,Fl_Menu_)
Fl_Menu_.mode = new_instancemethod(_fltk.Fl_Menu__mode,None,Fl_Menu_)
Fl_Menu_.mvalue = new_instancemethod(_fltk.Fl_Menu__mvalue,None,Fl_Menu_)
Fl_Menu_.value = new_instancemethod(_fltk.Fl_Menu__value,None,Fl_Menu_)
Fl_Menu_.text = new_instancemethod(_fltk.Fl_Menu__text,None,Fl_Menu_)
Fl_Menu_.textfont = new_instancemethod(_fltk.Fl_Menu__textfont,None,Fl_Menu_)
Fl_Menu_.textsize = new_instancemethod(_fltk.Fl_Menu__textsize,None,Fl_Menu_)
Fl_Menu_.textcolor = new_instancemethod(_fltk.Fl_Menu__textcolor,None,Fl_Menu_)
Fl_Menu_.down_box = new_instancemethod(_fltk.Fl_Menu__down_box,None,Fl_Menu_)
Fl_Menu_.down_color = new_instancemethod(_fltk.Fl_Menu__down_color,None,Fl_Menu_)
Fl_Menu_.copy = new_instancemethod(_fltk.Fl_Menu__copy,None,Fl_Menu_)
Fl_Menu_.add = new_instancemethod(_fltk.Fl_Menu__add,None,Fl_Menu_)
Fl_Menu_.menu = new_instancemethod(_fltk.Fl_Menu__menu,None,Fl_Menu_)
_fltk.Fl_Menu__swigregister(Fl_Menu_)

class Fl_Choice(Fl_Menu_):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Choice instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Choice_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Choice:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Choice(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def value(*args): return _fltk.Fl_Choice_value(*args)
    __swig_destroy__ = _fltk.delete_Fl_Choice
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Choice(self)
        return weakref_proxy(self)
Fl_Choice.draw = new_instancemethod(_fltk.Fl_Choice_draw,None,Fl_Choice)
Fl_Choice.value = new_instancemethod(_fltk.Fl_Choice_value,None,Fl_Choice)
_fltk.Fl_Choice_swigregister(Fl_Choice)

FL_SQUARE_CLOCK = _fltk.FL_SQUARE_CLOCK
FL_ROUND_CLOCK = _fltk.FL_ROUND_CLOCK
FL_ANALOG_CLOCK = _fltk.FL_ANALOG_CLOCK
FL_DIGITAL_CLOCK = _fltk.FL_DIGITAL_CLOCK
class Fl_Clock_Output(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Clock_Output instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Clock_Output_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Clock_Output:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Clock_Output(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def value(*args): return _fltk.Fl_Clock_Output_value(*args)
    def hour(*args): return _fltk.Fl_Clock_Output_hour(*args)
    def minute(*args): return _fltk.Fl_Clock_Output_minute(*args)
    def second(*args): return _fltk.Fl_Clock_Output_second(*args)
    __swig_destroy__ = _fltk.delete_Fl_Clock_Output
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Clock_Output(self)
        return weakref_proxy(self)
Fl_Clock_Output.draw = new_instancemethod(_fltk.Fl_Clock_Output_draw,None,Fl_Clock_Output)
Fl_Clock_Output.value = new_instancemethod(_fltk.Fl_Clock_Output_value,None,Fl_Clock_Output)
Fl_Clock_Output.hour = new_instancemethod(_fltk.Fl_Clock_Output_hour,None,Fl_Clock_Output)
Fl_Clock_Output.minute = new_instancemethod(_fltk.Fl_Clock_Output_minute,None,Fl_Clock_Output)
Fl_Clock_Output.second = new_instancemethod(_fltk.Fl_Clock_Output_second,None,Fl_Clock_Output)
_fltk.Fl_Clock_Output_swigregister(Fl_Clock_Output)

class Fl_Clock(Fl_Clock_Output):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Clock instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Clock:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Clock(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Clock
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Clock(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Clock_draw(*args)
Fl_Clock.draw = new_instancemethod(_fltk.Fl_Clock_draw,None,Fl_Clock)
_fltk.Fl_Clock_swigregister(Fl_Clock)

class Fl_Value_Input(Fl_Valuator):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Value_Input instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Value_Input:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Value_Input(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def soft(*args): return _fltk.Fl_Value_Input_soft(*args)
    def textfont(*args): return _fltk.Fl_Value_Input_textfont(*args)
    def textsize(*args): return _fltk.Fl_Value_Input_textsize(*args)
    def textcolor(*args): return _fltk.Fl_Value_Input_textcolor(*args)
    def cursor_color(*args): return _fltk.Fl_Value_Input_cursor_color(*args)
    __swig_destroy__ = _fltk.delete_Fl_Value_Input
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Value_Input(self)
        return weakref_proxy(self)
Fl_Value_Input.soft = new_instancemethod(_fltk.Fl_Value_Input_soft,None,Fl_Value_Input)
Fl_Value_Input.textfont = new_instancemethod(_fltk.Fl_Value_Input_textfont,None,Fl_Value_Input)
Fl_Value_Input.textsize = new_instancemethod(_fltk.Fl_Value_Input_textsize,None,Fl_Value_Input)
Fl_Value_Input.textcolor = new_instancemethod(_fltk.Fl_Value_Input_textcolor,None,Fl_Value_Input)
Fl_Value_Input.cursor_color = new_instancemethod(_fltk.Fl_Value_Input_cursor_color,None,Fl_Value_Input)
_fltk.Fl_Value_Input_swigregister(Fl_Value_Input)

class Flcc_HueBox(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Flcc_HueBox instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Flcc_HueBox_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Flcc_HueBox:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Flcc_HueBox(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Flcc_HueBox
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Flcc_HueBox(self)
        return weakref_proxy(self)
Flcc_HueBox.draw = new_instancemethod(_fltk.Flcc_HueBox_draw,None,Flcc_HueBox)
_fltk.Flcc_HueBox_swigregister(Flcc_HueBox)

class Flcc_ValueBox(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Flcc_ValueBox instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Flcc_ValueBox_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Flcc_ValueBox:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Flcc_ValueBox(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Flcc_ValueBox
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Flcc_ValueBox(self)
        return weakref_proxy(self)
Flcc_ValueBox.draw = new_instancemethod(_fltk.Flcc_ValueBox_draw,None,Flcc_ValueBox)
_fltk.Flcc_ValueBox_swigregister(Flcc_ValueBox)

class Flcc_Value_Input(Fl_Value_Input):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Flcc_Value_Input instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Flcc_Value_Input:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Flcc_Value_Input(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Flcc_Value_Input
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Flcc_Value_Input(self)
        return weakref_proxy(self)
_fltk.Flcc_Value_Input_swigregister(Flcc_Value_Input)

class Fl_Color_Chooser(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Color_Chooser instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def mode(*args): return _fltk.Fl_Color_Chooser_mode(*args)
    def hue(*args): return _fltk.Fl_Color_Chooser_hue(*args)
    def saturation(*args): return _fltk.Fl_Color_Chooser_saturation(*args)
    def value(*args): return _fltk.Fl_Color_Chooser_value(*args)
    def r(*args): return _fltk.Fl_Color_Chooser_r(*args)
    def g(*args): return _fltk.Fl_Color_Chooser_g(*args)
    def b(*args): return _fltk.Fl_Color_Chooser_b(*args)
    def hsv(*args): return _fltk.Fl_Color_Chooser_hsv(*args)
    def rgb(*args): return _fltk.Fl_Color_Chooser_rgb(*args)
    hsv2rgb = staticmethod(_fltk.Fl_Color_Chooser_hsv2rgb)
    rgb2hsv = staticmethod(_fltk.Fl_Color_Chooser_rgb2hsv)
    def __init__(self, *args):
        if self.__class__ == Fl_Color_Chooser:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Color_Chooser(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Color_Chooser
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Color_Chooser(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Color_Chooser_draw(*args)
Fl_Color_Chooser.mode = new_instancemethod(_fltk.Fl_Color_Chooser_mode,None,Fl_Color_Chooser)
Fl_Color_Chooser.hue = new_instancemethod(_fltk.Fl_Color_Chooser_hue,None,Fl_Color_Chooser)
Fl_Color_Chooser.saturation = new_instancemethod(_fltk.Fl_Color_Chooser_saturation,None,Fl_Color_Chooser)
Fl_Color_Chooser.value = new_instancemethod(_fltk.Fl_Color_Chooser_value,None,Fl_Color_Chooser)
Fl_Color_Chooser.r = new_instancemethod(_fltk.Fl_Color_Chooser_r,None,Fl_Color_Chooser)
Fl_Color_Chooser.g = new_instancemethod(_fltk.Fl_Color_Chooser_g,None,Fl_Color_Chooser)
Fl_Color_Chooser.b = new_instancemethod(_fltk.Fl_Color_Chooser_b,None,Fl_Color_Chooser)
Fl_Color_Chooser.hsv = new_instancemethod(_fltk.Fl_Color_Chooser_hsv,None,Fl_Color_Chooser)
Fl_Color_Chooser.rgb = new_instancemethod(_fltk.Fl_Color_Chooser_rgb,None,Fl_Color_Chooser)
Fl_Color_Chooser.draw = new_instancemethod(_fltk.Fl_Color_Chooser_draw,None,Fl_Color_Chooser)
_fltk.Fl_Color_Chooser_swigregister(Fl_Color_Chooser)

Fl_Color_Chooser_hsv2rgb = _fltk.Fl_Color_Chooser_hsv2rgb

Fl_Color_Chooser_rgb2hsv = _fltk.Fl_Color_Chooser_rgb2hsv


fl_color_chooser = _fltk.fl_color_chooser
FL_NORMAL_COUNTER = _fltk.FL_NORMAL_COUNTER
FL_SIMPLE_COUNTER = _fltk.FL_SIMPLE_COUNTER
class Fl_Counter(Fl_Valuator):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Counter instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Counter_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Counter:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Counter(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Counter
    def lstep(*args): return _fltk.Fl_Counter_lstep(*args)
    def step(*args): return _fltk.Fl_Counter_step(*args)
    def textfont(*args): return _fltk.Fl_Counter_textfont(*args)
    def textsize(*args): return _fltk.Fl_Counter_textsize(*args)
    def textcolor(*args): return _fltk.Fl_Counter_textcolor(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Counter(self)
        return weakref_proxy(self)
Fl_Counter.draw = new_instancemethod(_fltk.Fl_Counter_draw,None,Fl_Counter)
Fl_Counter.lstep = new_instancemethod(_fltk.Fl_Counter_lstep,None,Fl_Counter)
Fl_Counter.step = new_instancemethod(_fltk.Fl_Counter_step,None,Fl_Counter)
Fl_Counter.textfont = new_instancemethod(_fltk.Fl_Counter_textfont,None,Fl_Counter)
Fl_Counter.textsize = new_instancemethod(_fltk.Fl_Counter_textsize,None,Fl_Counter)
Fl_Counter.textcolor = new_instancemethod(_fltk.Fl_Counter_textcolor,None,Fl_Counter)
_fltk.Fl_Counter_swigregister(Fl_Counter)

FL_NORMAL_DIAL = _fltk.FL_NORMAL_DIAL
FL_LINE_DIAL = _fltk.FL_LINE_DIAL
FL_FILL_DIAL = _fltk.FL_FILL_DIAL
class Fl_Dial(Fl_Valuator):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Dial instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Dial_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Dial:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Dial(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def angle1(*args): return _fltk.Fl_Dial_angle1(*args)
    def angle2(*args): return _fltk.Fl_Dial_angle2(*args)
    def angles(*args): return _fltk.Fl_Dial_angles(*args)
    __swig_destroy__ = _fltk.delete_Fl_Dial
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Dial(self)
        return weakref_proxy(self)
Fl_Dial.draw = new_instancemethod(_fltk.Fl_Dial_draw,None,Fl_Dial)
Fl_Dial.angle1 = new_instancemethod(_fltk.Fl_Dial_angle1,None,Fl_Dial)
Fl_Dial.angle2 = new_instancemethod(_fltk.Fl_Dial_angle2,None,Fl_Dial)
Fl_Dial.angles = new_instancemethod(_fltk.Fl_Dial_angles,None,Fl_Dial)
_fltk.Fl_Dial_swigregister(Fl_Dial)

FL_WINDOW = _fltk.FL_WINDOW
FL_DOUBLE_WINDOW = _fltk.FL_DOUBLE_WINDOW
class Fl_Window(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Window instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Window_draw(*args)
    def flush(*args): return _fltk.Fl_Window_flush(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Window:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Window(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Window
    def handle(*args): return _fltk.Fl_Window_handle(*args)
    def resize(*args): return _fltk.Fl_Window_resize(*args)
    def clear_border(*args): return _fltk.Fl_Window_clear_border(*args)
    def border(*args): return _fltk.Fl_Window_border(*args)
    def set_override(*args): return _fltk.Fl_Window_set_override(*args)
    def override(*args): return _fltk.Fl_Window_override(*args)
    def set_modal(*args): return _fltk.Fl_Window_set_modal(*args)
    def modal(*args): return _fltk.Fl_Window_modal(*args)
    def set_non_modal(*args): return _fltk.Fl_Window_set_non_modal(*args)
    def non_modal(*args): return _fltk.Fl_Window_non_modal(*args)
    def hotspot(*args): return _fltk.Fl_Window_hotspot(*args)
    def free_position(*args): return _fltk.Fl_Window_free_position(*args)
    def size_range(*args): return _fltk.Fl_Window_size_range(*args)
    def iconlabel(*args): return _fltk.Fl_Window_iconlabel(*args)
    def label(*args): return _fltk.Fl_Window_label(*args)
    def copy_label(*args): return _fltk.Fl_Window_copy_label(*args)
    def xclass(*args): return _fltk.Fl_Window_xclass(*args)
    def icon(*args): return _fltk.Fl_Window_icon(*args)
    def shown(*args): return _fltk.Fl_Window_shown(*args)
    def hide(*args): return _fltk.Fl_Window_hide(*args)
    def fullscreen(*args): return _fltk.Fl_Window_fullscreen(*args)
    def fullscreen_off(*args): return _fltk.Fl_Window_fullscreen_off(*args)
    def iconize(*args): return _fltk.Fl_Window_iconize(*args)
    def x_root(*args): return _fltk.Fl_Window_x_root(*args)
    def y_root(*args): return _fltk.Fl_Window_y_root(*args)
    current = staticmethod(_fltk.Fl_Window_current)
    def make_current(*args): return _fltk.Fl_Window_make_current(*args)
    def cursor(*args): return _fltk.Fl_Window_cursor(*args)
    def default_cursor(*args): return _fltk.Fl_Window_default_cursor(*args)
    default_callback = staticmethod(_fltk.Fl_Window_default_callback)
    def show(*args): return _fltk.Fl_Window_show(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Window(self)
        return weakref_proxy(self)
Fl_Window.draw = new_instancemethod(_fltk.Fl_Window_draw,None,Fl_Window)
Fl_Window.flush = new_instancemethod(_fltk.Fl_Window_flush,None,Fl_Window)
Fl_Window.handle = new_instancemethod(_fltk.Fl_Window_handle,None,Fl_Window)
Fl_Window.resize = new_instancemethod(_fltk.Fl_Window_resize,None,Fl_Window)
Fl_Window.clear_border = new_instancemethod(_fltk.Fl_Window_clear_border,None,Fl_Window)
Fl_Window.border = new_instancemethod(_fltk.Fl_Window_border,None,Fl_Window)
Fl_Window.set_override = new_instancemethod(_fltk.Fl_Window_set_override,None,Fl_Window)
Fl_Window.override = new_instancemethod(_fltk.Fl_Window_override,None,Fl_Window)
Fl_Window.set_modal = new_instancemethod(_fltk.Fl_Window_set_modal,None,Fl_Window)
Fl_Window.modal = new_instancemethod(_fltk.Fl_Window_modal,None,Fl_Window)
Fl_Window.set_non_modal = new_instancemethod(_fltk.Fl_Window_set_non_modal,None,Fl_Window)
Fl_Window.non_modal = new_instancemethod(_fltk.Fl_Window_non_modal,None,Fl_Window)
Fl_Window.hotspot = new_instancemethod(_fltk.Fl_Window_hotspot,None,Fl_Window)
Fl_Window.free_position = new_instancemethod(_fltk.Fl_Window_free_position,None,Fl_Window)
Fl_Window.size_range = new_instancemethod(_fltk.Fl_Window_size_range,None,Fl_Window)
Fl_Window.iconlabel = new_instancemethod(_fltk.Fl_Window_iconlabel,None,Fl_Window)
Fl_Window.label = new_instancemethod(_fltk.Fl_Window_label,None,Fl_Window)
Fl_Window.copy_label = new_instancemethod(_fltk.Fl_Window_copy_label,None,Fl_Window)
Fl_Window.xclass = new_instancemethod(_fltk.Fl_Window_xclass,None,Fl_Window)
Fl_Window.icon = new_instancemethod(_fltk.Fl_Window_icon,None,Fl_Window)
Fl_Window.shown = new_instancemethod(_fltk.Fl_Window_shown,None,Fl_Window)
Fl_Window.hide = new_instancemethod(_fltk.Fl_Window_hide,None,Fl_Window)
Fl_Window.fullscreen = new_instancemethod(_fltk.Fl_Window_fullscreen,None,Fl_Window)
Fl_Window.fullscreen_off = new_instancemethod(_fltk.Fl_Window_fullscreen_off,None,Fl_Window)
Fl_Window.iconize = new_instancemethod(_fltk.Fl_Window_iconize,None,Fl_Window)
Fl_Window.x_root = new_instancemethod(_fltk.Fl_Window_x_root,None,Fl_Window)
Fl_Window.y_root = new_instancemethod(_fltk.Fl_Window_y_root,None,Fl_Window)
Fl_Window.make_current = new_instancemethod(_fltk.Fl_Window_make_current,None,Fl_Window)
Fl_Window.cursor = new_instancemethod(_fltk.Fl_Window_cursor,None,Fl_Window)
Fl_Window.default_cursor = new_instancemethod(_fltk.Fl_Window_default_cursor,None,Fl_Window)
Fl_Window.show = new_instancemethod(_fltk.Fl_Window_show,None,Fl_Window)
_fltk.Fl_Window_swigregister(Fl_Window)

Fl_Window_current = _fltk.Fl_Window_current

Fl_Window_default_callback = _fltk.Fl_Window_default_callback

class Fl_Double_Window(Fl_Window):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Double_Window instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def flush(*args): return _fltk.Fl_Double_Window_flush(*args)
    __swig_destroy__ = _fltk.delete_Fl_Double_Window
    def __init__(self, *args):
        if self.__class__ == Fl_Double_Window:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Double_Window(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def show(*args): return _fltk.Fl_Double_Window_show(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Double_Window(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Double_Window_draw(*args)
Fl_Double_Window.flush = new_instancemethod(_fltk.Fl_Double_Window_flush,None,Fl_Double_Window)
Fl_Double_Window.show = new_instancemethod(_fltk.Fl_Double_Window_show,None,Fl_Double_Window)
Fl_Double_Window.draw = new_instancemethod(_fltk.Fl_Double_Window_draw,None,Fl_Double_Window)
_fltk.Fl_Double_Window_swigregister(Fl_Double_Window)


fl_push_clip = _fltk.fl_push_clip

fl_push_no_clip = _fltk.fl_push_no_clip

fl_pop_clip = _fltk.fl_pop_clip

fl_not_clipped = _fltk.fl_not_clipped

fl_clip_box = _fltk.fl_clip_box

fl_point = _fltk.fl_point

fl_line_style = _fltk.fl_line_style
FL_SOLID = _fltk.FL_SOLID
FL_DASH = _fltk.FL_DASH
FL_DOT = _fltk.FL_DOT
FL_DASHDOT = _fltk.FL_DASHDOT
FL_DASHDOTDOT = _fltk.FL_DASHDOTDOT
FL_CAP_FLAT = _fltk.FL_CAP_FLAT
FL_CAP_ROUND = _fltk.FL_CAP_ROUND
FL_CAP_SQUARE = _fltk.FL_CAP_SQUARE
FL_JOIN_MITER = _fltk.FL_JOIN_MITER
FL_JOIN_ROUND = _fltk.FL_JOIN_ROUND
FL_JOIN_BEVEL = _fltk.FL_JOIN_BEVEL

fl_pie = _fltk.fl_pie

fl_push_matrix = _fltk.fl_push_matrix

fl_pop_matrix = _fltk.fl_pop_matrix

fl_translate = _fltk.fl_translate

fl_rotate = _fltk.fl_rotate

fl_mult_matrix = _fltk.fl_mult_matrix

fl_begin_points = _fltk.fl_begin_points

fl_begin_line = _fltk.fl_begin_line

fl_begin_loop = _fltk.fl_begin_loop

fl_begin_polygon = _fltk.fl_begin_polygon

fl_vertex = _fltk.fl_vertex

fl_curve = _fltk.fl_curve

fl_circle = _fltk.fl_circle

fl_end_points = _fltk.fl_end_points

fl_end_line = _fltk.fl_end_line

fl_end_loop = _fltk.fl_end_loop

fl_end_polygon = _fltk.fl_end_polygon

fl_begin_complex_polygon = _fltk.fl_begin_complex_polygon

fl_gap = _fltk.fl_gap

fl_end_complex_polygon = _fltk.fl_end_complex_polygon

fl_transform_x = _fltk.fl_transform_x

fl_transform_y = _fltk.fl_transform_y

fl_transform_dx = _fltk.fl_transform_dx

fl_transform_dy = _fltk.fl_transform_dy

fl_transformed_vertex = _fltk.fl_transformed_vertex

fl_size = _fltk.fl_size

fl_descent = _fltk.fl_descent

fl_measure = _fltk.fl_measure

fl_frame2 = _fltk.fl_frame2

fl_draw_box = _fltk.fl_draw_box

fl_draw_image = _fltk.fl_draw_image

fl_draw_image_mono = _fltk.fl_draw_image_mono

fl_draw_pixmap = _fltk.fl_draw_pixmap

fl_measure_pixmap = _fltk.fl_measure_pixmap

fl_scroll = _fltk.fl_scroll

fl_shortcut_label = _fltk.fl_shortcut_label

fl_overlay_rect = _fltk.fl_overlay_rect

fl_overlay_clear = _fltk.fl_overlay_clear

fl_cursor = _fltk.fl_cursor

fl_draw_symbol = _fltk.fl_draw_symbol

fl_add_symbol = _fltk.fl_add_symbol
FL_NORMAL_INPUT = _fltk.FL_NORMAL_INPUT
FL_FLOAT_INPUT = _fltk.FL_FLOAT_INPUT
FL_INT_INPUT = _fltk.FL_INT_INPUT
FL_HIDDEN_INPUT = _fltk.FL_HIDDEN_INPUT
FL_MULTILINE_INPUT = _fltk.FL_MULTILINE_INPUT
FL_SECRET_INPUT = _fltk.FL_SECRET_INPUT
FL_INPUT_TYPE = _fltk.FL_INPUT_TYPE
FL_INPUT_READONLY = _fltk.FL_INPUT_READONLY
FL_NORMAL_OUTPUT = _fltk.FL_NORMAL_OUTPUT
FL_MULTILINE_OUTPUT = _fltk.FL_MULTILINE_OUTPUT
FL_INPUT_WRAP = _fltk.FL_INPUT_WRAP
FL_MULTILINE_INPUT_WRAP = _fltk.FL_MULTILINE_INPUT_WRAP
FL_MULTILINE_OUTPUT_WRAP = _fltk.FL_MULTILINE_OUTPUT_WRAP
class Fl_Input_(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Input_ instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Input_:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Input_(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Input_
    def static_value(*args): return _fltk.Fl_Input__static_value(*args)
    def value(*args): return _fltk.Fl_Input__value(*args)
    def index(*args): return _fltk.Fl_Input__index(*args)
    def size(*args): return _fltk.Fl_Input__size(*args)
    def maximum_size(*args): return _fltk.Fl_Input__maximum_size(*args)
    def position(*args): return _fltk.Fl_Input__position(*args)
    def mark(*args): return _fltk.Fl_Input__mark(*args)
    def replace(*args): return _fltk.Fl_Input__replace(*args)
    def cut(*args): return _fltk.Fl_Input__cut(*args)
    def insert(*args): return _fltk.Fl_Input__insert(*args)
    def copy(*args): return _fltk.Fl_Input__copy(*args)
    def undo(*args): return _fltk.Fl_Input__undo(*args)
    def copy_cuts(*args): return _fltk.Fl_Input__copy_cuts(*args)
    def textfont(*args): return _fltk.Fl_Input__textfont(*args)
    def textsize(*args): return _fltk.Fl_Input__textsize(*args)
    def textcolor(*args): return _fltk.Fl_Input__textcolor(*args)
    def cursor_color(*args): return _fltk.Fl_Input__cursor_color(*args)
    def input_type(*args): return _fltk.Fl_Input__input_type(*args)
    def readonly(*args): return _fltk.Fl_Input__readonly(*args)
    def wrap(*args): return _fltk.Fl_Input__wrap(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Input_(self)
        return weakref_proxy(self)
Fl_Input_.static_value = new_instancemethod(_fltk.Fl_Input__static_value,None,Fl_Input_)
Fl_Input_.value = new_instancemethod(_fltk.Fl_Input__value,None,Fl_Input_)
Fl_Input_.index = new_instancemethod(_fltk.Fl_Input__index,None,Fl_Input_)
Fl_Input_.size = new_instancemethod(_fltk.Fl_Input__size,None,Fl_Input_)
Fl_Input_.maximum_size = new_instancemethod(_fltk.Fl_Input__maximum_size,None,Fl_Input_)
Fl_Input_.position = new_instancemethod(_fltk.Fl_Input__position,None,Fl_Input_)
Fl_Input_.mark = new_instancemethod(_fltk.Fl_Input__mark,None,Fl_Input_)
Fl_Input_.replace = new_instancemethod(_fltk.Fl_Input__replace,None,Fl_Input_)
Fl_Input_.cut = new_instancemethod(_fltk.Fl_Input__cut,None,Fl_Input_)
Fl_Input_.insert = new_instancemethod(_fltk.Fl_Input__insert,None,Fl_Input_)
Fl_Input_.copy = new_instancemethod(_fltk.Fl_Input__copy,None,Fl_Input_)
Fl_Input_.undo = new_instancemethod(_fltk.Fl_Input__undo,None,Fl_Input_)
Fl_Input_.copy_cuts = new_instancemethod(_fltk.Fl_Input__copy_cuts,None,Fl_Input_)
Fl_Input_.textfont = new_instancemethod(_fltk.Fl_Input__textfont,None,Fl_Input_)
Fl_Input_.textsize = new_instancemethod(_fltk.Fl_Input__textsize,None,Fl_Input_)
Fl_Input_.textcolor = new_instancemethod(_fltk.Fl_Input__textcolor,None,Fl_Input_)
Fl_Input_.cursor_color = new_instancemethod(_fltk.Fl_Input__cursor_color,None,Fl_Input_)
Fl_Input_.input_type = new_instancemethod(_fltk.Fl_Input__input_type,None,Fl_Input_)
Fl_Input_.readonly = new_instancemethod(_fltk.Fl_Input__readonly,None,Fl_Input_)
Fl_Input_.wrap = new_instancemethod(_fltk.Fl_Input__wrap,None,Fl_Input_)
_fltk.Fl_Input__swigregister(Fl_Input_)

fl_color = _fltk.fl_color

fl_rect = _fltk.fl_rect

fl_line = _fltk.fl_line

fl_loop = _fltk.fl_loop

fl_polygon = _fltk.fl_polygon

fl_xyline = _fltk.fl_xyline

fl_yxline = _fltk.fl_yxline

fl_scale = _fltk.fl_scale

fl_arc = _fltk.fl_arc

fl_font = _fltk.fl_font

fl_height = _fltk.fl_height

fl_width = _fltk.fl_width

fl_draw = _fltk.fl_draw

fl_frame = _fltk.fl_frame

fl_rectf = _fltk.fl_rectf

class Fl_Input(Fl_Input_):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Input instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Input:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Input(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Input
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Input(self)
        return weakref_proxy(self)
_fltk.Fl_Input_swigregister(Fl_Input)

class Fl_File_Input(Fl_Input):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_File_Input instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_File_Input:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_File_Input(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def handle(*args): return _fltk.Fl_File_Input_handle(*args)
    def draw(*args): return _fltk.Fl_File_Input_draw(*args)
    def down_box(*args): return _fltk.Fl_File_Input_down_box(*args)
    def errorcolor(*args): return _fltk.Fl_File_Input_errorcolor(*args)
    def value(*args): return _fltk.Fl_File_Input_value(*args)
    __swig_destroy__ = _fltk.delete_Fl_File_Input
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_File_Input(self)
        return weakref_proxy(self)
Fl_File_Input.handle = new_instancemethod(_fltk.Fl_File_Input_handle,None,Fl_File_Input)
Fl_File_Input.draw = new_instancemethod(_fltk.Fl_File_Input_draw,None,Fl_File_Input)
Fl_File_Input.down_box = new_instancemethod(_fltk.Fl_File_Input_down_box,None,Fl_File_Input)
Fl_File_Input.errorcolor = new_instancemethod(_fltk.Fl_File_Input_errorcolor,None,Fl_File_Input)
Fl_File_Input.value = new_instancemethod(_fltk.Fl_File_Input_value,None,Fl_File_Input)
_fltk.Fl_File_Input_swigregister(Fl_File_Input)

class Fl_Fill_Dial(Fl_Dial):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Fill_Dial instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Fill_Dial:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Fill_Dial(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Fill_Dial
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Fill_Dial(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Fill_Dial_draw(*args)
Fl_Fill_Dial.draw = new_instancemethod(_fltk.Fl_Fill_Dial_draw,None,Fl_Fill_Dial)
_fltk.Fl_Fill_Dial_swigregister(Fl_Fill_Dial)

FL_VERT_SLIDER = _fltk.FL_VERT_SLIDER
FL_HOR_SLIDER = _fltk.FL_HOR_SLIDER
FL_VERT_FILL_SLIDER = _fltk.FL_VERT_FILL_SLIDER
FL_HOR_FILL_SLIDER = _fltk.FL_HOR_FILL_SLIDER
FL_VERT_NICE_SLIDER = _fltk.FL_VERT_NICE_SLIDER
FL_HOR_NICE_SLIDER = _fltk.FL_HOR_NICE_SLIDER
class Fl_Slider(Fl_Valuator):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Slider instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Slider:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Slider(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def scrollvalue(*args): return _fltk.Fl_Slider_scrollvalue(*args)
    def bounds(*args): return _fltk.Fl_Slider_bounds(*args)
    def slider_size(*args): return _fltk.Fl_Slider_slider_size(*args)
    def slider(*args): return _fltk.Fl_Slider_slider(*args)
    __swig_destroy__ = _fltk.delete_Fl_Slider
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Slider(self)
        return weakref_proxy(self)
Fl_Slider.scrollvalue = new_instancemethod(_fltk.Fl_Slider_scrollvalue,None,Fl_Slider)
Fl_Slider.bounds = new_instancemethod(_fltk.Fl_Slider_bounds,None,Fl_Slider)
Fl_Slider.slider_size = new_instancemethod(_fltk.Fl_Slider_slider_size,None,Fl_Slider)
Fl_Slider.slider = new_instancemethod(_fltk.Fl_Slider_slider,None,Fl_Slider)
_fltk.Fl_Slider_swigregister(Fl_Slider)

class Fl_Fill_Slider(Fl_Slider):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Fill_Slider instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Fill_Slider:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Fill_Slider(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Fill_Slider
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Fill_Slider(self)
        return weakref_proxy(self)
_fltk.Fl_Fill_Slider_swigregister(Fl_Fill_Slider)

class Fl_Float_Input(Fl_Input):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Float_Input instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Float_Input:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Float_Input(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Float_Input
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Float_Input(self)
        return weakref_proxy(self)
_fltk.Fl_Float_Input_swigregister(Fl_Float_Input)

class Fl_FormsBitmap(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_FormsBitmap instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_FormsBitmap_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_FormsBitmap:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_FormsBitmap(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def set(*args): return _fltk.Fl_FormsBitmap_set(*args)
    def bitmap(*args): return _fltk.Fl_FormsBitmap_bitmap(*args)
    __swig_destroy__ = _fltk.delete_Fl_FormsBitmap
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_FormsBitmap(self)
        return weakref_proxy(self)
Fl_FormsBitmap.draw = new_instancemethod(_fltk.Fl_FormsBitmap_draw,None,Fl_FormsBitmap)
Fl_FormsBitmap.set = new_instancemethod(_fltk.Fl_FormsBitmap_set,None,Fl_FormsBitmap)
Fl_FormsBitmap.bitmap = new_instancemethod(_fltk.Fl_FormsBitmap_bitmap,None,Fl_FormsBitmap)
_fltk.Fl_FormsBitmap_swigregister(Fl_FormsBitmap)

class Fl_FormsPixmap(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_FormsPixmap instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_FormsPixmap_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_FormsPixmap:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_FormsPixmap(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def set(*args): return _fltk.Fl_FormsPixmap_set(*args)
    def Pixmap(*args): return _fltk.Fl_FormsPixmap_Pixmap(*args)
    __swig_destroy__ = _fltk.delete_Fl_FormsPixmap
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_FormsPixmap(self)
        return weakref_proxy(self)
Fl_FormsPixmap.draw = new_instancemethod(_fltk.Fl_FormsPixmap_draw,None,Fl_FormsPixmap)
Fl_FormsPixmap.set = new_instancemethod(_fltk.Fl_FormsPixmap_set,None,Fl_FormsPixmap)
Fl_FormsPixmap.Pixmap = new_instancemethod(_fltk.Fl_FormsPixmap_Pixmap,None,Fl_FormsPixmap)
_fltk.Fl_FormsPixmap_swigregister(Fl_FormsPixmap)

FL_NORMAL_FREE = _fltk.FL_NORMAL_FREE
FL_SLEEPING_FREE = _fltk.FL_SLEEPING_FREE
FL_INPUT_FREE = _fltk.FL_INPUT_FREE
FL_CONTINUOUS_FREE = _fltk.FL_CONTINUOUS_FREE
FL_ALL_FREE = _fltk.FL_ALL_FREE
class Fl_Free(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Free instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Free_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Free:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Free(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Free
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Free(self)
        return weakref_proxy(self)
Fl_Free.draw = new_instancemethod(_fltk.Fl_Free_draw,None,Fl_Free)
_fltk.Fl_Free_swigregister(Fl_Free)

FL_DRAW = _fltk.FL_DRAW
FL_STEP = _fltk.FL_STEP
FL_FREEMEM = _fltk.FL_FREEMEM
FL_FREEZE = _fltk.FL_FREEZE
FL_THAW = _fltk.FL_THAW
class Fl_Pixmap(Fl_Image):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Pixmap instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    alloc_data = property(_fltk.Fl_Pixmap_alloc_data_get, _fltk.Fl_Pixmap_alloc_data_set)
    def __init__(self, *args):
        if self.__class__ == Fl_Pixmap:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Pixmap(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Pixmap
    def copy(*args): return _fltk.Fl_Pixmap_copy(*args)
    def color_average(*args): return _fltk.Fl_Pixmap_color_average(*args)
    def desaturate(*args): return _fltk.Fl_Pixmap_desaturate(*args)
    def draw(*args): return _fltk.Fl_Pixmap_draw(*args)
    def label(*args): return _fltk.Fl_Pixmap_label(*args)
    def uncache(*args): return _fltk.Fl_Pixmap_uncache(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Pixmap(self)
        return weakref_proxy(self)
Fl_Pixmap.copy = new_instancemethod(_fltk.Fl_Pixmap_copy,None,Fl_Pixmap)
Fl_Pixmap.color_average = new_instancemethod(_fltk.Fl_Pixmap_color_average,None,Fl_Pixmap)
Fl_Pixmap.desaturate = new_instancemethod(_fltk.Fl_Pixmap_desaturate,None,Fl_Pixmap)
Fl_Pixmap.draw = new_instancemethod(_fltk.Fl_Pixmap_draw,None,Fl_Pixmap)
Fl_Pixmap.label = new_instancemethod(_fltk.Fl_Pixmap_label,None,Fl_Pixmap)
Fl_Pixmap.uncache = new_instancemethod(_fltk.Fl_Pixmap_uncache,None,Fl_Pixmap)
_fltk.Fl_Pixmap_swigregister(Fl_Pixmap)

class Fl_GIF_Image(Fl_Pixmap):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_GIF_Image instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_GIF_Image:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_GIF_Image(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_GIF_Image
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_GIF_Image(self)
        return weakref_proxy(self)
_fltk.Fl_GIF_Image_swigregister(Fl_GIF_Image)

class Fl_Gl_Window(Fl_Window):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Gl_Window instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def flush(*args): return _fltk.Fl_Gl_Window_flush(*args)
    def valid(*args): return _fltk.Fl_Gl_Window_valid(*args)
    def invalidate(*args): return _fltk.Fl_Gl_Window_invalidate(*args)
    def can_do(*args): return _fltk.Fl_Gl_Window_can_do(*args)
    def mode(*args): return _fltk.Fl_Gl_Window_mode(*args)
    def context(*args): return _fltk.Fl_Gl_Window_context(*args)
    def make_current(*args): return _fltk.Fl_Gl_Window_make_current(*args)
    def swap_buffers(*args): return _fltk.Fl_Gl_Window_swap_buffers(*args)
    def ortho(*args): return _fltk.Fl_Gl_Window_ortho(*args)
    def can_do_overlay(*args): return _fltk.Fl_Gl_Window_can_do_overlay(*args)
    def redraw_overlay(*args): return _fltk.Fl_Gl_Window_redraw_overlay(*args)
    def hide_overlay(*args): return _fltk.Fl_Gl_Window_hide_overlay(*args)
    def make_overlay_current(*args): return _fltk.Fl_Gl_Window_make_overlay_current(*args)
    __swig_destroy__ = _fltk.delete_Fl_Gl_Window
    def __init__(self, *args):
        if self.__class__ == Fl_Gl_Window:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Gl_Window(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def show(*args): return _fltk.Fl_Gl_Window_show(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Gl_Window(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Gl_Window_draw(*args)
Fl_Gl_Window.flush = new_instancemethod(_fltk.Fl_Gl_Window_flush,None,Fl_Gl_Window)
Fl_Gl_Window.valid = new_instancemethod(_fltk.Fl_Gl_Window_valid,None,Fl_Gl_Window)
Fl_Gl_Window.invalidate = new_instancemethod(_fltk.Fl_Gl_Window_invalidate,None,Fl_Gl_Window)
Fl_Gl_Window.can_do = new_instancemethod(_fltk.Fl_Gl_Window_can_do,None,Fl_Gl_Window)
Fl_Gl_Window.mode = new_instancemethod(_fltk.Fl_Gl_Window_mode,None,Fl_Gl_Window)
Fl_Gl_Window.context = new_instancemethod(_fltk.Fl_Gl_Window_context,None,Fl_Gl_Window)
Fl_Gl_Window.make_current = new_instancemethod(_fltk.Fl_Gl_Window_make_current,None,Fl_Gl_Window)
Fl_Gl_Window.swap_buffers = new_instancemethod(_fltk.Fl_Gl_Window_swap_buffers,None,Fl_Gl_Window)
Fl_Gl_Window.ortho = new_instancemethod(_fltk.Fl_Gl_Window_ortho,None,Fl_Gl_Window)
Fl_Gl_Window.can_do_overlay = new_instancemethod(_fltk.Fl_Gl_Window_can_do_overlay,None,Fl_Gl_Window)
Fl_Gl_Window.redraw_overlay = new_instancemethod(_fltk.Fl_Gl_Window_redraw_overlay,None,Fl_Gl_Window)
Fl_Gl_Window.hide_overlay = new_instancemethod(_fltk.Fl_Gl_Window_hide_overlay,None,Fl_Gl_Window)
Fl_Gl_Window.make_overlay_current = new_instancemethod(_fltk.Fl_Gl_Window_make_overlay_current,None,Fl_Gl_Window)
Fl_Gl_Window.show = new_instancemethod(_fltk.Fl_Gl_Window_show,None,Fl_Gl_Window)
Fl_Gl_Window.draw = new_instancemethod(_fltk.Fl_Gl_Window_draw,None,Fl_Gl_Window)
_fltk.Fl_Gl_Window_swigregister(Fl_Gl_Window)

class Fl_Help_Dialog(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Help_Dialog instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        this = _fltk.new_Fl_Help_Dialog(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Help_Dialog
    def h(*args): return _fltk.Fl_Help_Dialog_h(*args)
    def hide(*args): return _fltk.Fl_Help_Dialog_hide(*args)
    def load(*args): return _fltk.Fl_Help_Dialog_load(*args)
    def position(*args): return _fltk.Fl_Help_Dialog_position(*args)
    def resize(*args): return _fltk.Fl_Help_Dialog_resize(*args)
    def show(*args): return _fltk.Fl_Help_Dialog_show(*args)
    def textsize(*args): return _fltk.Fl_Help_Dialog_textsize(*args)
    def topline(*args): return _fltk.Fl_Help_Dialog_topline(*args)
    def value(*args): return _fltk.Fl_Help_Dialog_value(*args)
    def visible(*args): return _fltk.Fl_Help_Dialog_visible(*args)
    def w(*args): return _fltk.Fl_Help_Dialog_w(*args)
    def x(*args): return _fltk.Fl_Help_Dialog_x(*args)
    def y(*args): return _fltk.Fl_Help_Dialog_y(*args)
Fl_Help_Dialog.h = new_instancemethod(_fltk.Fl_Help_Dialog_h,None,Fl_Help_Dialog)
Fl_Help_Dialog.hide = new_instancemethod(_fltk.Fl_Help_Dialog_hide,None,Fl_Help_Dialog)
Fl_Help_Dialog.load = new_instancemethod(_fltk.Fl_Help_Dialog_load,None,Fl_Help_Dialog)
Fl_Help_Dialog.position = new_instancemethod(_fltk.Fl_Help_Dialog_position,None,Fl_Help_Dialog)
Fl_Help_Dialog.resize = new_instancemethod(_fltk.Fl_Help_Dialog_resize,None,Fl_Help_Dialog)
Fl_Help_Dialog.show = new_instancemethod(_fltk.Fl_Help_Dialog_show,None,Fl_Help_Dialog)
Fl_Help_Dialog.textsize = new_instancemethod(_fltk.Fl_Help_Dialog_textsize,None,Fl_Help_Dialog)
Fl_Help_Dialog.topline = new_instancemethod(_fltk.Fl_Help_Dialog_topline,None,Fl_Help_Dialog)
Fl_Help_Dialog.value = new_instancemethod(_fltk.Fl_Help_Dialog_value,None,Fl_Help_Dialog)
Fl_Help_Dialog.visible = new_instancemethod(_fltk.Fl_Help_Dialog_visible,None,Fl_Help_Dialog)
Fl_Help_Dialog.w = new_instancemethod(_fltk.Fl_Help_Dialog_w,None,Fl_Help_Dialog)
Fl_Help_Dialog.x = new_instancemethod(_fltk.Fl_Help_Dialog_x,None,Fl_Help_Dialog)
Fl_Help_Dialog.y = new_instancemethod(_fltk.Fl_Help_Dialog_y,None,Fl_Help_Dialog)
_fltk.Fl_Help_Dialog_swigregister(Fl_Help_Dialog)

class Fl_Help_Block(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Help_Block instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    start = property(_fltk.Fl_Help_Block_start_get, _fltk.Fl_Help_Block_start_set)
    end = property(_fltk.Fl_Help_Block_end_get, _fltk.Fl_Help_Block_end_set)
    border = property(_fltk.Fl_Help_Block_border_get, _fltk.Fl_Help_Block_border_set)
    bgcolor = property(_fltk.Fl_Help_Block_bgcolor_get, _fltk.Fl_Help_Block_bgcolor_set)
    x = property(_fltk.Fl_Help_Block_x_get, _fltk.Fl_Help_Block_x_set)
    y = property(_fltk.Fl_Help_Block_y_get, _fltk.Fl_Help_Block_y_set)
    w = property(_fltk.Fl_Help_Block_w_get, _fltk.Fl_Help_Block_w_set)
    h = property(_fltk.Fl_Help_Block_h_get, _fltk.Fl_Help_Block_h_set)
    line = property(_fltk.Fl_Help_Block_line_get, _fltk.Fl_Help_Block_line_set)
    def __init__(self, *args):
        this = _fltk.new_Fl_Help_Block(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Help_Block
_fltk.Fl_Help_Block_swigregister(Fl_Help_Block)

class Fl_Help_Link(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Help_Link instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    filename = property(_fltk.Fl_Help_Link_filename_get, _fltk.Fl_Help_Link_filename_set)
    name = property(_fltk.Fl_Help_Link_name_get, _fltk.Fl_Help_Link_name_set)
    x = property(_fltk.Fl_Help_Link_x_get, _fltk.Fl_Help_Link_x_set)
    y = property(_fltk.Fl_Help_Link_y_get, _fltk.Fl_Help_Link_y_set)
    w = property(_fltk.Fl_Help_Link_w_get, _fltk.Fl_Help_Link_w_set)
    h = property(_fltk.Fl_Help_Link_h_get, _fltk.Fl_Help_Link_h_set)
    def __init__(self, *args):
        this = _fltk.new_Fl_Help_Link(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Help_Link
_fltk.Fl_Help_Link_swigregister(Fl_Help_Link)

class Fl_Help_Target(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Help_Target instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    name = property(_fltk.Fl_Help_Target_name_get, _fltk.Fl_Help_Target_name_set)
    y = property(_fltk.Fl_Help_Target_y_get, _fltk.Fl_Help_Target_y_set)
    def __init__(self, *args):
        this = _fltk.new_Fl_Help_Target(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Help_Target
_fltk.Fl_Help_Target_swigregister(Fl_Help_Target)

class Fl_Help_View(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Help_View instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Help_View:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Help_View(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Help_View
    def directory(*args): return _fltk.Fl_Help_View_directory(*args)
    def filename(*args): return _fltk.Fl_Help_View_filename(*args)
    def find(*args): return _fltk.Fl_Help_View_find(*args)
    def load(*args): return _fltk.Fl_Help_View_load(*args)
    def size(*args): return _fltk.Fl_Help_View_size(*args)
    def textcolor(*args): return _fltk.Fl_Help_View_textcolor(*args)
    def textfont(*args): return _fltk.Fl_Help_View_textfont(*args)
    def textsize(*args): return _fltk.Fl_Help_View_textsize(*args)
    def title(*args): return _fltk.Fl_Help_View_title(*args)
    def topline(*args): return _fltk.Fl_Help_View_topline(*args)
    def leftline(*args): return _fltk.Fl_Help_View_leftline(*args)
    def value(*args): return _fltk.Fl_Help_View_value(*args)
    def link(*args): return _fltk.Fl_Help_View_link(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Help_View(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Help_View_draw(*args)
Fl_Help_View.directory = new_instancemethod(_fltk.Fl_Help_View_directory,None,Fl_Help_View)
Fl_Help_View.filename = new_instancemethod(_fltk.Fl_Help_View_filename,None,Fl_Help_View)
Fl_Help_View.find = new_instancemethod(_fltk.Fl_Help_View_find,None,Fl_Help_View)
Fl_Help_View.load = new_instancemethod(_fltk.Fl_Help_View_load,None,Fl_Help_View)
Fl_Help_View.size = new_instancemethod(_fltk.Fl_Help_View_size,None,Fl_Help_View)
Fl_Help_View.textcolor = new_instancemethod(_fltk.Fl_Help_View_textcolor,None,Fl_Help_View)
Fl_Help_View.textfont = new_instancemethod(_fltk.Fl_Help_View_textfont,None,Fl_Help_View)
Fl_Help_View.textsize = new_instancemethod(_fltk.Fl_Help_View_textsize,None,Fl_Help_View)
Fl_Help_View.title = new_instancemethod(_fltk.Fl_Help_View_title,None,Fl_Help_View)
Fl_Help_View.topline = new_instancemethod(_fltk.Fl_Help_View_topline,None,Fl_Help_View)
Fl_Help_View.leftline = new_instancemethod(_fltk.Fl_Help_View_leftline,None,Fl_Help_View)
Fl_Help_View.value = new_instancemethod(_fltk.Fl_Help_View_value,None,Fl_Help_View)
Fl_Help_View.link = new_instancemethod(_fltk.Fl_Help_View_link,None,Fl_Help_View)
Fl_Help_View.draw = new_instancemethod(_fltk.Fl_Help_View_draw,None,Fl_Help_View)
_fltk.Fl_Help_View_swigregister(Fl_Help_View)

class Fl_Hold_Browser(Fl_Browser):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Hold_Browser instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Hold_Browser:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Hold_Browser(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Hold_Browser
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Hold_Browser(self)
        return weakref_proxy(self)
    def item_first(*args): return _fltk.Fl_Hold_Browser_item_first(*args)
    def item_next(*args): return _fltk.Fl_Hold_Browser_item_next(*args)
    def item_prev(*args): return _fltk.Fl_Hold_Browser_item_prev(*args)
    def full_width(*args): return _fltk.Fl_Hold_Browser_full_width(*args)
    def item_select(*args): return _fltk.Fl_Hold_Browser_item_select(*args)
    def item_draw(*args): return _fltk.Fl_Hold_Browser_item_draw(*args)
    def full_height(*args): return _fltk.Fl_Hold_Browser_full_height(*args)
    def incr_height(*args): return _fltk.Fl_Hold_Browser_incr_height(*args)
    def draw(*args): return _fltk.Fl_Hold_Browser_draw(*args)
    def item_quick_height(*args): return _fltk.Fl_Hold_Browser_item_quick_height(*args)
    def item_selected(*args): return _fltk.Fl_Hold_Browser_item_selected(*args)
    def item_height(*args): return _fltk.Fl_Hold_Browser_item_height(*args)
    def item_width(*args): return _fltk.Fl_Hold_Browser_item_width(*args)
Fl_Hold_Browser.item_first = new_instancemethod(_fltk.Fl_Hold_Browser_item_first,None,Fl_Hold_Browser)
Fl_Hold_Browser.item_next = new_instancemethod(_fltk.Fl_Hold_Browser_item_next,None,Fl_Hold_Browser)
Fl_Hold_Browser.item_prev = new_instancemethod(_fltk.Fl_Hold_Browser_item_prev,None,Fl_Hold_Browser)
Fl_Hold_Browser.full_width = new_instancemethod(_fltk.Fl_Hold_Browser_full_width,None,Fl_Hold_Browser)
Fl_Hold_Browser.item_select = new_instancemethod(_fltk.Fl_Hold_Browser_item_select,None,Fl_Hold_Browser)
Fl_Hold_Browser.item_draw = new_instancemethod(_fltk.Fl_Hold_Browser_item_draw,None,Fl_Hold_Browser)
Fl_Hold_Browser.full_height = new_instancemethod(_fltk.Fl_Hold_Browser_full_height,None,Fl_Hold_Browser)
Fl_Hold_Browser.incr_height = new_instancemethod(_fltk.Fl_Hold_Browser_incr_height,None,Fl_Hold_Browser)
Fl_Hold_Browser.draw = new_instancemethod(_fltk.Fl_Hold_Browser_draw,None,Fl_Hold_Browser)
Fl_Hold_Browser.item_quick_height = new_instancemethod(_fltk.Fl_Hold_Browser_item_quick_height,None,Fl_Hold_Browser)
Fl_Hold_Browser.item_selected = new_instancemethod(_fltk.Fl_Hold_Browser_item_selected,None,Fl_Hold_Browser)
Fl_Hold_Browser.item_height = new_instancemethod(_fltk.Fl_Hold_Browser_item_height,None,Fl_Hold_Browser)
Fl_Hold_Browser.item_width = new_instancemethod(_fltk.Fl_Hold_Browser_item_width,None,Fl_Hold_Browser)
_fltk.Fl_Hold_Browser_swigregister(Fl_Hold_Browser)

class Fl_Hor_Fill_Slider(Fl_Slider):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Hor_Fill_Slider instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Hor_Fill_Slider:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Hor_Fill_Slider(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Hor_Fill_Slider
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Hor_Fill_Slider(self)
        return weakref_proxy(self)
_fltk.Fl_Hor_Fill_Slider_swigregister(Fl_Hor_Fill_Slider)

class Fl_Hor_Nice_Slider(Fl_Slider):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Hor_Nice_Slider instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Hor_Nice_Slider:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Hor_Nice_Slider(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Hor_Nice_Slider
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Hor_Nice_Slider(self)
        return weakref_proxy(self)
_fltk.Fl_Hor_Nice_Slider_swigregister(Fl_Hor_Nice_Slider)

class Fl_Hor_Slider(Fl_Slider):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Hor_Slider instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Hor_Slider:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Hor_Slider(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Hor_Slider
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Hor_Slider(self)
        return weakref_proxy(self)
_fltk.Fl_Hor_Slider_swigregister(Fl_Hor_Slider)

class Fl_Value_Slider(Fl_Slider):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Value_Slider instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Value_Slider:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Value_Slider(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def textfont(*args): return _fltk.Fl_Value_Slider_textfont(*args)
    def textsize(*args): return _fltk.Fl_Value_Slider_textsize(*args)
    def textcolor(*args): return _fltk.Fl_Value_Slider_textcolor(*args)
    __swig_destroy__ = _fltk.delete_Fl_Value_Slider
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Value_Slider(self)
        return weakref_proxy(self)
Fl_Value_Slider.textfont = new_instancemethod(_fltk.Fl_Value_Slider_textfont,None,Fl_Value_Slider)
Fl_Value_Slider.textsize = new_instancemethod(_fltk.Fl_Value_Slider_textsize,None,Fl_Value_Slider)
Fl_Value_Slider.textcolor = new_instancemethod(_fltk.Fl_Value_Slider_textcolor,None,Fl_Value_Slider)
_fltk.Fl_Value_Slider_swigregister(Fl_Value_Slider)

class Fl_Hor_Value_Slider(Fl_Value_Slider):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Hor_Value_Slider instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Hor_Value_Slider:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Hor_Value_Slider(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Hor_Value_Slider
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Hor_Value_Slider(self)
        return weakref_proxy(self)
_fltk.Fl_Hor_Value_Slider_swigregister(Fl_Hor_Value_Slider)

class Fl_Int_Input(Fl_Input):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Int_Input instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Int_Input:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Int_Input(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Int_Input
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Int_Input(self)
        return weakref_proxy(self)
_fltk.Fl_Int_Input_swigregister(Fl_Int_Input)

class Fl_Input_Choice(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Input_Choice instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Input_Choice:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Input_Choice(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def add(*args): return _fltk.Fl_Input_Choice_add(*args)
    def clear(*args): return _fltk.Fl_Input_Choice_clear(*args)
    def down_box(*args): return _fltk.Fl_Input_Choice_down_box(*args)
    def menu(*args): return _fltk.Fl_Input_Choice_menu(*args)
    def textcolor(*args): return _fltk.Fl_Input_Choice_textcolor(*args)
    def textfont(*args): return _fltk.Fl_Input_Choice_textfont(*args)
    def textsize(*args): return _fltk.Fl_Input_Choice_textsize(*args)
    def value(*args): return _fltk.Fl_Input_Choice_value(*args)
    def menubutton(*args): return _fltk.Fl_Input_Choice_menubutton(*args)
    def input(*args): return _fltk.Fl_Input_Choice_input(*args)
    __swig_destroy__ = _fltk.delete_Fl_Input_Choice
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Input_Choice(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Input_Choice_draw(*args)
Fl_Input_Choice.add = new_instancemethod(_fltk.Fl_Input_Choice_add,None,Fl_Input_Choice)
Fl_Input_Choice.clear = new_instancemethod(_fltk.Fl_Input_Choice_clear,None,Fl_Input_Choice)
Fl_Input_Choice.down_box = new_instancemethod(_fltk.Fl_Input_Choice_down_box,None,Fl_Input_Choice)
Fl_Input_Choice.menu = new_instancemethod(_fltk.Fl_Input_Choice_menu,None,Fl_Input_Choice)
Fl_Input_Choice.textcolor = new_instancemethod(_fltk.Fl_Input_Choice_textcolor,None,Fl_Input_Choice)
Fl_Input_Choice.textfont = new_instancemethod(_fltk.Fl_Input_Choice_textfont,None,Fl_Input_Choice)
Fl_Input_Choice.textsize = new_instancemethod(_fltk.Fl_Input_Choice_textsize,None,Fl_Input_Choice)
Fl_Input_Choice.value = new_instancemethod(_fltk.Fl_Input_Choice_value,None,Fl_Input_Choice)
Fl_Input_Choice.menubutton = new_instancemethod(_fltk.Fl_Input_Choice_menubutton,None,Fl_Input_Choice)
Fl_Input_Choice.input = new_instancemethod(_fltk.Fl_Input_Choice_input,None,Fl_Input_Choice)
Fl_Input_Choice.draw = new_instancemethod(_fltk.Fl_Input_Choice_draw,None,Fl_Input_Choice)
_fltk.Fl_Input_Choice_swigregister(Fl_Input_Choice)

class Fl_JPEG_Image(Fl_RGB_Image):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_JPEG_Image instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_JPEG_Image:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_JPEG_Image(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_JPEG_Image
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_JPEG_Image(self)
        return weakref_proxy(self)
_fltk.Fl_JPEG_Image_swigregister(Fl_JPEG_Image)

class Fl_Line_Dial(Fl_Dial):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Line_Dial instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Line_Dial:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Line_Dial(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Line_Dial
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Line_Dial(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Line_Dial_draw(*args)
Fl_Line_Dial.draw = new_instancemethod(_fltk.Fl_Line_Dial_draw,None,Fl_Line_Dial)
_fltk.Fl_Line_Dial_swigregister(Fl_Line_Dial)

class Fl_Menu_Bar(Fl_Menu_):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Menu_Bar instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Menu_Bar_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Menu_Bar:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Menu_Bar(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Menu_Bar
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Menu_Bar(self)
        return weakref_proxy(self)
Fl_Menu_Bar.draw = new_instancemethod(_fltk.Fl_Menu_Bar_draw,None,Fl_Menu_Bar)
_fltk.Fl_Menu_Bar_swigregister(Fl_Menu_Bar)

class Fl_Menu_Button(Fl_Menu_):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Menu_Button instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Menu_Button_draw(*args)
    POPUP1 = _fltk.Fl_Menu_Button_POPUP1
    POPUP2 = _fltk.Fl_Menu_Button_POPUP2
    POPUP12 = _fltk.Fl_Menu_Button_POPUP12
    POPUP3 = _fltk.Fl_Menu_Button_POPUP3
    POPUP13 = _fltk.Fl_Menu_Button_POPUP13
    POPUP23 = _fltk.Fl_Menu_Button_POPUP23
    POPUP123 = _fltk.Fl_Menu_Button_POPUP123
    def popup(*args): return _fltk.Fl_Menu_Button_popup(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Menu_Button:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Menu_Button(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Menu_Button
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Menu_Button(self)
        return weakref_proxy(self)
Fl_Menu_Button.draw = new_instancemethod(_fltk.Fl_Menu_Button_draw,None,Fl_Menu_Button)
Fl_Menu_Button.popup = new_instancemethod(_fltk.Fl_Menu_Button_popup,None,Fl_Menu_Button)
_fltk.Fl_Menu_Button_swigregister(Fl_Menu_Button)

FL_MENU_INACTIVE = _fltk.FL_MENU_INACTIVE
FL_MENU_TOGGLE = _fltk.FL_MENU_TOGGLE
FL_MENU_VALUE = _fltk.FL_MENU_VALUE
FL_MENU_RADIO = _fltk.FL_MENU_RADIO
FL_MENU_INVISIBLE = _fltk.FL_MENU_INVISIBLE
FL_SUBMENU_POINTER = _fltk.FL_SUBMENU_POINTER
FL_SUBMENU = _fltk.FL_SUBMENU
FL_MENU_DIVIDER = _fltk.FL_MENU_DIVIDER
FL_MENU_HORIZONTAL = _fltk.FL_MENU_HORIZONTAL
class Fl_Menu_Item(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Menu_Item instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    text = property(_fltk.Fl_Menu_Item_text_get, _fltk.Fl_Menu_Item_text_set)
    shortcut_ = property(_fltk.Fl_Menu_Item_shortcut__get, _fltk.Fl_Menu_Item_shortcut__set)
    callback_ = property(_fltk.Fl_Menu_Item_callback__get, _fltk.Fl_Menu_Item_callback__set)
    user_data_ = property(_fltk.Fl_Menu_Item_user_data__get, _fltk.Fl_Menu_Item_user_data__set)
    flags = property(_fltk.Fl_Menu_Item_flags_get, _fltk.Fl_Menu_Item_flags_set)
    labeltype_ = property(_fltk.Fl_Menu_Item_labeltype__get, _fltk.Fl_Menu_Item_labeltype__set)
    labelfont_ = property(_fltk.Fl_Menu_Item_labelfont__get, _fltk.Fl_Menu_Item_labelfont__set)
    labelsize_ = property(_fltk.Fl_Menu_Item_labelsize__get, _fltk.Fl_Menu_Item_labelsize__set)
    labelcolor_ = property(_fltk.Fl_Menu_Item_labelcolor__get, _fltk.Fl_Menu_Item_labelcolor__set)
    def next(*args): return _fltk.Fl_Menu_Item_next(*args)
    def first(*args): return _fltk.Fl_Menu_Item_first(*args)
    def label(*args): return _fltk.Fl_Menu_Item_label(*args)
    def labeltype(*args): return _fltk.Fl_Menu_Item_labeltype(*args)
    def labelcolor(*args): return _fltk.Fl_Menu_Item_labelcolor(*args)
    def labelfont(*args): return _fltk.Fl_Menu_Item_labelfont(*args)
    def labelsize(*args): return _fltk.Fl_Menu_Item_labelsize(*args)
    def argument(*args): return _fltk.Fl_Menu_Item_argument(*args)
    def shortcut(*args): return _fltk.Fl_Menu_Item_shortcut(*args)
    def submenu(*args): return _fltk.Fl_Menu_Item_submenu(*args)
    def checkbox(*args): return _fltk.Fl_Menu_Item_checkbox(*args)
    def radio(*args): return _fltk.Fl_Menu_Item_radio(*args)
    def value(*args): return _fltk.Fl_Menu_Item_value(*args)
    def set(*args): return _fltk.Fl_Menu_Item_set(*args)
    def clear(*args): return _fltk.Fl_Menu_Item_clear(*args)
    def setonly(*args): return _fltk.Fl_Menu_Item_setonly(*args)
    def visible(*args): return _fltk.Fl_Menu_Item_visible(*args)
    def show(*args): return _fltk.Fl_Menu_Item_show(*args)
    def hide(*args): return _fltk.Fl_Menu_Item_hide(*args)
    def active(*args): return _fltk.Fl_Menu_Item_active(*args)
    def activate(*args): return _fltk.Fl_Menu_Item_activate(*args)
    def deactivate(*args): return _fltk.Fl_Menu_Item_deactivate(*args)
    def activevisible(*args): return _fltk.Fl_Menu_Item_activevisible(*args)
    def image(*args): return _fltk.Fl_Menu_Item_image(*args)
    def measure(*args): return _fltk.Fl_Menu_Item_measure(*args)
    def draw(*args): return _fltk.Fl_Menu_Item_draw(*args)
    def popup(*args): return _fltk.Fl_Menu_Item_popup(*args)
    def pulldown(*args): return _fltk.Fl_Menu_Item_pulldown(*args)
    def test_shortcut(*args): return _fltk.Fl_Menu_Item_test_shortcut(*args)
    def find_shortcut(*args): return _fltk.Fl_Menu_Item_find_shortcut(*args)
    def do_callback(*args): return _fltk.Fl_Menu_Item_do_callback(*args)
    def checked(*args): return _fltk.Fl_Menu_Item_checked(*args)
    def check(*args): return _fltk.Fl_Menu_Item_check(*args)
    def uncheck(*args): return _fltk.Fl_Menu_Item_uncheck(*args)
    def add(*args): return _fltk.Fl_Menu_Item_add(*args)
    def size(*args): return _fltk.Fl_Menu_Item_size(*args)
    def callback(*args): return _fltk.Fl_Menu_Item_callback(*args)
    def user_data(*args): return _fltk.Fl_Menu_Item_user_data(*args)
    def __init__(self, *args):
        this = _fltk.new_Fl_Menu_Item(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Menu_Item
Fl_Menu_Item.next = new_instancemethod(_fltk.Fl_Menu_Item_next,None,Fl_Menu_Item)
Fl_Menu_Item.first = new_instancemethod(_fltk.Fl_Menu_Item_first,None,Fl_Menu_Item)
Fl_Menu_Item.label = new_instancemethod(_fltk.Fl_Menu_Item_label,None,Fl_Menu_Item)
Fl_Menu_Item.labeltype = new_instancemethod(_fltk.Fl_Menu_Item_labeltype,None,Fl_Menu_Item)
Fl_Menu_Item.labelcolor = new_instancemethod(_fltk.Fl_Menu_Item_labelcolor,None,Fl_Menu_Item)
Fl_Menu_Item.labelfont = new_instancemethod(_fltk.Fl_Menu_Item_labelfont,None,Fl_Menu_Item)
Fl_Menu_Item.labelsize = new_instancemethod(_fltk.Fl_Menu_Item_labelsize,None,Fl_Menu_Item)
Fl_Menu_Item.argument = new_instancemethod(_fltk.Fl_Menu_Item_argument,None,Fl_Menu_Item)
Fl_Menu_Item.shortcut = new_instancemethod(_fltk.Fl_Menu_Item_shortcut,None,Fl_Menu_Item)
Fl_Menu_Item.submenu = new_instancemethod(_fltk.Fl_Menu_Item_submenu,None,Fl_Menu_Item)
Fl_Menu_Item.checkbox = new_instancemethod(_fltk.Fl_Menu_Item_checkbox,None,Fl_Menu_Item)
Fl_Menu_Item.radio = new_instancemethod(_fltk.Fl_Menu_Item_radio,None,Fl_Menu_Item)
Fl_Menu_Item.value = new_instancemethod(_fltk.Fl_Menu_Item_value,None,Fl_Menu_Item)
Fl_Menu_Item.set = new_instancemethod(_fltk.Fl_Menu_Item_set,None,Fl_Menu_Item)
Fl_Menu_Item.clear = new_instancemethod(_fltk.Fl_Menu_Item_clear,None,Fl_Menu_Item)
Fl_Menu_Item.setonly = new_instancemethod(_fltk.Fl_Menu_Item_setonly,None,Fl_Menu_Item)
Fl_Menu_Item.visible = new_instancemethod(_fltk.Fl_Menu_Item_visible,None,Fl_Menu_Item)
Fl_Menu_Item.show = new_instancemethod(_fltk.Fl_Menu_Item_show,None,Fl_Menu_Item)
Fl_Menu_Item.hide = new_instancemethod(_fltk.Fl_Menu_Item_hide,None,Fl_Menu_Item)
Fl_Menu_Item.active = new_instancemethod(_fltk.Fl_Menu_Item_active,None,Fl_Menu_Item)
Fl_Menu_Item.activate = new_instancemethod(_fltk.Fl_Menu_Item_activate,None,Fl_Menu_Item)
Fl_Menu_Item.deactivate = new_instancemethod(_fltk.Fl_Menu_Item_deactivate,None,Fl_Menu_Item)
Fl_Menu_Item.activevisible = new_instancemethod(_fltk.Fl_Menu_Item_activevisible,None,Fl_Menu_Item)
Fl_Menu_Item.image = new_instancemethod(_fltk.Fl_Menu_Item_image,None,Fl_Menu_Item)
Fl_Menu_Item.measure = new_instancemethod(_fltk.Fl_Menu_Item_measure,None,Fl_Menu_Item)
Fl_Menu_Item.draw = new_instancemethod(_fltk.Fl_Menu_Item_draw,None,Fl_Menu_Item)
Fl_Menu_Item.popup = new_instancemethod(_fltk.Fl_Menu_Item_popup,None,Fl_Menu_Item)
Fl_Menu_Item.pulldown = new_instancemethod(_fltk.Fl_Menu_Item_pulldown,None,Fl_Menu_Item)
Fl_Menu_Item.test_shortcut = new_instancemethod(_fltk.Fl_Menu_Item_test_shortcut,None,Fl_Menu_Item)
Fl_Menu_Item.find_shortcut = new_instancemethod(_fltk.Fl_Menu_Item_find_shortcut,None,Fl_Menu_Item)
Fl_Menu_Item.do_callback = new_instancemethod(_fltk.Fl_Menu_Item_do_callback,None,Fl_Menu_Item)
Fl_Menu_Item.checked = new_instancemethod(_fltk.Fl_Menu_Item_checked,None,Fl_Menu_Item)
Fl_Menu_Item.check = new_instancemethod(_fltk.Fl_Menu_Item_check,None,Fl_Menu_Item)
Fl_Menu_Item.uncheck = new_instancemethod(_fltk.Fl_Menu_Item_uncheck,None,Fl_Menu_Item)
Fl_Menu_Item.add = new_instancemethod(_fltk.Fl_Menu_Item_add,None,Fl_Menu_Item)
Fl_Menu_Item.size = new_instancemethod(_fltk.Fl_Menu_Item_size,None,Fl_Menu_Item)
Fl_Menu_Item.callback = new_instancemethod(_fltk.Fl_Menu_Item_callback,None,Fl_Menu_Item)
Fl_Menu_Item.user_data = new_instancemethod(_fltk.Fl_Menu_Item_user_data,None,Fl_Menu_Item)
_fltk.Fl_Menu_Item_swigregister(Fl_Menu_Item)

FL_PUP_NONE = _fltk.FL_PUP_NONE
FL_PUP_GREY = _fltk.FL_PUP_GREY
FL_PUP_GRAY = _fltk.FL_PUP_GRAY
FL_MENU_BOX = _fltk.FL_MENU_BOX
FL_PUP_BOX = _fltk.FL_PUP_BOX
FL_MENU_CHECK = _fltk.FL_MENU_CHECK
FL_PUP_CHECK = _fltk.FL_PUP_CHECK
FL_PUP_RADIO = _fltk.FL_PUP_RADIO
FL_PUP_INVISIBLE = _fltk.FL_PUP_INVISIBLE
FL_PUP_SUBMENU = _fltk.FL_PUP_SUBMENU
class Fl_Single_Window(Fl_Window):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Single_Window instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def flush(*args): return _fltk.Fl_Single_Window_flush(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Single_Window:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Single_Window(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def show(*args): return _fltk.Fl_Single_Window_show(*args)
    __swig_destroy__ = _fltk.delete_Fl_Single_Window
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Single_Window(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Single_Window_draw(*args)
Fl_Single_Window.flush = new_instancemethod(_fltk.Fl_Single_Window_flush,None,Fl_Single_Window)
Fl_Single_Window.show = new_instancemethod(_fltk.Fl_Single_Window_show,None,Fl_Single_Window)
Fl_Single_Window.draw = new_instancemethod(_fltk.Fl_Single_Window_draw,None,Fl_Single_Window)
_fltk.Fl_Single_Window_swigregister(Fl_Single_Window)

class Fl_Menu_Window(Fl_Single_Window):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Menu_Window instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def erase(*args): return _fltk.Fl_Menu_Window_erase(*args)
    def overlay(*args): return _fltk.Fl_Menu_Window_overlay(*args)
    def set_overlay(*args): return _fltk.Fl_Menu_Window_set_overlay(*args)
    def clear_overlay(*args): return _fltk.Fl_Menu_Window_clear_overlay(*args)
    __swig_destroy__ = _fltk.delete_Fl_Menu_Window
    def __init__(self, *args):
        if self.__class__ == Fl_Menu_Window:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Menu_Window(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Menu_Window(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Menu_Window_draw(*args)
Fl_Menu_Window.erase = new_instancemethod(_fltk.Fl_Menu_Window_erase,None,Fl_Menu_Window)
Fl_Menu_Window.overlay = new_instancemethod(_fltk.Fl_Menu_Window_overlay,None,Fl_Menu_Window)
Fl_Menu_Window.set_overlay = new_instancemethod(_fltk.Fl_Menu_Window_set_overlay,None,Fl_Menu_Window)
Fl_Menu_Window.clear_overlay = new_instancemethod(_fltk.Fl_Menu_Window_clear_overlay,None,Fl_Menu_Window)
Fl_Menu_Window.draw = new_instancemethod(_fltk.Fl_Menu_Window_draw,None,Fl_Menu_Window)
_fltk.Fl_Menu_Window_swigregister(Fl_Menu_Window)

class Fl_Multiline_Input(Fl_Input):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Multiline_Input instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Multiline_Input:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Multiline_Input(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Multiline_Input
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Multiline_Input(self)
        return weakref_proxy(self)
_fltk.Fl_Multiline_Input_swigregister(Fl_Multiline_Input)

class Fl_Output(Fl_Input):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Output instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Output:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Output(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Output
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Output(self)
        return weakref_proxy(self)
_fltk.Fl_Output_swigregister(Fl_Output)

class Fl_Multiline_Output(Fl_Output):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Multiline_Output instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Multiline_Output:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Multiline_Output(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Multiline_Output
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Multiline_Output(self)
        return weakref_proxy(self)
_fltk.Fl_Multiline_Output_swigregister(Fl_Multiline_Output)

class Fl_Multi_Browser(Fl_Browser):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Multi_Browser instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Multi_Browser:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Multi_Browser(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Multi_Browser
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Multi_Browser(self)
        return weakref_proxy(self)
    def item_first(*args): return _fltk.Fl_Multi_Browser_item_first(*args)
    def item_next(*args): return _fltk.Fl_Multi_Browser_item_next(*args)
    def item_prev(*args): return _fltk.Fl_Multi_Browser_item_prev(*args)
    def full_width(*args): return _fltk.Fl_Multi_Browser_full_width(*args)
    def item_select(*args): return _fltk.Fl_Multi_Browser_item_select(*args)
    def item_draw(*args): return _fltk.Fl_Multi_Browser_item_draw(*args)
    def full_height(*args): return _fltk.Fl_Multi_Browser_full_height(*args)
    def incr_height(*args): return _fltk.Fl_Multi_Browser_incr_height(*args)
    def draw(*args): return _fltk.Fl_Multi_Browser_draw(*args)
    def item_quick_height(*args): return _fltk.Fl_Multi_Browser_item_quick_height(*args)
    def item_selected(*args): return _fltk.Fl_Multi_Browser_item_selected(*args)
    def item_height(*args): return _fltk.Fl_Multi_Browser_item_height(*args)
    def item_width(*args): return _fltk.Fl_Multi_Browser_item_width(*args)
Fl_Multi_Browser.item_first = new_instancemethod(_fltk.Fl_Multi_Browser_item_first,None,Fl_Multi_Browser)
Fl_Multi_Browser.item_next = new_instancemethod(_fltk.Fl_Multi_Browser_item_next,None,Fl_Multi_Browser)
Fl_Multi_Browser.item_prev = new_instancemethod(_fltk.Fl_Multi_Browser_item_prev,None,Fl_Multi_Browser)
Fl_Multi_Browser.full_width = new_instancemethod(_fltk.Fl_Multi_Browser_full_width,None,Fl_Multi_Browser)
Fl_Multi_Browser.item_select = new_instancemethod(_fltk.Fl_Multi_Browser_item_select,None,Fl_Multi_Browser)
Fl_Multi_Browser.item_draw = new_instancemethod(_fltk.Fl_Multi_Browser_item_draw,None,Fl_Multi_Browser)
Fl_Multi_Browser.full_height = new_instancemethod(_fltk.Fl_Multi_Browser_full_height,None,Fl_Multi_Browser)
Fl_Multi_Browser.incr_height = new_instancemethod(_fltk.Fl_Multi_Browser_incr_height,None,Fl_Multi_Browser)
Fl_Multi_Browser.draw = new_instancemethod(_fltk.Fl_Multi_Browser_draw,None,Fl_Multi_Browser)
Fl_Multi_Browser.item_quick_height = new_instancemethod(_fltk.Fl_Multi_Browser_item_quick_height,None,Fl_Multi_Browser)
Fl_Multi_Browser.item_selected = new_instancemethod(_fltk.Fl_Multi_Browser_item_selected,None,Fl_Multi_Browser)
Fl_Multi_Browser.item_height = new_instancemethod(_fltk.Fl_Multi_Browser_item_height,None,Fl_Multi_Browser)
Fl_Multi_Browser.item_width = new_instancemethod(_fltk.Fl_Multi_Browser_item_width,None,Fl_Multi_Browser)
_fltk.Fl_Multi_Browser_swigregister(Fl_Multi_Browser)

class Fl_Multi_Label(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Multi_Label instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    labela = property(_fltk.Fl_Multi_Label_labela_get, _fltk.Fl_Multi_Label_labela_set)
    labelb = property(_fltk.Fl_Multi_Label_labelb_get, _fltk.Fl_Multi_Label_labelb_set)
    typea = property(_fltk.Fl_Multi_Label_typea_get, _fltk.Fl_Multi_Label_typea_set)
    typeb = property(_fltk.Fl_Multi_Label_typeb_get, _fltk.Fl_Multi_Label_typeb_set)
    def label(*args): return _fltk.Fl_Multi_Label_label(*args)
    def __init__(self, *args):
        this = _fltk.new_Fl_Multi_Label(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Multi_Label
Fl_Multi_Label.label = new_instancemethod(_fltk.Fl_Multi_Label_label,None,Fl_Multi_Label)
_fltk.Fl_Multi_Label_swigregister(Fl_Multi_Label)

class Fl_Nice_Slider(Fl_Slider):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Nice_Slider instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Nice_Slider:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Nice_Slider(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Nice_Slider
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Nice_Slider(self)
        return weakref_proxy(self)
_fltk.Fl_Nice_Slider_swigregister(Fl_Nice_Slider)

class Fl_Overlay_Window(Fl_Double_Window):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self): raise AttributeError, "No constructor defined"
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Overlay_Window instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    __swig_destroy__ = _fltk.delete_Fl_Overlay_Window
    def can_do_overlay(*args): return _fltk.Fl_Overlay_Window_can_do_overlay(*args)
    def redraw_overlay(*args): return _fltk.Fl_Overlay_Window_redraw_overlay(*args)
    def show(*args): return _fltk.Fl_Overlay_Window_show(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Overlay_Window(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Overlay_Window_draw(*args)
Fl_Overlay_Window.can_do_overlay = new_instancemethod(_fltk.Fl_Overlay_Window_can_do_overlay,None,Fl_Overlay_Window)
Fl_Overlay_Window.redraw_overlay = new_instancemethod(_fltk.Fl_Overlay_Window_redraw_overlay,None,Fl_Overlay_Window)
Fl_Overlay_Window.show = new_instancemethod(_fltk.Fl_Overlay_Window_show,None,Fl_Overlay_Window)
Fl_Overlay_Window.draw = new_instancemethod(_fltk.Fl_Overlay_Window_draw,None,Fl_Overlay_Window)
_fltk.Fl_Overlay_Window_swigregister(Fl_Overlay_Window)

class Fl_Pack(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Pack instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    VERTICAL = _fltk.Fl_Pack_VERTICAL
    HORIZONTAL = _fltk.Fl_Pack_HORIZONTAL
    def __init__(self, *args):
        if self.__class__ == Fl_Pack:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Pack(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def spacing(*args): return _fltk.Fl_Pack_spacing(*args)
    def horizontal(*args): return _fltk.Fl_Pack_horizontal(*args)
    __swig_destroy__ = _fltk.delete_Fl_Pack
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Pack(self)
        return weakref_proxy(self)
Fl_Pack.spacing = new_instancemethod(_fltk.Fl_Pack_spacing,None,Fl_Pack)
Fl_Pack.horizontal = new_instancemethod(_fltk.Fl_Pack_horizontal,None,Fl_Pack)
_fltk.Fl_Pack_swigregister(Fl_Pack)

class Fl_PNG_Image(Fl_RGB_Image):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_PNG_Image instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_PNG_Image:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_PNG_Image(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_PNG_Image
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_PNG_Image(self)
        return weakref_proxy(self)
_fltk.Fl_PNG_Image_swigregister(Fl_PNG_Image)

class Fl_PNM_Image(Fl_RGB_Image):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_PNM_Image instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_PNM_Image:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_PNM_Image(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_PNM_Image
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_PNM_Image(self)
        return weakref_proxy(self)
_fltk.Fl_PNM_Image_swigregister(Fl_PNM_Image)

class Fl_Positioner(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Positioner instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Positioner_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Positioner:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Positioner(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def xvalue(*args): return _fltk.Fl_Positioner_xvalue(*args)
    def yvalue(*args): return _fltk.Fl_Positioner_yvalue(*args)
    def value(*args): return _fltk.Fl_Positioner_value(*args)
    def xbounds(*args): return _fltk.Fl_Positioner_xbounds(*args)
    def xminimum(*args): return _fltk.Fl_Positioner_xminimum(*args)
    def xmaximum(*args): return _fltk.Fl_Positioner_xmaximum(*args)
    def ybounds(*args): return _fltk.Fl_Positioner_ybounds(*args)
    def yminimum(*args): return _fltk.Fl_Positioner_yminimum(*args)
    def ymaximum(*args): return _fltk.Fl_Positioner_ymaximum(*args)
    def xstep(*args): return _fltk.Fl_Positioner_xstep(*args)
    def ystep(*args): return _fltk.Fl_Positioner_ystep(*args)
    __swig_destroy__ = _fltk.delete_Fl_Positioner
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Positioner(self)
        return weakref_proxy(self)
Fl_Positioner.draw = new_instancemethod(_fltk.Fl_Positioner_draw,None,Fl_Positioner)
Fl_Positioner.xvalue = new_instancemethod(_fltk.Fl_Positioner_xvalue,None,Fl_Positioner)
Fl_Positioner.yvalue = new_instancemethod(_fltk.Fl_Positioner_yvalue,None,Fl_Positioner)
Fl_Positioner.value = new_instancemethod(_fltk.Fl_Positioner_value,None,Fl_Positioner)
Fl_Positioner.xbounds = new_instancemethod(_fltk.Fl_Positioner_xbounds,None,Fl_Positioner)
Fl_Positioner.xminimum = new_instancemethod(_fltk.Fl_Positioner_xminimum,None,Fl_Positioner)
Fl_Positioner.xmaximum = new_instancemethod(_fltk.Fl_Positioner_xmaximum,None,Fl_Positioner)
Fl_Positioner.ybounds = new_instancemethod(_fltk.Fl_Positioner_ybounds,None,Fl_Positioner)
Fl_Positioner.yminimum = new_instancemethod(_fltk.Fl_Positioner_yminimum,None,Fl_Positioner)
Fl_Positioner.ymaximum = new_instancemethod(_fltk.Fl_Positioner_ymaximum,None,Fl_Positioner)
Fl_Positioner.xstep = new_instancemethod(_fltk.Fl_Positioner_xstep,None,Fl_Positioner)
Fl_Positioner.ystep = new_instancemethod(_fltk.Fl_Positioner_ystep,None,Fl_Positioner)
_fltk.Fl_Positioner_swigregister(Fl_Positioner)

class Fl_Preferences(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Preferences instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    SYSTEM = _fltk.Fl_Preferences_SYSTEM
    USER = _fltk.Fl_Preferences_USER
    def __init__(self, *args):
        this = _fltk.new_Fl_Preferences(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Preferences
    def groups(*args): return _fltk.Fl_Preferences_groups(*args)
    def group(*args): return _fltk.Fl_Preferences_group(*args)
    def groupExists(*args): return _fltk.Fl_Preferences_groupExists(*args)
    def deleteGroup(*args): return _fltk.Fl_Preferences_deleteGroup(*args)
    def entries(*args): return _fltk.Fl_Preferences_entries(*args)
    def entry(*args): return _fltk.Fl_Preferences_entry(*args)
    def entryExists(*args): return _fltk.Fl_Preferences_entryExists(*args)
    def deleteEntry(*args): return _fltk.Fl_Preferences_deleteEntry(*args)
    def set(*args): return _fltk.Fl_Preferences_set(*args)
    def get(*args): return _fltk.Fl_Preferences_get(*args)
    def size(*args): return _fltk.Fl_Preferences_size(*args)
    def getUserdataPath(*args): return _fltk.Fl_Preferences_getUserdataPath(*args)
    def flush(*args): return _fltk.Fl_Preferences_flush(*args)
Fl_Preferences.groups = new_instancemethod(_fltk.Fl_Preferences_groups,None,Fl_Preferences)
Fl_Preferences.group = new_instancemethod(_fltk.Fl_Preferences_group,None,Fl_Preferences)
Fl_Preferences.groupExists = new_instancemethod(_fltk.Fl_Preferences_groupExists,None,Fl_Preferences)
Fl_Preferences.deleteGroup = new_instancemethod(_fltk.Fl_Preferences_deleteGroup,None,Fl_Preferences)
Fl_Preferences.entries = new_instancemethod(_fltk.Fl_Preferences_entries,None,Fl_Preferences)
Fl_Preferences.entry = new_instancemethod(_fltk.Fl_Preferences_entry,None,Fl_Preferences)
Fl_Preferences.entryExists = new_instancemethod(_fltk.Fl_Preferences_entryExists,None,Fl_Preferences)
Fl_Preferences.deleteEntry = new_instancemethod(_fltk.Fl_Preferences_deleteEntry,None,Fl_Preferences)
Fl_Preferences.set = new_instancemethod(_fltk.Fl_Preferences_set,None,Fl_Preferences)
Fl_Preferences.get = new_instancemethod(_fltk.Fl_Preferences_get,None,Fl_Preferences)
Fl_Preferences.size = new_instancemethod(_fltk.Fl_Preferences_size,None,Fl_Preferences)
Fl_Preferences.getUserdataPath = new_instancemethod(_fltk.Fl_Preferences_getUserdataPath,None,Fl_Preferences)
Fl_Preferences.flush = new_instancemethod(_fltk.Fl_Preferences_flush,None,Fl_Preferences)
_fltk.Fl_Preferences_swigregister(Fl_Preferences)

class Fl_Progress(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Progress instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Progress_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Progress:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Progress(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def maximum(*args): return _fltk.Fl_Progress_maximum(*args)
    def minimum(*args): return _fltk.Fl_Progress_minimum(*args)
    def value(*args): return _fltk.Fl_Progress_value(*args)
    __swig_destroy__ = _fltk.delete_Fl_Progress
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Progress(self)
        return weakref_proxy(self)
Fl_Progress.draw = new_instancemethod(_fltk.Fl_Progress_draw,None,Fl_Progress)
Fl_Progress.maximum = new_instancemethod(_fltk.Fl_Progress_maximum,None,Fl_Progress)
Fl_Progress.minimum = new_instancemethod(_fltk.Fl_Progress_minimum,None,Fl_Progress)
Fl_Progress.value = new_instancemethod(_fltk.Fl_Progress_value,None,Fl_Progress)
_fltk.Fl_Progress_swigregister(Fl_Progress)

class Fl_Radio_Button(Fl_Button):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Radio_Button instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Radio_Button:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Radio_Button(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Radio_Button
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Radio_Button(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Radio_Button_draw(*args)
Fl_Radio_Button.draw = new_instancemethod(_fltk.Fl_Radio_Button_draw,None,Fl_Radio_Button)
_fltk.Fl_Radio_Button_swigregister(Fl_Radio_Button)

class Fl_Radio_Light_Button(Fl_Light_Button):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Radio_Light_Button instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Radio_Light_Button:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Radio_Light_Button(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Radio_Light_Button
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Radio_Light_Button(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Radio_Light_Button_draw(*args)
Fl_Radio_Light_Button.draw = new_instancemethod(_fltk.Fl_Radio_Light_Button_draw,None,Fl_Radio_Light_Button)
_fltk.Fl_Radio_Light_Button_swigregister(Fl_Radio_Light_Button)

class Fl_Round_Button(Fl_Light_Button):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Round_Button instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Round_Button:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Round_Button(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Round_Button
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Round_Button(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Round_Button_draw(*args)
Fl_Round_Button.draw = new_instancemethod(_fltk.Fl_Round_Button_draw,None,Fl_Round_Button)
_fltk.Fl_Round_Button_swigregister(Fl_Round_Button)

class Fl_Radio_Round_Button(Fl_Round_Button):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Radio_Round_Button instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Radio_Round_Button:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Radio_Round_Button(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Radio_Round_Button
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Radio_Round_Button(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Radio_Round_Button_draw(*args)
Fl_Radio_Round_Button.draw = new_instancemethod(_fltk.Fl_Radio_Round_Button_draw,None,Fl_Radio_Round_Button)
_fltk.Fl_Radio_Round_Button_swigregister(Fl_Radio_Round_Button)

class Fl_Repeat_Button(Fl_Button):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Repeat_Button instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Repeat_Button:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Repeat_Button(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def deactivate(*args): return _fltk.Fl_Repeat_Button_deactivate(*args)
    __swig_destroy__ = _fltk.delete_Fl_Repeat_Button
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Repeat_Button(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Repeat_Button_draw(*args)
Fl_Repeat_Button.deactivate = new_instancemethod(_fltk.Fl_Repeat_Button_deactivate,None,Fl_Repeat_Button)
Fl_Repeat_Button.draw = new_instancemethod(_fltk.Fl_Repeat_Button_draw,None,Fl_Repeat_Button)
_fltk.Fl_Repeat_Button_swigregister(Fl_Repeat_Button)

class Fl_Return_Button(Fl_Button):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Return_Button instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Return_Button_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Return_Button:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Return_Button(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Return_Button
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Return_Button(self)
        return weakref_proxy(self)
Fl_Return_Button.draw = new_instancemethod(_fltk.Fl_Return_Button_draw,None,Fl_Return_Button)
_fltk.Fl_Return_Button_swigregister(Fl_Return_Button)

class Fl_Roller(Fl_Valuator):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Roller instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Roller_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Roller:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Roller(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Roller
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Roller(self)
        return weakref_proxy(self)
Fl_Roller.draw = new_instancemethod(_fltk.Fl_Roller_draw,None,Fl_Roller)
_fltk.Fl_Roller_swigregister(Fl_Roller)

class Fl_Round_Clock(Fl_Clock):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Round_Clock instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Round_Clock:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Round_Clock(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Round_Clock
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Round_Clock(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Round_Clock_draw(*args)
Fl_Round_Clock.draw = new_instancemethod(_fltk.Fl_Round_Clock_draw,None,Fl_Round_Clock)
_fltk.Fl_Round_Clock_swigregister(Fl_Round_Clock)

class Fl_Scroll(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Scroll instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Scroll_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Scroll:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Scroll(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    HORIZONTAL = _fltk.Fl_Scroll_HORIZONTAL
    VERTICAL = _fltk.Fl_Scroll_VERTICAL
    BOTH = _fltk.Fl_Scroll_BOTH
    ALWAYS_ON = _fltk.Fl_Scroll_ALWAYS_ON
    HORIZONTAL_ALWAYS = _fltk.Fl_Scroll_HORIZONTAL_ALWAYS
    VERTICAL_ALWAYS = _fltk.Fl_Scroll_VERTICAL_ALWAYS
    BOTH_ALWAYS = _fltk.Fl_Scroll_BOTH_ALWAYS
    def xposition(*args): return _fltk.Fl_Scroll_xposition(*args)
    def yposition(*args): return _fltk.Fl_Scroll_yposition(*args)
    def position(*args): return _fltk.Fl_Scroll_position(*args)
    def clear(*args): return _fltk.Fl_Scroll_clear(*args)
    def getScrollbar(*args): return _fltk.Fl_Scroll_getScrollbar(*args)
    def getHScrollbar(*args): return _fltk.Fl_Scroll_getHScrollbar(*args)
    __swig_destroy__ = _fltk.delete_Fl_Scroll
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Scroll(self)
        return weakref_proxy(self)
Fl_Scroll.draw = new_instancemethod(_fltk.Fl_Scroll_draw,None,Fl_Scroll)
Fl_Scroll.xposition = new_instancemethod(_fltk.Fl_Scroll_xposition,None,Fl_Scroll)
Fl_Scroll.yposition = new_instancemethod(_fltk.Fl_Scroll_yposition,None,Fl_Scroll)
Fl_Scroll.position = new_instancemethod(_fltk.Fl_Scroll_position,None,Fl_Scroll)
Fl_Scroll.clear = new_instancemethod(_fltk.Fl_Scroll_clear,None,Fl_Scroll)
Fl_Scroll.getScrollbar = new_instancemethod(_fltk.Fl_Scroll_getScrollbar,None,Fl_Scroll)
Fl_Scroll.getHScrollbar = new_instancemethod(_fltk.Fl_Scroll_getHScrollbar,None,Fl_Scroll)
_fltk.Fl_Scroll_swigregister(Fl_Scroll)

class Fl_Scrollbar(Fl_Slider):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Scrollbar instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Scrollbar_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Scrollbar:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Scrollbar(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def value(*args): return _fltk.Fl_Scrollbar_value(*args)
    def linesize(*args): return _fltk.Fl_Scrollbar_linesize(*args)
    __swig_destroy__ = _fltk.delete_Fl_Scrollbar
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Scrollbar(self)
        return weakref_proxy(self)
Fl_Scrollbar.draw = new_instancemethod(_fltk.Fl_Scrollbar_draw,None,Fl_Scrollbar)
Fl_Scrollbar.value = new_instancemethod(_fltk.Fl_Scrollbar_value,None,Fl_Scrollbar)
Fl_Scrollbar.linesize = new_instancemethod(_fltk.Fl_Scrollbar_linesize,None,Fl_Scrollbar)
_fltk.Fl_Scrollbar_swigregister(Fl_Scrollbar)

class Fl_Secret_Input(Fl_Input):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Secret_Input instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Secret_Input:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Secret_Input(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Secret_Input
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Secret_Input(self)
        return weakref_proxy(self)
_fltk.Fl_Secret_Input_swigregister(Fl_Secret_Input)

class Fl_Select_Browser(Fl_Browser):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Select_Browser instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Select_Browser:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Select_Browser(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Select_Browser
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Select_Browser(self)
        return weakref_proxy(self)
    def item_first(*args): return _fltk.Fl_Select_Browser_item_first(*args)
    def item_next(*args): return _fltk.Fl_Select_Browser_item_next(*args)
    def item_prev(*args): return _fltk.Fl_Select_Browser_item_prev(*args)
    def full_width(*args): return _fltk.Fl_Select_Browser_full_width(*args)
    def item_select(*args): return _fltk.Fl_Select_Browser_item_select(*args)
    def item_draw(*args): return _fltk.Fl_Select_Browser_item_draw(*args)
    def full_height(*args): return _fltk.Fl_Select_Browser_full_height(*args)
    def incr_height(*args): return _fltk.Fl_Select_Browser_incr_height(*args)
    def draw(*args): return _fltk.Fl_Select_Browser_draw(*args)
    def item_quick_height(*args): return _fltk.Fl_Select_Browser_item_quick_height(*args)
    def item_selected(*args): return _fltk.Fl_Select_Browser_item_selected(*args)
    def item_height(*args): return _fltk.Fl_Select_Browser_item_height(*args)
    def item_width(*args): return _fltk.Fl_Select_Browser_item_width(*args)
Fl_Select_Browser.item_first = new_instancemethod(_fltk.Fl_Select_Browser_item_first,None,Fl_Select_Browser)
Fl_Select_Browser.item_next = new_instancemethod(_fltk.Fl_Select_Browser_item_next,None,Fl_Select_Browser)
Fl_Select_Browser.item_prev = new_instancemethod(_fltk.Fl_Select_Browser_item_prev,None,Fl_Select_Browser)
Fl_Select_Browser.full_width = new_instancemethod(_fltk.Fl_Select_Browser_full_width,None,Fl_Select_Browser)
Fl_Select_Browser.item_select = new_instancemethod(_fltk.Fl_Select_Browser_item_select,None,Fl_Select_Browser)
Fl_Select_Browser.item_draw = new_instancemethod(_fltk.Fl_Select_Browser_item_draw,None,Fl_Select_Browser)
Fl_Select_Browser.full_height = new_instancemethod(_fltk.Fl_Select_Browser_full_height,None,Fl_Select_Browser)
Fl_Select_Browser.incr_height = new_instancemethod(_fltk.Fl_Select_Browser_incr_height,None,Fl_Select_Browser)
Fl_Select_Browser.draw = new_instancemethod(_fltk.Fl_Select_Browser_draw,None,Fl_Select_Browser)
Fl_Select_Browser.item_quick_height = new_instancemethod(_fltk.Fl_Select_Browser_item_quick_height,None,Fl_Select_Browser)
Fl_Select_Browser.item_selected = new_instancemethod(_fltk.Fl_Select_Browser_item_selected,None,Fl_Select_Browser)
Fl_Select_Browser.item_height = new_instancemethod(_fltk.Fl_Select_Browser_item_height,None,Fl_Select_Browser)
Fl_Select_Browser.item_width = new_instancemethod(_fltk.Fl_Select_Browser_item_width,None,Fl_Select_Browser)
_fltk.Fl_Select_Browser_swigregister(Fl_Select_Browser)

class Fl_Shared_Image(Fl_Image):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Shared_Image instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Shared_Image:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Shared_Image(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def name(*args): return _fltk.Fl_Shared_Image_name(*args)
    def refcount(*args): return _fltk.Fl_Shared_Image_refcount(*args)
    def release(*args): return _fltk.Fl_Shared_Image_release(*args)
    def reload(*args): return _fltk.Fl_Shared_Image_reload(*args)
    def copy(*args): return _fltk.Fl_Shared_Image_copy(*args)
    def color_average(*args): return _fltk.Fl_Shared_Image_color_average(*args)
    def desaturate(*args): return _fltk.Fl_Shared_Image_desaturate(*args)
    def draw(*args): return _fltk.Fl_Shared_Image_draw(*args)
    def uncache(*args): return _fltk.Fl_Shared_Image_uncache(*args)
    find = staticmethod(_fltk.Fl_Shared_Image_find)
    get = staticmethod(_fltk.Fl_Shared_Image_get)
    images = staticmethod(_fltk.Fl_Shared_Image_images)
    num_images = staticmethod(_fltk.Fl_Shared_Image_num_images)
    add_handler = staticmethod(_fltk.Fl_Shared_Image_add_handler)
    remove_handler = staticmethod(_fltk.Fl_Shared_Image_remove_handler)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Shared_Image(self)
        return weakref_proxy(self)
Fl_Shared_Image.name = new_instancemethod(_fltk.Fl_Shared_Image_name,None,Fl_Shared_Image)
Fl_Shared_Image.refcount = new_instancemethod(_fltk.Fl_Shared_Image_refcount,None,Fl_Shared_Image)
Fl_Shared_Image.release = new_instancemethod(_fltk.Fl_Shared_Image_release,None,Fl_Shared_Image)
Fl_Shared_Image.reload = new_instancemethod(_fltk.Fl_Shared_Image_reload,None,Fl_Shared_Image)
Fl_Shared_Image.copy = new_instancemethod(_fltk.Fl_Shared_Image_copy,None,Fl_Shared_Image)
Fl_Shared_Image.color_average = new_instancemethod(_fltk.Fl_Shared_Image_color_average,None,Fl_Shared_Image)
Fl_Shared_Image.desaturate = new_instancemethod(_fltk.Fl_Shared_Image_desaturate,None,Fl_Shared_Image)
Fl_Shared_Image.draw = new_instancemethod(_fltk.Fl_Shared_Image_draw,None,Fl_Shared_Image)
Fl_Shared_Image.uncache = new_instancemethod(_fltk.Fl_Shared_Image_uncache,None,Fl_Shared_Image)
_fltk.Fl_Shared_Image_swigregister(Fl_Shared_Image)

Fl_Shared_Image_find = _fltk.Fl_Shared_Image_find

Fl_Shared_Image_get = _fltk.Fl_Shared_Image_get

Fl_Shared_Image_images = _fltk.Fl_Shared_Image_images

Fl_Shared_Image_num_images = _fltk.Fl_Shared_Image_num_images

Fl_Shared_Image_add_handler = _fltk.Fl_Shared_Image_add_handler

Fl_Shared_Image_remove_handler = _fltk.Fl_Shared_Image_remove_handler


fl_register_images = _fltk.fl_register_images
class Fl_Spinner(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Spinner instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Spinner:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Spinner(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def format(*args): return _fltk.Fl_Spinner_format(*args)
    def maxinum(*args): return _fltk.Fl_Spinner_maxinum(*args)
    def mininum(*args): return _fltk.Fl_Spinner_mininum(*args)
    def range(*args): return _fltk.Fl_Spinner_range(*args)
    def step(*args): return _fltk.Fl_Spinner_step(*args)
    def textcolor(*args): return _fltk.Fl_Spinner_textcolor(*args)
    def textfont(*args): return _fltk.Fl_Spinner_textfont(*args)
    def textsize(*args): return _fltk.Fl_Spinner_textsize(*args)
    def value(*args): return _fltk.Fl_Spinner_value(*args)
    def minimum(*args): return _fltk.Fl_Spinner_minimum(*args)
    def maximum(*args): return _fltk.Fl_Spinner_maximum(*args)
    __swig_destroy__ = _fltk.delete_Fl_Spinner
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Spinner(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Spinner_draw(*args)
Fl_Spinner.format = new_instancemethod(_fltk.Fl_Spinner_format,None,Fl_Spinner)
Fl_Spinner.maxinum = new_instancemethod(_fltk.Fl_Spinner_maxinum,None,Fl_Spinner)
Fl_Spinner.mininum = new_instancemethod(_fltk.Fl_Spinner_mininum,None,Fl_Spinner)
Fl_Spinner.range = new_instancemethod(_fltk.Fl_Spinner_range,None,Fl_Spinner)
Fl_Spinner.step = new_instancemethod(_fltk.Fl_Spinner_step,None,Fl_Spinner)
Fl_Spinner.textcolor = new_instancemethod(_fltk.Fl_Spinner_textcolor,None,Fl_Spinner)
Fl_Spinner.textfont = new_instancemethod(_fltk.Fl_Spinner_textfont,None,Fl_Spinner)
Fl_Spinner.textsize = new_instancemethod(_fltk.Fl_Spinner_textsize,None,Fl_Spinner)
Fl_Spinner.value = new_instancemethod(_fltk.Fl_Spinner_value,None,Fl_Spinner)
Fl_Spinner.minimum = new_instancemethod(_fltk.Fl_Spinner_minimum,None,Fl_Spinner)
Fl_Spinner.maximum = new_instancemethod(_fltk.Fl_Spinner_maximum,None,Fl_Spinner)
Fl_Spinner.draw = new_instancemethod(_fltk.Fl_Spinner_draw,None,Fl_Spinner)
_fltk.Fl_Spinner_swigregister(Fl_Spinner)


fl_show_colormap = _fltk.fl_show_colormap
class Fl_Simple_Counter(Fl_Counter):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Simple_Counter instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Simple_Counter:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Simple_Counter(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Simple_Counter
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Simple_Counter(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Simple_Counter_draw(*args)
Fl_Simple_Counter.draw = new_instancemethod(_fltk.Fl_Simple_Counter_draw,None,Fl_Simple_Counter)
_fltk.Fl_Simple_Counter_swigregister(Fl_Simple_Counter)

class Fl_Tabs(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Tabs instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Tabs_draw(*args)
    def value(*args): return _fltk.Fl_Tabs_value(*args)
    def push(*args): return _fltk.Fl_Tabs_push(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Tabs:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Tabs(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def which(*args): return _fltk.Fl_Tabs_which(*args)
    __swig_destroy__ = _fltk.delete_Fl_Tabs
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Tabs(self)
        return weakref_proxy(self)
Fl_Tabs.draw = new_instancemethod(_fltk.Fl_Tabs_draw,None,Fl_Tabs)
Fl_Tabs.value = new_instancemethod(_fltk.Fl_Tabs_value,None,Fl_Tabs)
Fl_Tabs.push = new_instancemethod(_fltk.Fl_Tabs_push,None,Fl_Tabs)
Fl_Tabs.which = new_instancemethod(_fltk.Fl_Tabs_which,None,Fl_Tabs)
_fltk.Fl_Tabs_swigregister(Fl_Tabs)

FL_TEXT_MAX_EXP_CHAR_LEN = _fltk.FL_TEXT_MAX_EXP_CHAR_LEN
class Fl_Text_Selection(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Text_Selection instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def set(*args): return _fltk.Fl_Text_Selection_set(*args)
    def set_rectangular(*args): return _fltk.Fl_Text_Selection_set_rectangular(*args)
    def update(*args): return _fltk.Fl_Text_Selection_update(*args)
    def rectangular(*args): return _fltk.Fl_Text_Selection_rectangular(*args)
    def start(*args): return _fltk.Fl_Text_Selection_start(*args)
    def end(*args): return _fltk.Fl_Text_Selection_end(*args)
    def rect_start(*args): return _fltk.Fl_Text_Selection_rect_start(*args)
    def rect_end(*args): return _fltk.Fl_Text_Selection_rect_end(*args)
    def selected(*args): return _fltk.Fl_Text_Selection_selected(*args)
    def includes(*args): return _fltk.Fl_Text_Selection_includes(*args)
    def position(*args): return _fltk.Fl_Text_Selection_position(*args)
    def __init__(self, *args):
        this = _fltk.new_Fl_Text_Selection(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Text_Selection
Fl_Text_Selection.set = new_instancemethod(_fltk.Fl_Text_Selection_set,None,Fl_Text_Selection)
Fl_Text_Selection.set_rectangular = new_instancemethod(_fltk.Fl_Text_Selection_set_rectangular,None,Fl_Text_Selection)
Fl_Text_Selection.update = new_instancemethod(_fltk.Fl_Text_Selection_update,None,Fl_Text_Selection)
Fl_Text_Selection.rectangular = new_instancemethod(_fltk.Fl_Text_Selection_rectangular,None,Fl_Text_Selection)
Fl_Text_Selection.start = new_instancemethod(_fltk.Fl_Text_Selection_start,None,Fl_Text_Selection)
Fl_Text_Selection.end = new_instancemethod(_fltk.Fl_Text_Selection_end,None,Fl_Text_Selection)
Fl_Text_Selection.rect_start = new_instancemethod(_fltk.Fl_Text_Selection_rect_start,None,Fl_Text_Selection)
Fl_Text_Selection.rect_end = new_instancemethod(_fltk.Fl_Text_Selection_rect_end,None,Fl_Text_Selection)
Fl_Text_Selection.selected = new_instancemethod(_fltk.Fl_Text_Selection_selected,None,Fl_Text_Selection)
Fl_Text_Selection.includes = new_instancemethod(_fltk.Fl_Text_Selection_includes,None,Fl_Text_Selection)
Fl_Text_Selection.position = new_instancemethod(_fltk.Fl_Text_Selection_position,None,Fl_Text_Selection)
_fltk.Fl_Text_Selection_swigregister(Fl_Text_Selection)

class Fl_Text_Buffer(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Text_Buffer instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        this = _fltk.new_Fl_Text_Buffer(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Text_Buffer
    def length(*args): return _fltk.Fl_Text_Buffer_length(*args)
    def text(*args): return _fltk.Fl_Text_Buffer_text(*args)
    def text_range(*args): return _fltk.Fl_Text_Buffer_text_range(*args)
    def character(*args): return _fltk.Fl_Text_Buffer_character(*args)
    def text_in_rectangle(*args): return _fltk.Fl_Text_Buffer_text_in_rectangle(*args)
    def insert(*args): return _fltk.Fl_Text_Buffer_insert(*args)
    def append(*args): return _fltk.Fl_Text_Buffer_append(*args)
    def remove(*args): return _fltk.Fl_Text_Buffer_remove(*args)
    def replace(*args): return _fltk.Fl_Text_Buffer_replace(*args)
    def copy(*args): return _fltk.Fl_Text_Buffer_copy(*args)
    def undo(*args): return _fltk.Fl_Text_Buffer_undo(*args)
    def canUndo(*args): return _fltk.Fl_Text_Buffer_canUndo(*args)
    def insertfile(*args): return _fltk.Fl_Text_Buffer_insertfile(*args)
    def appendfile(*args): return _fltk.Fl_Text_Buffer_appendfile(*args)
    def loadfile(*args): return _fltk.Fl_Text_Buffer_loadfile(*args)
    def outputfile(*args): return _fltk.Fl_Text_Buffer_outputfile(*args)
    def savefile(*args): return _fltk.Fl_Text_Buffer_savefile(*args)
    def insert_column(*args): return _fltk.Fl_Text_Buffer_insert_column(*args)
    def replace_rectangular(*args): return _fltk.Fl_Text_Buffer_replace_rectangular(*args)
    def overlay_rectangular(*args): return _fltk.Fl_Text_Buffer_overlay_rectangular(*args)
    def remove_rectangular(*args): return _fltk.Fl_Text_Buffer_remove_rectangular(*args)
    def clear_rectangular(*args): return _fltk.Fl_Text_Buffer_clear_rectangular(*args)
    def tab_distance(*args): return _fltk.Fl_Text_Buffer_tab_distance(*args)
    def select(*args): return _fltk.Fl_Text_Buffer_select(*args)
    def selected(*args): return _fltk.Fl_Text_Buffer_selected(*args)
    def unselect(*args): return _fltk.Fl_Text_Buffer_unselect(*args)
    def select_rectangular(*args): return _fltk.Fl_Text_Buffer_select_rectangular(*args)
    def selection_position(*args): return _fltk.Fl_Text_Buffer_selection_position(*args)
    def selection_text(*args): return _fltk.Fl_Text_Buffer_selection_text(*args)
    def remove_selection(*args): return _fltk.Fl_Text_Buffer_remove_selection(*args)
    def replace_selection(*args): return _fltk.Fl_Text_Buffer_replace_selection(*args)
    def secondary_select(*args): return _fltk.Fl_Text_Buffer_secondary_select(*args)
    def secondary_unselect(*args): return _fltk.Fl_Text_Buffer_secondary_unselect(*args)
    def secondary_select_rectangular(*args): return _fltk.Fl_Text_Buffer_secondary_select_rectangular(*args)
    def secondary_selection_position(*args): return _fltk.Fl_Text_Buffer_secondary_selection_position(*args)
    def secondary_selection_text(*args): return _fltk.Fl_Text_Buffer_secondary_selection_text(*args)
    def remove_secondary_selection(*args): return _fltk.Fl_Text_Buffer_remove_secondary_selection(*args)
    def replace_secondary_selection(*args): return _fltk.Fl_Text_Buffer_replace_secondary_selection(*args)
    def highlight(*args): return _fltk.Fl_Text_Buffer_highlight(*args)
    def unhighlight(*args): return _fltk.Fl_Text_Buffer_unhighlight(*args)
    def highlight_rectangular(*args): return _fltk.Fl_Text_Buffer_highlight_rectangular(*args)
    def highlight_position(*args): return _fltk.Fl_Text_Buffer_highlight_position(*args)
    def highlight_text(*args): return _fltk.Fl_Text_Buffer_highlight_text(*args)
    def remove_modify_callback(*args): return _fltk.Fl_Text_Buffer_remove_modify_callback(*args)
    def add_predelete_callback(*args): return _fltk.Fl_Text_Buffer_add_predelete_callback(*args)
    def remove_predelete_callback(*args): return _fltk.Fl_Text_Buffer_remove_predelete_callback(*args)
    def line_text(*args): return _fltk.Fl_Text_Buffer_line_text(*args)
    def line_start(*args): return _fltk.Fl_Text_Buffer_line_start(*args)
    def line_end(*args): return _fltk.Fl_Text_Buffer_line_end(*args)
    def word_start(*args): return _fltk.Fl_Text_Buffer_word_start(*args)
    def word_end(*args): return _fltk.Fl_Text_Buffer_word_end(*args)
    expand_character = staticmethod(_fltk.Fl_Text_Buffer_expand_character)
    character_width = staticmethod(_fltk.Fl_Text_Buffer_character_width)
    def count_displayed_characters(*args): return _fltk.Fl_Text_Buffer_count_displayed_characters(*args)
    def skip_displayed_characters(*args): return _fltk.Fl_Text_Buffer_skip_displayed_characters(*args)
    def count_lines(*args): return _fltk.Fl_Text_Buffer_count_lines(*args)
    def skip_lines(*args): return _fltk.Fl_Text_Buffer_skip_lines(*args)
    def rewind_lines(*args): return _fltk.Fl_Text_Buffer_rewind_lines(*args)
    def findchar_forward(*args): return _fltk.Fl_Text_Buffer_findchar_forward(*args)
    def findchar_backward(*args): return _fltk.Fl_Text_Buffer_findchar_backward(*args)
    def findchars_forward(*args): return _fltk.Fl_Text_Buffer_findchars_forward(*args)
    def findchars_backward(*args): return _fltk.Fl_Text_Buffer_findchars_backward(*args)
    def search_forward(*args): return _fltk.Fl_Text_Buffer_search_forward(*args)
    def search_backward(*args): return _fltk.Fl_Text_Buffer_search_backward(*args)
    def substitute_null_characters(*args): return _fltk.Fl_Text_Buffer_substitute_null_characters(*args)
    def unsubstitute_null_characters(*args): return _fltk.Fl_Text_Buffer_unsubstitute_null_characters(*args)
    def null_substitution_character(*args): return _fltk.Fl_Text_Buffer_null_substitution_character(*args)
    def primary_selection(*args): return _fltk.Fl_Text_Buffer_primary_selection(*args)
    def secondary_selection(*args): return _fltk.Fl_Text_Buffer_secondary_selection(*args)
    def highlight_selection(*args): return _fltk.Fl_Text_Buffer_highlight_selection(*args)
    def add_modify_callback(*args): return _fltk.Fl_Text_Buffer_add_modify_callback(*args)
Fl_Text_Buffer.length = new_instancemethod(_fltk.Fl_Text_Buffer_length,None,Fl_Text_Buffer)
Fl_Text_Buffer.text = new_instancemethod(_fltk.Fl_Text_Buffer_text,None,Fl_Text_Buffer)
Fl_Text_Buffer.text_range = new_instancemethod(_fltk.Fl_Text_Buffer_text_range,None,Fl_Text_Buffer)
Fl_Text_Buffer.character = new_instancemethod(_fltk.Fl_Text_Buffer_character,None,Fl_Text_Buffer)
Fl_Text_Buffer.text_in_rectangle = new_instancemethod(_fltk.Fl_Text_Buffer_text_in_rectangle,None,Fl_Text_Buffer)
Fl_Text_Buffer.insert = new_instancemethod(_fltk.Fl_Text_Buffer_insert,None,Fl_Text_Buffer)
Fl_Text_Buffer.append = new_instancemethod(_fltk.Fl_Text_Buffer_append,None,Fl_Text_Buffer)
Fl_Text_Buffer.remove = new_instancemethod(_fltk.Fl_Text_Buffer_remove,None,Fl_Text_Buffer)
Fl_Text_Buffer.replace = new_instancemethod(_fltk.Fl_Text_Buffer_replace,None,Fl_Text_Buffer)
Fl_Text_Buffer.copy = new_instancemethod(_fltk.Fl_Text_Buffer_copy,None,Fl_Text_Buffer)
Fl_Text_Buffer.undo = new_instancemethod(_fltk.Fl_Text_Buffer_undo,None,Fl_Text_Buffer)
Fl_Text_Buffer.canUndo = new_instancemethod(_fltk.Fl_Text_Buffer_canUndo,None,Fl_Text_Buffer)
Fl_Text_Buffer.insertfile = new_instancemethod(_fltk.Fl_Text_Buffer_insertfile,None,Fl_Text_Buffer)
Fl_Text_Buffer.appendfile = new_instancemethod(_fltk.Fl_Text_Buffer_appendfile,None,Fl_Text_Buffer)
Fl_Text_Buffer.loadfile = new_instancemethod(_fltk.Fl_Text_Buffer_loadfile,None,Fl_Text_Buffer)
Fl_Text_Buffer.outputfile = new_instancemethod(_fltk.Fl_Text_Buffer_outputfile,None,Fl_Text_Buffer)
Fl_Text_Buffer.savefile = new_instancemethod(_fltk.Fl_Text_Buffer_savefile,None,Fl_Text_Buffer)
Fl_Text_Buffer.insert_column = new_instancemethod(_fltk.Fl_Text_Buffer_insert_column,None,Fl_Text_Buffer)
Fl_Text_Buffer.replace_rectangular = new_instancemethod(_fltk.Fl_Text_Buffer_replace_rectangular,None,Fl_Text_Buffer)
Fl_Text_Buffer.overlay_rectangular = new_instancemethod(_fltk.Fl_Text_Buffer_overlay_rectangular,None,Fl_Text_Buffer)
Fl_Text_Buffer.remove_rectangular = new_instancemethod(_fltk.Fl_Text_Buffer_remove_rectangular,None,Fl_Text_Buffer)
Fl_Text_Buffer.clear_rectangular = new_instancemethod(_fltk.Fl_Text_Buffer_clear_rectangular,None,Fl_Text_Buffer)
Fl_Text_Buffer.tab_distance = new_instancemethod(_fltk.Fl_Text_Buffer_tab_distance,None,Fl_Text_Buffer)
Fl_Text_Buffer.select = new_instancemethod(_fltk.Fl_Text_Buffer_select,None,Fl_Text_Buffer)
Fl_Text_Buffer.selected = new_instancemethod(_fltk.Fl_Text_Buffer_selected,None,Fl_Text_Buffer)
Fl_Text_Buffer.unselect = new_instancemethod(_fltk.Fl_Text_Buffer_unselect,None,Fl_Text_Buffer)
Fl_Text_Buffer.select_rectangular = new_instancemethod(_fltk.Fl_Text_Buffer_select_rectangular,None,Fl_Text_Buffer)
Fl_Text_Buffer.selection_position = new_instancemethod(_fltk.Fl_Text_Buffer_selection_position,None,Fl_Text_Buffer)
Fl_Text_Buffer.selection_text = new_instancemethod(_fltk.Fl_Text_Buffer_selection_text,None,Fl_Text_Buffer)
Fl_Text_Buffer.remove_selection = new_instancemethod(_fltk.Fl_Text_Buffer_remove_selection,None,Fl_Text_Buffer)
Fl_Text_Buffer.replace_selection = new_instancemethod(_fltk.Fl_Text_Buffer_replace_selection,None,Fl_Text_Buffer)
Fl_Text_Buffer.secondary_select = new_instancemethod(_fltk.Fl_Text_Buffer_secondary_select,None,Fl_Text_Buffer)
Fl_Text_Buffer.secondary_unselect = new_instancemethod(_fltk.Fl_Text_Buffer_secondary_unselect,None,Fl_Text_Buffer)
Fl_Text_Buffer.secondary_select_rectangular = new_instancemethod(_fltk.Fl_Text_Buffer_secondary_select_rectangular,None,Fl_Text_Buffer)
Fl_Text_Buffer.secondary_selection_position = new_instancemethod(_fltk.Fl_Text_Buffer_secondary_selection_position,None,Fl_Text_Buffer)
Fl_Text_Buffer.secondary_selection_text = new_instancemethod(_fltk.Fl_Text_Buffer_secondary_selection_text,None,Fl_Text_Buffer)
Fl_Text_Buffer.remove_secondary_selection = new_instancemethod(_fltk.Fl_Text_Buffer_remove_secondary_selection,None,Fl_Text_Buffer)
Fl_Text_Buffer.replace_secondary_selection = new_instancemethod(_fltk.Fl_Text_Buffer_replace_secondary_selection,None,Fl_Text_Buffer)
Fl_Text_Buffer.highlight = new_instancemethod(_fltk.Fl_Text_Buffer_highlight,None,Fl_Text_Buffer)
Fl_Text_Buffer.unhighlight = new_instancemethod(_fltk.Fl_Text_Buffer_unhighlight,None,Fl_Text_Buffer)
Fl_Text_Buffer.highlight_rectangular = new_instancemethod(_fltk.Fl_Text_Buffer_highlight_rectangular,None,Fl_Text_Buffer)
Fl_Text_Buffer.highlight_position = new_instancemethod(_fltk.Fl_Text_Buffer_highlight_position,None,Fl_Text_Buffer)
Fl_Text_Buffer.highlight_text = new_instancemethod(_fltk.Fl_Text_Buffer_highlight_text,None,Fl_Text_Buffer)
Fl_Text_Buffer.remove_modify_callback = new_instancemethod(_fltk.Fl_Text_Buffer_remove_modify_callback,None,Fl_Text_Buffer)
Fl_Text_Buffer.add_predelete_callback = new_instancemethod(_fltk.Fl_Text_Buffer_add_predelete_callback,None,Fl_Text_Buffer)
Fl_Text_Buffer.remove_predelete_callback = new_instancemethod(_fltk.Fl_Text_Buffer_remove_predelete_callback,None,Fl_Text_Buffer)
Fl_Text_Buffer.line_text = new_instancemethod(_fltk.Fl_Text_Buffer_line_text,None,Fl_Text_Buffer)
Fl_Text_Buffer.line_start = new_instancemethod(_fltk.Fl_Text_Buffer_line_start,None,Fl_Text_Buffer)
Fl_Text_Buffer.line_end = new_instancemethod(_fltk.Fl_Text_Buffer_line_end,None,Fl_Text_Buffer)
Fl_Text_Buffer.word_start = new_instancemethod(_fltk.Fl_Text_Buffer_word_start,None,Fl_Text_Buffer)
Fl_Text_Buffer.word_end = new_instancemethod(_fltk.Fl_Text_Buffer_word_end,None,Fl_Text_Buffer)
Fl_Text_Buffer.count_displayed_characters = new_instancemethod(_fltk.Fl_Text_Buffer_count_displayed_characters,None,Fl_Text_Buffer)
Fl_Text_Buffer.skip_displayed_characters = new_instancemethod(_fltk.Fl_Text_Buffer_skip_displayed_characters,None,Fl_Text_Buffer)
Fl_Text_Buffer.count_lines = new_instancemethod(_fltk.Fl_Text_Buffer_count_lines,None,Fl_Text_Buffer)
Fl_Text_Buffer.skip_lines = new_instancemethod(_fltk.Fl_Text_Buffer_skip_lines,None,Fl_Text_Buffer)
Fl_Text_Buffer.rewind_lines = new_instancemethod(_fltk.Fl_Text_Buffer_rewind_lines,None,Fl_Text_Buffer)
Fl_Text_Buffer.findchar_forward = new_instancemethod(_fltk.Fl_Text_Buffer_findchar_forward,None,Fl_Text_Buffer)
Fl_Text_Buffer.findchar_backward = new_instancemethod(_fltk.Fl_Text_Buffer_findchar_backward,None,Fl_Text_Buffer)
Fl_Text_Buffer.findchars_forward = new_instancemethod(_fltk.Fl_Text_Buffer_findchars_forward,None,Fl_Text_Buffer)
Fl_Text_Buffer.findchars_backward = new_instancemethod(_fltk.Fl_Text_Buffer_findchars_backward,None,Fl_Text_Buffer)
Fl_Text_Buffer.search_forward = new_instancemethod(_fltk.Fl_Text_Buffer_search_forward,None,Fl_Text_Buffer)
Fl_Text_Buffer.search_backward = new_instancemethod(_fltk.Fl_Text_Buffer_search_backward,None,Fl_Text_Buffer)
Fl_Text_Buffer.substitute_null_characters = new_instancemethod(_fltk.Fl_Text_Buffer_substitute_null_characters,None,Fl_Text_Buffer)
Fl_Text_Buffer.unsubstitute_null_characters = new_instancemethod(_fltk.Fl_Text_Buffer_unsubstitute_null_characters,None,Fl_Text_Buffer)
Fl_Text_Buffer.null_substitution_character = new_instancemethod(_fltk.Fl_Text_Buffer_null_substitution_character,None,Fl_Text_Buffer)
Fl_Text_Buffer.primary_selection = new_instancemethod(_fltk.Fl_Text_Buffer_primary_selection,None,Fl_Text_Buffer)
Fl_Text_Buffer.secondary_selection = new_instancemethod(_fltk.Fl_Text_Buffer_secondary_selection,None,Fl_Text_Buffer)
Fl_Text_Buffer.highlight_selection = new_instancemethod(_fltk.Fl_Text_Buffer_highlight_selection,None,Fl_Text_Buffer)
Fl_Text_Buffer.add_modify_callback = new_instancemethod(_fltk.Fl_Text_Buffer_add_modify_callback,None,Fl_Text_Buffer)
_fltk.Fl_Text_Buffer_swigregister(Fl_Text_Buffer)

Fl_Text_Buffer_expand_character = _fltk.Fl_Text_Buffer_expand_character

Fl_Text_Buffer_character_width = _fltk.Fl_Text_Buffer_character_width

class Fl_Text_Display(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Text_Display instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    NORMAL_CURSOR = _fltk.Fl_Text_Display_NORMAL_CURSOR
    CARET_CURSOR = _fltk.Fl_Text_Display_CARET_CURSOR
    DIM_CURSOR = _fltk.Fl_Text_Display_DIM_CURSOR
    BLOCK_CURSOR = _fltk.Fl_Text_Display_BLOCK_CURSOR
    HEAVY_CURSOR = _fltk.Fl_Text_Display_HEAVY_CURSOR
    CURSOR_POS = _fltk.Fl_Text_Display_CURSOR_POS
    CHARACTER_POS = _fltk.Fl_Text_Display_CHARACTER_POS
    DRAG_CHAR = _fltk.Fl_Text_Display_DRAG_CHAR
    DRAG_WORD = _fltk.Fl_Text_Display_DRAG_WORD
    DRAG_LINE = _fltk.Fl_Text_Display_DRAG_LINE
    ATTR_NONE = _fltk.Fl_Text_Display_ATTR_NONE
    ATTR_UNDERLINE = _fltk.Fl_Text_Display_ATTR_UNDERLINE
    ATTR_HIDDEN = _fltk.Fl_Text_Display_ATTR_HIDDEN
    def __init__(self, *args):
        if self.__class__ == Fl_Text_Display:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Text_Display(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Text_Display
    def handle(*args): return _fltk.Fl_Text_Display_handle(*args)
    def buffer(*args): return _fltk.Fl_Text_Display_buffer(*args)
    def redisplay_range(*args): return _fltk.Fl_Text_Display_redisplay_range(*args)
    def scroll(*args): return _fltk.Fl_Text_Display_scroll(*args)
    def insert(*args): return _fltk.Fl_Text_Display_insert(*args)
    def overstrike(*args): return _fltk.Fl_Text_Display_overstrike(*args)
    def insert_position(*args): return _fltk.Fl_Text_Display_insert_position(*args)
    def in_selection(*args): return _fltk.Fl_Text_Display_in_selection(*args)
    def show_insert_position(*args): return _fltk.Fl_Text_Display_show_insert_position(*args)
    def move_right(*args): return _fltk.Fl_Text_Display_move_right(*args)
    def move_left(*args): return _fltk.Fl_Text_Display_move_left(*args)
    def move_up(*args): return _fltk.Fl_Text_Display_move_up(*args)
    def move_down(*args): return _fltk.Fl_Text_Display_move_down(*args)
    def count_lines(*args): return _fltk.Fl_Text_Display_count_lines(*args)
    def line_start(*args): return _fltk.Fl_Text_Display_line_start(*args)
    def line_end(*args): return _fltk.Fl_Text_Display_line_end(*args)
    def skip_lines(*args): return _fltk.Fl_Text_Display_skip_lines(*args)
    def rewind_lines(*args): return _fltk.Fl_Text_Display_rewind_lines(*args)
    def next_word(*args): return _fltk.Fl_Text_Display_next_word(*args)
    def previous_word(*args): return _fltk.Fl_Text_Display_previous_word(*args)
    def show_cursor(*args): return _fltk.Fl_Text_Display_show_cursor(*args)
    def hide_cursor(*args): return _fltk.Fl_Text_Display_hide_cursor(*args)
    def cursor_style(*args): return _fltk.Fl_Text_Display_cursor_style(*args)
    def cursor_color(*args): return _fltk.Fl_Text_Display_cursor_color(*args)
    def scrollbar_width(*args): return _fltk.Fl_Text_Display_scrollbar_width(*args)
    def scrollbar_align(*args): return _fltk.Fl_Text_Display_scrollbar_align(*args)
    def word_start(*args): return _fltk.Fl_Text_Display_word_start(*args)
    def word_end(*args): return _fltk.Fl_Text_Display_word_end(*args)
    def position_style(*args): return _fltk.Fl_Text_Display_position_style(*args)
    def textfont(*args): return _fltk.Fl_Text_Display_textfont(*args)
    def textsize(*args): return _fltk.Fl_Text_Display_textsize(*args)
    def textcolor(*args): return _fltk.Fl_Text_Display_textcolor(*args)
    def wrapped_column(*args): return _fltk.Fl_Text_Display_wrapped_column(*args)
    def wrapped_row(*args): return _fltk.Fl_Text_Display_wrapped_row(*args)
    def wrap_mode(*args): return _fltk.Fl_Text_Display_wrap_mode(*args)
    def resize(*args): return _fltk.Fl_Text_Display_resize(*args)
    def draw(*args): return _fltk.Fl_Text_Display_draw(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Text_Display(self)
        return weakref_proxy(self)
Fl_Text_Display.handle = new_instancemethod(_fltk.Fl_Text_Display_handle,None,Fl_Text_Display)
Fl_Text_Display.buffer = new_instancemethod(_fltk.Fl_Text_Display_buffer,None,Fl_Text_Display)
Fl_Text_Display.redisplay_range = new_instancemethod(_fltk.Fl_Text_Display_redisplay_range,None,Fl_Text_Display)
Fl_Text_Display.scroll = new_instancemethod(_fltk.Fl_Text_Display_scroll,None,Fl_Text_Display)
Fl_Text_Display.insert = new_instancemethod(_fltk.Fl_Text_Display_insert,None,Fl_Text_Display)
Fl_Text_Display.overstrike = new_instancemethod(_fltk.Fl_Text_Display_overstrike,None,Fl_Text_Display)
Fl_Text_Display.insert_position = new_instancemethod(_fltk.Fl_Text_Display_insert_position,None,Fl_Text_Display)
Fl_Text_Display.in_selection = new_instancemethod(_fltk.Fl_Text_Display_in_selection,None,Fl_Text_Display)
Fl_Text_Display.show_insert_position = new_instancemethod(_fltk.Fl_Text_Display_show_insert_position,None,Fl_Text_Display)
Fl_Text_Display.move_right = new_instancemethod(_fltk.Fl_Text_Display_move_right,None,Fl_Text_Display)
Fl_Text_Display.move_left = new_instancemethod(_fltk.Fl_Text_Display_move_left,None,Fl_Text_Display)
Fl_Text_Display.move_up = new_instancemethod(_fltk.Fl_Text_Display_move_up,None,Fl_Text_Display)
Fl_Text_Display.move_down = new_instancemethod(_fltk.Fl_Text_Display_move_down,None,Fl_Text_Display)
Fl_Text_Display.count_lines = new_instancemethod(_fltk.Fl_Text_Display_count_lines,None,Fl_Text_Display)
Fl_Text_Display.line_start = new_instancemethod(_fltk.Fl_Text_Display_line_start,None,Fl_Text_Display)
Fl_Text_Display.line_end = new_instancemethod(_fltk.Fl_Text_Display_line_end,None,Fl_Text_Display)
Fl_Text_Display.skip_lines = new_instancemethod(_fltk.Fl_Text_Display_skip_lines,None,Fl_Text_Display)
Fl_Text_Display.rewind_lines = new_instancemethod(_fltk.Fl_Text_Display_rewind_lines,None,Fl_Text_Display)
Fl_Text_Display.next_word = new_instancemethod(_fltk.Fl_Text_Display_next_word,None,Fl_Text_Display)
Fl_Text_Display.previous_word = new_instancemethod(_fltk.Fl_Text_Display_previous_word,None,Fl_Text_Display)
Fl_Text_Display.show_cursor = new_instancemethod(_fltk.Fl_Text_Display_show_cursor,None,Fl_Text_Display)
Fl_Text_Display.hide_cursor = new_instancemethod(_fltk.Fl_Text_Display_hide_cursor,None,Fl_Text_Display)
Fl_Text_Display.cursor_style = new_instancemethod(_fltk.Fl_Text_Display_cursor_style,None,Fl_Text_Display)
Fl_Text_Display.cursor_color = new_instancemethod(_fltk.Fl_Text_Display_cursor_color,None,Fl_Text_Display)
Fl_Text_Display.scrollbar_width = new_instancemethod(_fltk.Fl_Text_Display_scrollbar_width,None,Fl_Text_Display)
Fl_Text_Display.scrollbar_align = new_instancemethod(_fltk.Fl_Text_Display_scrollbar_align,None,Fl_Text_Display)
Fl_Text_Display.word_start = new_instancemethod(_fltk.Fl_Text_Display_word_start,None,Fl_Text_Display)
Fl_Text_Display.word_end = new_instancemethod(_fltk.Fl_Text_Display_word_end,None,Fl_Text_Display)
Fl_Text_Display.position_style = new_instancemethod(_fltk.Fl_Text_Display_position_style,None,Fl_Text_Display)
Fl_Text_Display.textfont = new_instancemethod(_fltk.Fl_Text_Display_textfont,None,Fl_Text_Display)
Fl_Text_Display.textsize = new_instancemethod(_fltk.Fl_Text_Display_textsize,None,Fl_Text_Display)
Fl_Text_Display.textcolor = new_instancemethod(_fltk.Fl_Text_Display_textcolor,None,Fl_Text_Display)
Fl_Text_Display.wrapped_column = new_instancemethod(_fltk.Fl_Text_Display_wrapped_column,None,Fl_Text_Display)
Fl_Text_Display.wrapped_row = new_instancemethod(_fltk.Fl_Text_Display_wrapped_row,None,Fl_Text_Display)
Fl_Text_Display.wrap_mode = new_instancemethod(_fltk.Fl_Text_Display_wrap_mode,None,Fl_Text_Display)
Fl_Text_Display.resize = new_instancemethod(_fltk.Fl_Text_Display_resize,None,Fl_Text_Display)
Fl_Text_Display.draw = new_instancemethod(_fltk.Fl_Text_Display_draw,None,Fl_Text_Display)
_fltk.Fl_Text_Display_swigregister(Fl_Text_Display)

FL_TEXT_EDITOR_ANY_STATE = _fltk.FL_TEXT_EDITOR_ANY_STATE
class Fl_Text_Editor(Fl_Text_Display):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Text_Editor instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Text_Editor:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Text_Editor(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Text_Editor
    def handle(*args): return _fltk.Fl_Text_Editor_handle(*args)
    def insert_mode(*args): return _fltk.Fl_Text_Editor_insert_mode(*args)
    def add_key_binding(*args): return _fltk.Fl_Text_Editor_add_key_binding(*args)
    def remove_key_binding(*args): return _fltk.Fl_Text_Editor_remove_key_binding(*args)
    def remove_all_key_bindings(*args): return _fltk.Fl_Text_Editor_remove_all_key_bindings(*args)
    def bound_key_function(*args): return _fltk.Fl_Text_Editor_bound_key_function(*args)
    def default_key_function(*args): return _fltk.Fl_Text_Editor_default_key_function(*args)
    kf_default = staticmethod(_fltk.Fl_Text_Editor_kf_default)
    kf_ignore = staticmethod(_fltk.Fl_Text_Editor_kf_ignore)
    kf_backspace = staticmethod(_fltk.Fl_Text_Editor_kf_backspace)
    kf_enter = staticmethod(_fltk.Fl_Text_Editor_kf_enter)
    kf_move = staticmethod(_fltk.Fl_Text_Editor_kf_move)
    kf_shift_move = staticmethod(_fltk.Fl_Text_Editor_kf_shift_move)
    kf_ctrl_move = staticmethod(_fltk.Fl_Text_Editor_kf_ctrl_move)
    kf_c_s_move = staticmethod(_fltk.Fl_Text_Editor_kf_c_s_move)
    kf_home = staticmethod(_fltk.Fl_Text_Editor_kf_home)
    kf_end = staticmethod(_fltk.Fl_Text_Editor_kf_end)
    kf_left = staticmethod(_fltk.Fl_Text_Editor_kf_left)
    kf_up = staticmethod(_fltk.Fl_Text_Editor_kf_up)
    kf_right = staticmethod(_fltk.Fl_Text_Editor_kf_right)
    kf_down = staticmethod(_fltk.Fl_Text_Editor_kf_down)
    kf_page_up = staticmethod(_fltk.Fl_Text_Editor_kf_page_up)
    kf_page_down = staticmethod(_fltk.Fl_Text_Editor_kf_page_down)
    kf_insert = staticmethod(_fltk.Fl_Text_Editor_kf_insert)
    kf_delete = staticmethod(_fltk.Fl_Text_Editor_kf_delete)
    kf_copy = staticmethod(_fltk.Fl_Text_Editor_kf_copy)
    kf_cut = staticmethod(_fltk.Fl_Text_Editor_kf_cut)
    kf_paste = staticmethod(_fltk.Fl_Text_Editor_kf_paste)
    kf_select_all = staticmethod(_fltk.Fl_Text_Editor_kf_select_all)
    kf_undo = staticmethod(_fltk.Fl_Text_Editor_kf_undo)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Text_Editor(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Text_Editor_draw(*args)
Fl_Text_Editor.handle = new_instancemethod(_fltk.Fl_Text_Editor_handle,None,Fl_Text_Editor)
Fl_Text_Editor.insert_mode = new_instancemethod(_fltk.Fl_Text_Editor_insert_mode,None,Fl_Text_Editor)
Fl_Text_Editor.add_key_binding = new_instancemethod(_fltk.Fl_Text_Editor_add_key_binding,None,Fl_Text_Editor)
Fl_Text_Editor.remove_key_binding = new_instancemethod(_fltk.Fl_Text_Editor_remove_key_binding,None,Fl_Text_Editor)
Fl_Text_Editor.remove_all_key_bindings = new_instancemethod(_fltk.Fl_Text_Editor_remove_all_key_bindings,None,Fl_Text_Editor)
Fl_Text_Editor.bound_key_function = new_instancemethod(_fltk.Fl_Text_Editor_bound_key_function,None,Fl_Text_Editor)
Fl_Text_Editor.default_key_function = new_instancemethod(_fltk.Fl_Text_Editor_default_key_function,None,Fl_Text_Editor)
Fl_Text_Editor.draw = new_instancemethod(_fltk.Fl_Text_Editor_draw,None,Fl_Text_Editor)
_fltk.Fl_Text_Editor_swigregister(Fl_Text_Editor)

Fl_Text_Editor_kf_default = _fltk.Fl_Text_Editor_kf_default

Fl_Text_Editor_kf_ignore = _fltk.Fl_Text_Editor_kf_ignore

Fl_Text_Editor_kf_backspace = _fltk.Fl_Text_Editor_kf_backspace

Fl_Text_Editor_kf_enter = _fltk.Fl_Text_Editor_kf_enter

Fl_Text_Editor_kf_move = _fltk.Fl_Text_Editor_kf_move

Fl_Text_Editor_kf_shift_move = _fltk.Fl_Text_Editor_kf_shift_move

Fl_Text_Editor_kf_ctrl_move = _fltk.Fl_Text_Editor_kf_ctrl_move

Fl_Text_Editor_kf_c_s_move = _fltk.Fl_Text_Editor_kf_c_s_move

Fl_Text_Editor_kf_home = _fltk.Fl_Text_Editor_kf_home

Fl_Text_Editor_kf_end = _fltk.Fl_Text_Editor_kf_end

Fl_Text_Editor_kf_left = _fltk.Fl_Text_Editor_kf_left

Fl_Text_Editor_kf_up = _fltk.Fl_Text_Editor_kf_up

Fl_Text_Editor_kf_right = _fltk.Fl_Text_Editor_kf_right

Fl_Text_Editor_kf_down = _fltk.Fl_Text_Editor_kf_down

Fl_Text_Editor_kf_page_up = _fltk.Fl_Text_Editor_kf_page_up

Fl_Text_Editor_kf_page_down = _fltk.Fl_Text_Editor_kf_page_down

Fl_Text_Editor_kf_insert = _fltk.Fl_Text_Editor_kf_insert

Fl_Text_Editor_kf_delete = _fltk.Fl_Text_Editor_kf_delete

Fl_Text_Editor_kf_copy = _fltk.Fl_Text_Editor_kf_copy

Fl_Text_Editor_kf_cut = _fltk.Fl_Text_Editor_kf_cut

Fl_Text_Editor_kf_paste = _fltk.Fl_Text_Editor_kf_paste

Fl_Text_Editor_kf_select_all = _fltk.Fl_Text_Editor_kf_select_all

Fl_Text_Editor_kf_undo = _fltk.Fl_Text_Editor_kf_undo

class Fl_Tile(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Tile instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Tile:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Tile(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def position(*args): return _fltk.Fl_Tile_position(*args)
    __swig_destroy__ = _fltk.delete_Fl_Tile
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Tile(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Tile_draw(*args)
Fl_Tile.position = new_instancemethod(_fltk.Fl_Tile_position,None,Fl_Tile)
Fl_Tile.draw = new_instancemethod(_fltk.Fl_Tile_draw,None,Fl_Tile)
_fltk.Fl_Tile_swigregister(Fl_Tile)

class Fl_Tiled_Image(Fl_Image):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Tiled_Image instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Tiled_Image:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Tiled_Image(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Tiled_Image
    def copy(*args): return _fltk.Fl_Tiled_Image_copy(*args)
    def color_average(*args): return _fltk.Fl_Tiled_Image_color_average(*args)
    def desaturate(*args): return _fltk.Fl_Tiled_Image_desaturate(*args)
    def draw(*args): return _fltk.Fl_Tiled_Image_draw(*args)
    def image(*args): return _fltk.Fl_Tiled_Image_image(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Tiled_Image(self)
        return weakref_proxy(self)
Fl_Tiled_Image.copy = new_instancemethod(_fltk.Fl_Tiled_Image_copy,None,Fl_Tiled_Image)
Fl_Tiled_Image.color_average = new_instancemethod(_fltk.Fl_Tiled_Image_color_average,None,Fl_Tiled_Image)
Fl_Tiled_Image.desaturate = new_instancemethod(_fltk.Fl_Tiled_Image_desaturate,None,Fl_Tiled_Image)
Fl_Tiled_Image.draw = new_instancemethod(_fltk.Fl_Tiled_Image_draw,None,Fl_Tiled_Image)
Fl_Tiled_Image.image = new_instancemethod(_fltk.Fl_Tiled_Image_image,None,Fl_Tiled_Image)
_fltk.Fl_Tiled_Image_swigregister(Fl_Tiled_Image)

FL_NORMAL_TIMER = _fltk.FL_NORMAL_TIMER
FL_VALUE_TIMER = _fltk.FL_VALUE_TIMER
FL_HIDDEN_TIMER = _fltk.FL_HIDDEN_TIMER
class Fl_Timer(Fl_Widget):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Timer instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def draw(*args): return _fltk.Fl_Timer_draw(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Timer:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Timer(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Timer
    def value(*args): return _fltk.Fl_Timer_value(*args)
    def direction(*args): return _fltk.Fl_Timer_direction(*args)
    def suspended(*args): return _fltk.Fl_Timer_suspended(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Timer(self)
        return weakref_proxy(self)
Fl_Timer.draw = new_instancemethod(_fltk.Fl_Timer_draw,None,Fl_Timer)
Fl_Timer.value = new_instancemethod(_fltk.Fl_Timer_value,None,Fl_Timer)
Fl_Timer.direction = new_instancemethod(_fltk.Fl_Timer_direction,None,Fl_Timer)
Fl_Timer.suspended = new_instancemethod(_fltk.Fl_Timer_suspended,None,Fl_Timer)
_fltk.Fl_Timer_swigregister(Fl_Timer)

class Fl_Toggle_Button(Fl_Button):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Toggle_Button instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Toggle_Button:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Toggle_Button(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Toggle_Button
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Toggle_Button(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Toggle_Button_draw(*args)
Fl_Toggle_Button.draw = new_instancemethod(_fltk.Fl_Toggle_Button_draw,None,Fl_Toggle_Button)
_fltk.Fl_Toggle_Button_swigregister(Fl_Toggle_Button)

class Fl_Tooltip(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Tooltip instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    delay = staticmethod(_fltk.Fl_Tooltip_delay)
    hoverdelay = staticmethod(_fltk.Fl_Tooltip_hoverdelay)
    enabled = staticmethod(_fltk.Fl_Tooltip_enabled)
    enable = staticmethod(_fltk.Fl_Tooltip_enable)
    disable = staticmethod(_fltk.Fl_Tooltip_disable)
    enter = property(_fltk.Fl_Tooltip_enter_get, _fltk.Fl_Tooltip_enter_set)
    enter_area = staticmethod(_fltk.Fl_Tooltip_enter_area)
    exit = property(_fltk.Fl_Tooltip_exit_get, _fltk.Fl_Tooltip_exit_set)
    current = staticmethod(_fltk.Fl_Tooltip_current)
    font = staticmethod(_fltk.Fl_Tooltip_font)
    size = staticmethod(_fltk.Fl_Tooltip_size)
    color = staticmethod(_fltk.Fl_Tooltip_color)
    textcolor = staticmethod(_fltk.Fl_Tooltip_textcolor)
    enter_ = staticmethod(_fltk.Fl_Tooltip_enter_)
    exit_ = staticmethod(_fltk.Fl_Tooltip_exit_)
    def __init__(self, *args):
        this = _fltk.new_Fl_Tooltip(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Tooltip
_fltk.Fl_Tooltip_swigregister(Fl_Tooltip)

Fl_Tooltip_delay = _fltk.Fl_Tooltip_delay

Fl_Tooltip_hoverdelay = _fltk.Fl_Tooltip_hoverdelay

Fl_Tooltip_enabled = _fltk.Fl_Tooltip_enabled

Fl_Tooltip_enable = _fltk.Fl_Tooltip_enable

Fl_Tooltip_disable = _fltk.Fl_Tooltip_disable

Fl_Tooltip_enter_area = _fltk.Fl_Tooltip_enter_area

Fl_Tooltip_current = _fltk.Fl_Tooltip_current

Fl_Tooltip_font = _fltk.Fl_Tooltip_font

Fl_Tooltip_size = _fltk.Fl_Tooltip_size

Fl_Tooltip_color = _fltk.Fl_Tooltip_color

Fl_Tooltip_textcolor = _fltk.Fl_Tooltip_textcolor

Fl_Tooltip_enter_ = _fltk.Fl_Tooltip_enter_

Fl_Tooltip_exit_ = _fltk.Fl_Tooltip_exit_

class Fl_Value_Output(Fl_Valuator):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Value_Output instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Value_Output:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Value_Output(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def soft(*args): return _fltk.Fl_Value_Output_soft(*args)
    def textfont(*args): return _fltk.Fl_Value_Output_textfont(*args)
    def textsize(*args): return _fltk.Fl_Value_Output_textsize(*args)
    def textcolor(*args): return _fltk.Fl_Value_Output_textcolor(*args)
    __swig_destroy__ = _fltk.delete_Fl_Value_Output
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Value_Output(self)
        return weakref_proxy(self)
Fl_Value_Output.soft = new_instancemethod(_fltk.Fl_Value_Output_soft,None,Fl_Value_Output)
Fl_Value_Output.textfont = new_instancemethod(_fltk.Fl_Value_Output_textfont,None,Fl_Value_Output)
Fl_Value_Output.textsize = new_instancemethod(_fltk.Fl_Value_Output_textsize,None,Fl_Value_Output)
Fl_Value_Output.textcolor = new_instancemethod(_fltk.Fl_Value_Output_textcolor,None,Fl_Value_Output)
_fltk.Fl_Value_Output_swigregister(Fl_Value_Output)

class Fl_Wizard(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Wizard instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_Wizard:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Wizard(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def next(*args): return _fltk.Fl_Wizard_next(*args)
    def prev(*args): return _fltk.Fl_Wizard_prev(*args)
    def value(*args): return _fltk.Fl_Wizard_value(*args)
    __swig_destroy__ = _fltk.delete_Fl_Wizard
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Wizard(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Wizard_draw(*args)
Fl_Wizard.next = new_instancemethod(_fltk.Fl_Wizard_next,None,Fl_Wizard)
Fl_Wizard.prev = new_instancemethod(_fltk.Fl_Wizard_prev,None,Fl_Wizard)
Fl_Wizard.value = new_instancemethod(_fltk.Fl_Wizard_value,None,Fl_Wizard)
Fl_Wizard.draw = new_instancemethod(_fltk.Fl_Wizard_draw,None,Fl_Wizard)
_fltk.Fl_Wizard_swigregister(Fl_Wizard)

class Fl_XBM_Image(Fl_Bitmap):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_XBM_Image instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_XBM_Image:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_XBM_Image(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_XBM_Image
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_XBM_Image(self)
        return weakref_proxy(self)
_fltk.Fl_XBM_Image_swigregister(Fl_XBM_Image)

class Fl_XPM_Image(Fl_Pixmap):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_XPM_Image instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == Fl_XPM_Image:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_XPM_Image(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_XPM_Image
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_XPM_Image(self)
        return weakref_proxy(self)
_fltk.Fl_XPM_Image_swigregister(Fl_XPM_Image)


fl_xid = _fltk.fl_xid
class ListSelect(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ ListSelect instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    def __init__(self, *args):
        if self.__class__ == ListSelect:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_ListSelect(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    def getTopBrowser(*args): return _fltk.ListSelect_getTopBrowser(*args)
    def getBottomBrowser(*args): return _fltk.ListSelect_getBottomBrowser(*args)
    def resize(*args): return _fltk.ListSelect_resize(*args)
    __swig_destroy__ = _fltk.delete_ListSelect
    def __disown__(self):
        self.this.disown()
        _fltk.disown_ListSelect(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.ListSelect_draw(*args)
ListSelect.getTopBrowser = new_instancemethod(_fltk.ListSelect_getTopBrowser,None,ListSelect)
ListSelect.getBottomBrowser = new_instancemethod(_fltk.ListSelect_getBottomBrowser,None,ListSelect)
ListSelect.resize = new_instancemethod(_fltk.ListSelect_resize,None,ListSelect)
ListSelect.draw = new_instancemethod(_fltk.ListSelect_draw,None,ListSelect)
_fltk.ListSelect_swigregister(ListSelect)

upCB = _fltk.upCB

downCB = _fltk.downCB

toggleCB = _fltk.toggleCB

class Fl_Table(Fl_Group):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Table instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    CONTEXT_NONE = _fltk.Fl_Table_CONTEXT_NONE
    CONTEXT_STARTPAGE = _fltk.Fl_Table_CONTEXT_STARTPAGE
    CONTEXT_ENDPAGE = _fltk.Fl_Table_CONTEXT_ENDPAGE
    CONTEXT_ROW_HEADER = _fltk.Fl_Table_CONTEXT_ROW_HEADER
    CONTEXT_COL_HEADER = _fltk.Fl_Table_CONTEXT_COL_HEADER
    CONTEXT_CELL = _fltk.Fl_Table_CONTEXT_CELL
    CONTEXT_TABLE = _fltk.Fl_Table_CONTEXT_TABLE
    CONTEXT_RC_RESIZE = _fltk.Fl_Table_CONTEXT_RC_RESIZE
    def handle(*args): return _fltk.Fl_Table_handle(*args)
    def draw(*args): return _fltk.Fl_Table_draw(*args)
    def draw_cell(*args): return _fltk.Fl_Table_draw_cell(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Table:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Table(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Table
    def clear(*args): return _fltk.Fl_Table_clear(*args)
    def table_box(*args): return _fltk.Fl_Table_table_box(*args)
    def rows(*args): return _fltk.Fl_Table_rows(*args)
    def cols(*args): return _fltk.Fl_Table_cols(*args)
    def visible_cells(*args): return _fltk.Fl_Table_visible_cells(*args)
    def is_interactive_resize(*args): return _fltk.Fl_Table_is_interactive_resize(*args)
    def row_resize(*args): return _fltk.Fl_Table_row_resize(*args)
    def col_resize(*args): return _fltk.Fl_Table_col_resize(*args)
    def col_resize_min(*args): return _fltk.Fl_Table_col_resize_min(*args)
    def row_resize_min(*args): return _fltk.Fl_Table_row_resize_min(*args)
    def row_header(*args): return _fltk.Fl_Table_row_header(*args)
    def col_header(*args): return _fltk.Fl_Table_col_header(*args)
    def col_header_height(*args): return _fltk.Fl_Table_col_header_height(*args)
    def row_header_width(*args): return _fltk.Fl_Table_row_header_width(*args)
    def row_header_color(*args): return _fltk.Fl_Table_row_header_color(*args)
    def col_header_color(*args): return _fltk.Fl_Table_col_header_color(*args)
    def row_height(*args): return _fltk.Fl_Table_row_height(*args)
    def col_width(*args): return _fltk.Fl_Table_col_width(*args)
    def row_height_all(*args): return _fltk.Fl_Table_row_height_all(*args)
    def col_width_all(*args): return _fltk.Fl_Table_col_width_all(*args)
    def row_position(*args): return _fltk.Fl_Table_row_position(*args)
    def col_position(*args): return _fltk.Fl_Table_col_position(*args)
    def top_row(*args): return _fltk.Fl_Table_top_row(*args)
    def is_selected(*args): return _fltk.Fl_Table_is_selected(*args)
    def get_selection(*args): return _fltk.Fl_Table_get_selection(*args)
    def set_selection(*args): return _fltk.Fl_Table_set_selection(*args)
    def move_cursor(*args): return _fltk.Fl_Table_move_cursor(*args)
    def init_sizes(*args): return _fltk.Fl_Table_init_sizes(*args)
    def add(*args): return _fltk.Fl_Table_add(*args)
    def insert(*args): return _fltk.Fl_Table_insert(*args)
    def insert_before(*args): return _fltk.Fl_Table_insert_before(*args)
    def begin(*args): return _fltk.Fl_Table_begin(*args)
    def end(*args): return _fltk.Fl_Table_end(*args)
    def child(*args): return _fltk.Fl_Table_child(*args)
    def children(*args): return _fltk.Fl_Table_children(*args)
    def find(*args): return _fltk.Fl_Table_find(*args)
    def callback_row(*args): return _fltk.Fl_Table_callback_row(*args)
    def callback_col(*args): return _fltk.Fl_Table_callback_col(*args)
    def callback_context(*args): return _fltk.Fl_Table_callback_context(*args)
    def do_callback(*args): return _fltk.Fl_Table_do_callback(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Table(self)
        return weakref_proxy(self)
Fl_Table.handle = new_instancemethod(_fltk.Fl_Table_handle,None,Fl_Table)
Fl_Table.draw = new_instancemethod(_fltk.Fl_Table_draw,None,Fl_Table)
Fl_Table.draw_cell = new_instancemethod(_fltk.Fl_Table_draw_cell,None,Fl_Table)
Fl_Table.clear = new_instancemethod(_fltk.Fl_Table_clear,None,Fl_Table)
Fl_Table.table_box = new_instancemethod(_fltk.Fl_Table_table_box,None,Fl_Table)
Fl_Table.rows = new_instancemethod(_fltk.Fl_Table_rows,None,Fl_Table)
Fl_Table.cols = new_instancemethod(_fltk.Fl_Table_cols,None,Fl_Table)
Fl_Table.visible_cells = new_instancemethod(_fltk.Fl_Table_visible_cells,None,Fl_Table)
Fl_Table.is_interactive_resize = new_instancemethod(_fltk.Fl_Table_is_interactive_resize,None,Fl_Table)
Fl_Table.row_resize = new_instancemethod(_fltk.Fl_Table_row_resize,None,Fl_Table)
Fl_Table.col_resize = new_instancemethod(_fltk.Fl_Table_col_resize,None,Fl_Table)
Fl_Table.col_resize_min = new_instancemethod(_fltk.Fl_Table_col_resize_min,None,Fl_Table)
Fl_Table.row_resize_min = new_instancemethod(_fltk.Fl_Table_row_resize_min,None,Fl_Table)
Fl_Table.row_header = new_instancemethod(_fltk.Fl_Table_row_header,None,Fl_Table)
Fl_Table.col_header = new_instancemethod(_fltk.Fl_Table_col_header,None,Fl_Table)
Fl_Table.col_header_height = new_instancemethod(_fltk.Fl_Table_col_header_height,None,Fl_Table)
Fl_Table.row_header_width = new_instancemethod(_fltk.Fl_Table_row_header_width,None,Fl_Table)
Fl_Table.row_header_color = new_instancemethod(_fltk.Fl_Table_row_header_color,None,Fl_Table)
Fl_Table.col_header_color = new_instancemethod(_fltk.Fl_Table_col_header_color,None,Fl_Table)
Fl_Table.row_height = new_instancemethod(_fltk.Fl_Table_row_height,None,Fl_Table)
Fl_Table.col_width = new_instancemethod(_fltk.Fl_Table_col_width,None,Fl_Table)
Fl_Table.row_height_all = new_instancemethod(_fltk.Fl_Table_row_height_all,None,Fl_Table)
Fl_Table.col_width_all = new_instancemethod(_fltk.Fl_Table_col_width_all,None,Fl_Table)
Fl_Table.row_position = new_instancemethod(_fltk.Fl_Table_row_position,None,Fl_Table)
Fl_Table.col_position = new_instancemethod(_fltk.Fl_Table_col_position,None,Fl_Table)
Fl_Table.top_row = new_instancemethod(_fltk.Fl_Table_top_row,None,Fl_Table)
Fl_Table.is_selected = new_instancemethod(_fltk.Fl_Table_is_selected,None,Fl_Table)
Fl_Table.get_selection = new_instancemethod(_fltk.Fl_Table_get_selection,None,Fl_Table)
Fl_Table.set_selection = new_instancemethod(_fltk.Fl_Table_set_selection,None,Fl_Table)
Fl_Table.move_cursor = new_instancemethod(_fltk.Fl_Table_move_cursor,None,Fl_Table)
Fl_Table.init_sizes = new_instancemethod(_fltk.Fl_Table_init_sizes,None,Fl_Table)
Fl_Table.add = new_instancemethod(_fltk.Fl_Table_add,None,Fl_Table)
Fl_Table.insert = new_instancemethod(_fltk.Fl_Table_insert,None,Fl_Table)
Fl_Table.insert_before = new_instancemethod(_fltk.Fl_Table_insert_before,None,Fl_Table)
Fl_Table.begin = new_instancemethod(_fltk.Fl_Table_begin,None,Fl_Table)
Fl_Table.end = new_instancemethod(_fltk.Fl_Table_end,None,Fl_Table)
Fl_Table.child = new_instancemethod(_fltk.Fl_Table_child,None,Fl_Table)
Fl_Table.children = new_instancemethod(_fltk.Fl_Table_children,None,Fl_Table)
Fl_Table.find = new_instancemethod(_fltk.Fl_Table_find,None,Fl_Table)
Fl_Table.callback_row = new_instancemethod(_fltk.Fl_Table_callback_row,None,Fl_Table)
Fl_Table.callback_col = new_instancemethod(_fltk.Fl_Table_callback_col,None,Fl_Table)
Fl_Table.callback_context = new_instancemethod(_fltk.Fl_Table_callback_context,None,Fl_Table)
Fl_Table.do_callback = new_instancemethod(_fltk.Fl_Table_do_callback,None,Fl_Table)
_fltk.Fl_Table_swigregister(Fl_Table)

class Fl_Table_Row(Fl_Table):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __repr__(self):
        try: strthis = "at 0x%x" %( self.this, ) 
        except: strthis = "" 
        return "<%s.%s; proxy of C++ Fl_Table_Row instance %s>" % (self.__class__.__module__, self.__class__.__name__, strthis,)
    SELECT_NONE = _fltk.Fl_Table_Row_SELECT_NONE
    SELECT_SINGLE = _fltk.Fl_Table_Row_SELECT_SINGLE
    SELECT_MULTI = _fltk.Fl_Table_Row_SELECT_MULTI
    def handle(*args): return _fltk.Fl_Table_Row_handle(*args)
    def find_cell(*args): return _fltk.Fl_Table_Row_find_cell(*args)
    def __init__(self, *args):
        if self.__class__ == Fl_Table_Row:
            args = (None,) + args
        else:
            args = (self,) + args
        this = _fltk.new_Fl_Table_Row(*args)
        this.own(0)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _fltk.delete_Fl_Table_Row
    def rows(*args): return _fltk.Fl_Table_Row_rows(*args)
    def type(*args): return _fltk.Fl_Table_Row_type(*args)
    def row_selected(*args): return _fltk.Fl_Table_Row_row_selected(*args)
    def select_row(*args): return _fltk.Fl_Table_Row_select_row(*args)
    def select_all_rows(*args): return _fltk.Fl_Table_Row_select_all_rows(*args)
    def __disown__(self):
        self.this.disown()
        _fltk.disown_Fl_Table_Row(self)
        return weakref_proxy(self)
    def draw(*args): return _fltk.Fl_Table_Row_draw(*args)
    def draw_cell(*args): return _fltk.Fl_Table_Row_draw_cell(*args)
Fl_Table_Row.handle = new_instancemethod(_fltk.Fl_Table_Row_handle,None,Fl_Table_Row)
Fl_Table_Row.find_cell = new_instancemethod(_fltk.Fl_Table_Row_find_cell,None,Fl_Table_Row)
Fl_Table_Row.rows = new_instancemethod(_fltk.Fl_Table_Row_rows,None,Fl_Table_Row)
Fl_Table_Row.type = new_instancemethod(_fltk.Fl_Table_Row_type,None,Fl_Table_Row)
Fl_Table_Row.row_selected = new_instancemethod(_fltk.Fl_Table_Row_row_selected,None,Fl_Table_Row)
Fl_Table_Row.select_row = new_instancemethod(_fltk.Fl_Table_Row_select_row,None,Fl_Table_Row)
Fl_Table_Row.select_all_rows = new_instancemethod(_fltk.Fl_Table_Row_select_all_rows,None,Fl_Table_Row)
Fl_Table_Row.draw = new_instancemethod(_fltk.Fl_Table_Row_draw,None,Fl_Table_Row)
Fl_Table_Row.draw_cell = new_instancemethod(_fltk.Fl_Table_Row_draw_cell,None,Fl_Table_Row)
_fltk.Fl_Table_Row_swigregister(Fl_Table_Row)


gl_start = _fltk.gl_start

gl_finish = _fltk.gl_finish

gl_color = _fltk.gl_color

gl_rect = _fltk.gl_rect

gl_rectf = _fltk.gl_rectf

gl_font = _fltk.gl_font

gl_height = _fltk.gl_height

gl_descent = _fltk.gl_descent

gl_measure = _fltk.gl_measure

gl_draw_image = _fltk.gl_draw_image

glLoadIdentity = _fltk.glLoadIdentity

glViewport = _fltk.glViewport

glClear = _fltk.glClear

glColor3f = _fltk.glColor3f

glBegin = _fltk.glBegin

glEnd = _fltk.glEnd

glVertex3f = _fltk.glVertex3f
M_PI = _fltk.M_PI
M_PI_2 = _fltk.M_PI_2
M_PI_4 = _fltk.M_PI_4
M_1_PI = _fltk.M_1_PI
M_2_PI = _fltk.M_2_PI
M_SQRT2 = _fltk.M_SQRT2
M_SQRT1_2 = _fltk.M_SQRT1_2

castWidget2Window = _fltk.castWidget2Window

castWidget2Menu = _fltk.castWidget2Menu

castWidget2Menu_ = _fltk.castWidget2Menu_

castWidget2Btn = _fltk.castWidget2Btn

castWidget2Browser = _fltk.castWidget2Browser

castWidget2Slider = _fltk.castWidget2Slider

castWidget2FileChooser = _fltk.castWidget2FileChooser

castWidget2Dial = _fltk.castWidget2Dial

castWidget2Box = _fltk.castWidget2Box

castWidget2Adjuster = _fltk.castWidget2Adjuster

castWidget2Valuator = _fltk.castWidget2Valuator

castWidget2Scrollbar = _fltk.castWidget2Scrollbar

castWidget2Scroll = _fltk.castWidget2Scroll
__idleCallbacks = []
def Fl_add_idle( func, data=None):
    __idleCallbacks.append( (func, data) )
    if len(__idleCallbacks) == 1:
        pyFLTK_controlIdleCallbacks(1)

def Fl_remove_idle( func, data=None):
    for cb in __idleCallbacks:
        if cb == ( func, data ):
            __idleCallbacks.remove(cb)
            break

def pyFLTK_doIdleCallbacks():
    for cb in __idleCallbacks:
        cb[0](cb[1])

pyFLTK_registerDoIdle(pyFLTK_doIdleCallbacks)


Fl.add_idle = staticmethod(Fl_add_idle)
Fl.remove_idle = staticmethod(Fl_remove_idle)



def __Fl_WidgetCallback(self,*args):
	import string
        type_name = repr(type(self))
        start_pos = string.find(type_name, 'fltk.')+len('fltk.')
        end_pos = string.rfind(type_name, "'")
        type_string = type_name[start_pos:end_pos]+" *"
        if len(args) == 1:
            new_args = (self, type_string, args[0])
        else:
            new_args = (self, type_string, args[0], args[1])
        return apply(_fltk.Fl_Widget_callback,new_args)

Fl_Widget.callback = __Fl_WidgetCallback


def __Fl_Text_BufferAddModifyCallback(self,*args):
	import string
        type_name = repr(type(self))
        start_pos = string.find(type_name, 'fltk.')+len('fltk.')
        end_pos = string.rfind(type_name, "'")
        type_string = type_name[start_pos:end_pos]+" *"
        if len(args) == 1:
            new_args = (self, type_string, args[0])
        else:
            new_args = (self, type_string, args[0], args[1])
        return apply(_fltk.Fl_Text_Buffer_add_modify_callback,new_args)

Fl_Text_Buffer.add_modify_callback = __Fl_Text_BufferAddModifyCallback


def __Fl_Help_ViewLink(self,*args):
	import string
        type_name = repr(type(self))
        start_pos = string.find(type_name, 'fltk.')+len('fltk.')
        end_pos = string.rfind(type_name, "'")
        type_string = type_name[start_pos:end_pos]+" *"
        if len(args) == 1:
            new_args = (self, type_string, args[0])
        else:
            new_args = (self, type_string, args[0], args[1])
        return apply(_fltk.Fl_Help_View_link,new_args)

Fl_Help_View.link = __Fl_Help_ViewLink


Fl.add_timeout = staticmethod(Fl_add_timeout)
Fl.add_check = staticmethod(Fl_add_check)
Fl.remove_check = staticmethod(Fl_remove_check)
Fl.add_handler = staticmethod(Fl_add_handler)
Fl.remove_handler = staticmethod(Fl_remove_handler)



gl_width = _fltk.gl_width

gl_draw = _fltk.gl_draw
setMenu = _fltk.setMenu


