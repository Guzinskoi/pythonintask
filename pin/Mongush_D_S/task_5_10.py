# Задание 5. Вариант 10.
# Mongush D.S.
# Напишите программу, которая бы при запуске случайным образом отображала название одного из шести континентов Земли.
# 05.04.17

#Импортируем модуль рандом из библиотеки, чтобы можно было пользоваться его функционалом
import random

#создаем кортеж
materiki = ("Евразия", "Африка", "Австралия", "Северная Америка", "Южная Америка", "Антарктида")
#присваиваем переменной word случайно выбранное значение из значений materiki
word = random.choice(materiki)
#выводим на экран выбранное значение
print ("Компьютер выбрал материк", word)
#Ждем нажатия Enter для выхода
input("\n\nНажмите Enter, чтобы выйти.")