# Задача 7. Вариант 10.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Lisyanskaya A. V.
# 03.04.2017

import random
print("Программа случайным образом загадывает название одной из трех стран, входящих в военно-политический блок 'Тройственный союз', а игрок должен его угадать.")
print("По результатам игры Вам будут начислены очки.")
ball = 0
strani = ("Германия","Австро-Венгрия","Италия")
vibor = strani[random.randint(0, 2)]
while 1:
    otvet = input("Попробуйте угадать страну:")
    if otvet == vibor:
        print("Вы угадали! Правильный ответ: ", vibor)
        ball = ball + 1000
        print("Вам начислено", ball, "очков")
        break
    else:
        print("Вы не угадали. Следующая попытка.")
        ball = ball - 300	   
    print()
input("\n\n\nНажмите Enter, чтобы выйти.")