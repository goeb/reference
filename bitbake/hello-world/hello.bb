# Simple demo recipe

NAMES = "alice bob charlie"
AGE_alice = "42"

python() {
    bb.warn("hello world")
    for name in d.getVar('NAMES').split():
        age = d.getVar('AGE_%s' % name)
        bb.warn("name=%s, age=%s" % (name, age))
}
