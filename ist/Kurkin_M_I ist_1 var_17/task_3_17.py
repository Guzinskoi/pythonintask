#Задача 3. Вариант 17.
#Напишите	программу,	которая	выводит	имя	"Симона	Руссель",	и	запрашивает	его псевдоним.	
#Программа	должна	сцеплять	две	эти	строки	и	выводить	полученную строку,	разделяя	имя	и	псевдоним	с	помощью	тире.

#Kurkin M. I.
#19.04.2017
print ("Герой нашей сегодняшней программы - Симона Руссель!")

answer = input("Под каким же именем мы знаем этого человека? Ваш ответ: ")

if answer == "Мишель Морган":

	print ("Всё верно: Симона Руссель " + "-" + " это Мишель Морган.")

else:

	print ("Эх, неудача! Попробуй снова.")

input ("Для выхода из программы нажмите клавишу <Enter>.")