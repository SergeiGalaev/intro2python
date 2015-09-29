from random import randint

print "Ygadai 4islo kotoroe ya zagadal"
print "Vvedite predel 4isel"

n = int(raw_input(">"))
x = randint(0,n)
logic = 0
print "Vvedite koli4estvo popitok"
p = int(raw_input(">"))

while (logic !=1):
	print "Vvedite 4islo kotoroe vi pridymali"
	h = int(raw_input(">"))
	if h == x:
		print "Vi pravi"
		print "Vi ygadali 4islo za", popitka, "popitki"
		logic = 1
	#if popitka > p:
		#print "Y vas zakon4ilis' popitki", break
	else:
		print "Poprobuite eshe raz"
	popitka+=1
	