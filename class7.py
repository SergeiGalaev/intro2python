s = "sef 668 76 7  757 57 "
news = ""
for n in s:
	if n == " ":
		n = "!"
	news += n
print news		