
inherit_defer ${TEST1}

A = "This is A"
TEST1 = "test1"

inherit_defer test2

python() {
    bb.warn("in test-inherit.bb...")
}

inherit test3
