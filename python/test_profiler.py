
import cProfile



def f(x) :
    if x < 1:
        return 1
    else :
        y = x*f(x-1)
        return y

def g() :
    for i in range(0, 100000):
        ii =  f(i%100)

cProfile.run('g()')
