import random
import sys

def tokenize(str):
	i1 = 0
	i2 = -1
	tokens = []
	token = ''
	for c in str:
		i2 = i2 + 1
		if c.isalpha() or ord(c)>127:
			None
		else:
			if i1 != i2:
				token = str[i1:i2]
				tokens.append(token)
			i1 = i2+1
			tokens.append(c)

	if i1 != i2+1:
		token = str[i1:]
		tokens.append(token)
	return tokens

def scramble(str):
	if len(str)>2:
		s = str[1:-1]
		a = []
		for c in s: a.append(c)
		random.shuffle(a)
		s = ''
		for c in a: s = s + c
		str2 = str[0] + s + str[-1]
		str = str2
	return str

def scramble_text(text):
	tokens = tokenize(text)
	for t in tokens:
		sys.stdout.write(scramble(t))

line =  sys.stdin.readline()
while line != '':
	scramble_text(line)
	line =  sys.stdin.readline()

