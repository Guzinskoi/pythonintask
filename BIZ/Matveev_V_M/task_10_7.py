# Задача 10. Вариант 7.
# Напишите программу "Генератор персонажей" для игры. Пользователю должно
# быть предоставлено 30 пунктов, которые можно распределить между четырьмя
# характеристиками: Сила, Здоровье, Мудрость и Ловкость. Надо сделать так, чтобы
# пользователь мог не только брать эти пункты из общего "пула", но и возвращать их
# туда из характеристик, которым он решил присвоить другие значения.

# Matveev V.M.
# 21.04.2017

x=30
a=0
b=0
c=0
d=0
skill=""
print("Программа 'Генератор персонажей'")
print("Вам предоставлено ", x, "пунктов,которые нужно распределить между четырьмя характеристиками")
print("  Сила,	Здоровье,	Мудрость	и	Ловкость")
while x>0:
	skill=input("выбор пункта:(например, 'сила') ")
	if skill == "сила":
		choice = input ("измените пункт характеристики(+/-)")
		if choice == "+":
			a=a+1
			print ("характеристика 'сила'", a)
			x=x-1
		else: 
			a=a-1
			print ("характеристика 'сила'", a)
			x=x+1
	if skill == "здоровье":
		choice = input ("измените пункт характеристики(+/-)")
		if choice == "+":
			b=b+1
			print ("характеристика 'здоровье'", b)
			x=x-1
		else: 
			b=b-1
			print ("характеристика 'здоровье'", b)
			x=x+1
	if skill == "мудрость":
		choice = input ("измените пункт характеристики(+/-)")
		if choice == "+":
			c=c+1
			print ("характеристика 'мудрость'", c)
			x=x-1
		else: 
			c=c-1
			print ("характеристика 'мудрость'", c)
			x=x+1
	if skill == "ловкость":
		choice = input ("измените пункт характеристики(+/-)")
		if choice == "+":
			d=d+1
			print ("характеристика 'ловкость'", d)
			x=x-1
		else: 
			d=d-1
			print ("характеристика 'ловкость'", d)
			x=x+1
	print("У вас еще", x)
	print ( "сила - ", a , "здоровье - ", b, "мудрость - ", c, "ловкость - ", d)
print("Все пункты присвоены .")
input("\nHaжмитe Enter. чтобы выйти.")