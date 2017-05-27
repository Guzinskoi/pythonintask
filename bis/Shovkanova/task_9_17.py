# Задача 9. Вариант 17.

# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать.
# Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове,
# причем программа может отвечать только "Да" и "Нет".
# Вслед за тем игрок должен попробовать отгадать слово.

#Шовканова Г.Д.
#27.03.2017
import random

WORDS=("чайник", "книга", "фотография", "стол")
# случайным образом выберем из последовательности одно слово
word = random.choice(WORDS)
length=len(word)

# начало игры
print(
"""
Добро пожаловать в игру 'Отгадай слово'!
Надо попытаться догадаться, какое слово загадал компьютер.
(Для выхода нажмите Enter. не вводя своей версии.)
"""
)

# отметка, сколько было подсказок
adviced=0

print("Длина загаданного слова: " + str(length))
print("Сейчас вы можете спросить компьютер, есть ли в слове любая из букв алфавита:")
while adviced < 5:
    char=input("Введите букву: ")
    if char == "":
        break;
    if word.find(char) > -1:
        print("Буква " + char + " есть в слове!")
    else:
        print("Буквы " + char + " в слове нет!")
    adviced = adviced + 1


if char != "":
    guess = input("\nПопробуйте отгадать исходное слово: ")

    while (guess != word or guess == "") and char != "":
        if guess == "":
            break
        print("K сожалению. вы неправы.")
        guess = input("Попробуйте отгадать исходное слово: ")

    if guess == word:
        print("Дa. именно так! Вы отгадали! Слово: " + word)

print("Cnacибo за игру.")
input("\nHaжмитe Enter. чтобы выйти.")