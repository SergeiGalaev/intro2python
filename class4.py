# -*-coding: utf-8-*-
print u"Вы входите в комнату с тремя дверями. В какую вы должны войти чтобы выжить？"

door = raw_input(">")
if door =="1":
	print u"Там спит очень злая собака что вы сделаете?"
	print u"1. Прогоните собаку."
	print u"2. Постараетесь найти выход не разбудив ее."
	print u"3.Вернетесь назад к двум дверям."

	dog = raw_input(">")

	if dog == "1":
		print u"Вы постарались прогнать ее но собака была бешеная и сильно покусала вас."
	if dog =="2":
		print u"Вы не нашли выход но нашли какой-то ключ ивернюлись назад."
	if dog == "3":
		print u"Cкорее всего это было верным решением."
	else: 
	print u"Вы долго думали собака проснулась и покусала вас" 	
if door == "2":
	print u"Там сиди Старец что вы сделаете?"
	print u"1.Вы поговорите с ним."
	print u"2.Вы попросите показать путь."
	print u"3.Вы вернетесь назад"

	st = raw_input(">")
	if st == "1":
		print u"Вы поговорили но ничего особенного он вам ни сказал"
	if st == "2":
		print u"Он сказал что не может этого сделать"
	if st == "3":
		print u"Cкорее всего это было верным решением"
	else: 
	print u"Вы долго думали пришла собака и покусала вас"
If door == "3":
	print u"Там есть еще две двери в какую вы пойдете?"
	door2 = raw_input(">")
	if door2 == "1":
		print u"Эта дверь закрыта"
	if door2 == "2":
		print u"Если вы не забыли взять ключ то вы нашли выход"
	else: 
		print u"Начните все с начала"

else:
	print "У вас есть только три двери"