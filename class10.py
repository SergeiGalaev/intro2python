from random import randint
l = []
s = 0
for x in range(10):
	l.append(randint(0,102))
	s += x
	print s
	if s/10>5:
		l.reverse()

print l