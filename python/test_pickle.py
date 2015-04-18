#!/usr/bin/python

import pickle

f=open("xx", "w")
for i in range(1, 10000) :
	x = (i, "sample_"+str(i)+".jpg", "cdrom1", "/images/people", "people", ("fred", "man"))
	pickle.dump(x, f)
