# implementation of a diff between 2 strings

source = 'ABCDEFGH'
print 'source=', source
source_len = len(source)

# destination string
#dest = '123456789'
dest = 'ABCDxEFGH'
print 'destination=', dest
dest_len = len(dest)

# matrix of Levenshtein distance
d = []
for i in range(0, source_len+1):
    d.append([ 0 ] * (dest_len+1))

for i in range(0, source_len+1):
    d[i][0] = i

for j in range(0, dest_len+1):
    d[0][j] = j

for i in range(0, source_len):
    for j in range(0, dest_len):
        if source[i] == dest[j] : d[i+1][j+1] = d[i][j]
        else : d[i+1][j+1] = min(d[i][j+1], d[i+1][j])+1

print 'Levenshtein matrix done.'
print 'distance=', d[source_len][dest_len]
#print d

# following the path starting from the end
stack = []
j = dest_len
i = source_len
while i>0 and j>0 :
    if source[i-1] == dest[j-1] :
        stack.insert(0, ['=', source[i-1]])
        j = j-1
        i = i-1
    else :
        # find the best cell
        if d[i-1][j] < d[i][j-1] :
            stack.insert(0, ['-', source[i-1]])
            i = i-1
        else :
            stack.insert(0, ['+', dest[j-1]])
            j = j-1

if i>0 : # source characters to be removed
    stack.insert(0, ['-', source[0:i-1]])
if j>0 : # dest characters to be added
    stack.insert(0, ['+', dest[0:j-1]])

# print the result
previous = None
result = ''
for v in stack:
    if previous != None:
        if previous != v[0]:
            result = result + '\n' + v[0] + ' '
            previous = v[0]
        result = result + v[1]
    else:
        result = result + v[0] + ' ' + v[1]
        previous = v[0]

print result

