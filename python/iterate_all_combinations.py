
# 'abc'
# => 'abc'
#    'acb'
#    'bac'
#    'bca'
#    'cab'
#    'cba'

def all_combinations(prefix, alist):
    if (len(alist) == 1):
        print(prefix + alist[0])

    for i in range(len(alist)):
        L1 = alist[:]
        first = L1.pop(i)
        all_combinations(prefix + first, L1)

all_combinations('', list('abc'))
all_combinations('', list('abcd'))
all_combinations('', list('abcde'))
