# Simple demo recipe

NAMES = "alice bob charlie"
AGE_alice = "42"

X ?= "X10"
X += "X12"
X:append = " X13"

python() {
    bb.warn("hello world")
    for name in d.getVar('NAMES').split():
        age = d.getVar('AGE_%s' % name)
        bb.warn("name=%s, age=%s" % (name, age))
    bb.warn("X=%s" % (d.getVar('X')))
}

python do_xx() {
    bb.warn("do_xx")
}

addtask do_xx before do_build
do_xx[vardeps] = "SOME_PARAMETER_X"

