# Задача 8. Вариант 7.
# Доработайте игру "Анаграммы" (см. М.Доусон Программируем на Python. Гл.4) так,
# чтобы к каждому слову полагалась подсказка. Игрок должен получать право на подсказку
# в том случае, если у него нет никаких предположений. Разработайте систему начисления
# очков, по которой бы игроки, отгадавшие слово без подсказки, получали больше тех,
# кто запросил подсказку.

# Lysenko N.A.
# 26.03.2017

import random
WORDS = ("разработка", "python", "самолет", "пробоина", "коммуникации")
word = random.choice(WORDS)
correct = word
jumble = ""
points = 100

#Перемешиваем буквы в слове
while word:
    position = random.randrange(len(word))
    jumble += word [position]
    word = word[:position]+word[(position+1):]
    
#Начало игры
print(
"""
           Добро пожаловать в игру аннаграмы!
        
   		Поставьте буквы в правильном порядке и победите.
   			У вас есть только 3 подсказки!
"""
)

print ("Замаскированное слово:", jumble)
guess = input("\nВаше предположение (напишите \"подсказка\" для вызова подсказки): ")
l = 0
while guess.lower() != correct and guess != "":

    if guess.lower() != "подсказка":
        print ("Вы не угадали!\n")
    else:
        if l!=3:
            help = int(input("Какую по счету букву Вы хотите открыть? "))
            print ("Это буква ", correct[(help-1)], "\n")
            points -= 15
            l += 1
        else:
            print ("Лимит подсказок исчерпан.\n")

    guess = input ("Ваше предположение (напишите \"подсказка\" для вызова подсказки): ")

if guess.lower() == correct:
    print("Правильно! Поздравляю! Вы набрали", points, "очков.\a")

input("\n\nНажмите Enter, чтобы выйти")