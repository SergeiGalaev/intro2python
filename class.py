print "Enter first number please, and tap Enter"
num1=int(raw_input(">"))
print "Enter second number please, and tap the Enter"
num2=int(raw_input(">"))
if num1 < num2:
	print num1 + num2
elif num1 > num2:
	print num1 - num2
elif num1 == num2:
	print num1 * num2