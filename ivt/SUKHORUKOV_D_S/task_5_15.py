# Задача 5. Вариант 15.
# Напишите программу, которая бы при запуске случайным образом отображала
# название одного из двенадцати городов, входящих в Золотое кольцо России.


# Сухоруков Д. С.

# 14.03.17
import random,string
print("\tПрограмма случайным образом отображает название\n" \
      "одного из двенадцати городов, входящих в Золотое кольцо России\n")
cityes =  ["Переславль-Залесский", "Ростов Великий",
           "Углич", "Ярославль", "Кострома","Плёс",
           "Суздаль", "Владимир", "Юрьев-Польский",
           "Александров", "Сергиев Посад", "Тутаев"]
print('\t',random.choice(cityes))
input("\n\nНажмите Enter для выхода")