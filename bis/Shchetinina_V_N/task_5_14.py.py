#Задача 5. Вариант 14 
#Напишите программу, которая бы при запуске случайным образом отображала название одной из двадцати башен Московского кремля. 

# Shchetinina V. N.
# 26.03.2017


import random 

import string 

print('Эта программа случайным образом отображает назване одной из двадцати башен Московского Кремля!') 

tower = ["Беклемишевская","Константино-Еленинская","Набатная","Царская","Спасская","Сенатская","Никольская","Угловая Арсенальная","Средняя Арсенальная","Троицкая","Кутафья","Комендантская","Оружейная","Боровицкая","Водовозная","Благовещенская","Тайницкая","Первая Безымянная","Вторая Безымянная","Петровская"] 

print('\nНазвание башни: ', random.choice(tower)) 

input('\nНажмите Enter, чтобы выйти')