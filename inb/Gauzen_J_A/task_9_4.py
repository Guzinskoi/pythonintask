# Задача 9. # Вариант 4.
#Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать.
#Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет".
#Вслед за тем игрок должен попробовать отгадать слово.

# Гаузен Юлия Александровна
# 16.04.2017

import random
words = ("ответ","кот","собака","отдых","веселье","учеба","дорога","ноутбук","телефон")
word = random.choice(words)
correct = word
a = ""
c = 1

print("Добро пожаловать в игру.")
print("Вы узнаете сколько букв в слове, затем у вас будет 5 попыток узнать, еслть ли какая-то конкретная буква в слове.")
print("Затем вы должны попробовать отгадать слово,но помните, что у вас только одна попытка.")
print("Игра началась.")
print("Количество букв в слове:", len(word))
while c != 5:
    a = input("Назовите букву:")
    if a in word:
        print("Да")
    if a not in word:
        print("Нет")
    c = c + 1
b=input("Теперь попробуйте отгадать слово:")
if b == correct:
    print("Все верно!")
else:
    print("Вы проиграли.")
print("Спасибо за игру!")
input("Нажмите Enter, чтобюы выйти")    
    

