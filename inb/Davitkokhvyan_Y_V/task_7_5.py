# Задача 7. Вариант 5.
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Давиткохвян Юрий Васильевич
# 13.03.2017

print("Программа случайным образом загадывает один из трех цветов светофора, а игрок должен его угадать.")
import random

colors = [
    "Зеленый",
    "Желтый",
    "Красный"
    ]
c = random.choice(colors)
answer = input("Назовите цвет:")
tries = 1000
while c != answer :
    print("\nВы не угадали! ")
    answer = input("Ваш вариант ответа:")
    tries -= 100
else:
    print("\nПоздравляю! Вы справились!")   
    print("Вам начислено ", tries," баллов!\n" )
          


input("\n\npress Enter")        
    
      