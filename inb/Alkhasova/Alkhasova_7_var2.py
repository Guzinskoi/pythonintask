# задача №7 v2
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы больше количество баллов за меньшее кол-во попыток

print("Программа случайным оброзом загадывает название одного из семи холмов, но которых была построенна Москва, а игрок должен его угадать")
print("Чем быстрее вы угадаете, тем больше баллов за игру получите")

import random

b = 1000
x = ['Заяц', 'Волк', 'Медведь', 'Лиса']

while True:
    n = input("Назовите одного из 4 животных: ")
    if n != (random.choice(x)):
        print("Вы не угадали!!!")
        print("Правильный ответ был - ", (r.choice(x)))
        print("-100 баллов")
        print("Попробуй еще раз.")
        b = b - 100

    else:
        print("Вы угадали!")
        print("Вам зачисленно", b, "баллов")
        break

end = input("\nНажмите Enter для выхода")