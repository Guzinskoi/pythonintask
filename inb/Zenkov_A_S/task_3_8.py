# Задача 3. Вариант 8.
# Напишите программу, которая выводит имя "Борис Николаевич Бугаев", и запрашивает его псевдоним.
# Программа должна сцеплять две эти строки и выводить полученную строку, разделяя имя и псевдоним с помощью тире.

# Zenkov A. S.
# 13.03.2017

ans='Y'
while ans=='Y':
	print ('Какой псевдоним был у Бориса Николаевича Бугаева?')
	name=input('Введите псевдоним: ')
	if name=='Андрей Белый':
		print('Правильно! '+'Борис Николаевич Бугаев'+' - '+name)
		input()
		break
	print('Не верный ответ')
	print('Попробовать снова? [Y/N]')
	ans=input()
	if ans=='Y':
		continue
	if ans=='N':
		break
	else:
		print('Я не понял')
		while ans != 'Y' and ans != 'N':
			ans=input('Попробуй ещё [Y/N]\n')
	continue