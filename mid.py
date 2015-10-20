from random import randint
l = []
l2 = []
for x in range(10):
	l.append(randint(0,10))
print l

sum1 = 0
for x in l:
	sum1 += x
abs1 = sum1/10
print abs1
 
if abs1 >= 5:
	l.reverse()
	print l
else:
	for x in l:
		x = x*2
		l2.append(x)
	print l2