# Задача 9, Вариант 12 

# Создайте игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать. 
# Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо 
# буква в слове, причем программа может отвечать только "Да" и "Нет". Вслед за тем игрок должен попробовать отгадать слово.

# Паноян Л.Т.
# 22.04.2017

import random
word = ("слава","победа","память","гордость","парад","салют","праздник")
varik=""
comp=random.choice(word)
 
quantity=5
attempt=1 
print('у вас 5 попыток отгадать слово')
print("Угадайте заданное слово из ниже перечисленных")
print (word)

while varik != comp and quantity > 0:
    if quantity == 5 :  
        if (input("нужны ли Вам подсказки?")) == "да" :
            print("Длина заданного слова = :",len(comp))
    else :
        if quantity <5:
            if (input("нужна ли Вам ещё подсказка?")) == "да" :
                symbol=input("Назовите букву и я скажу - есть ли она в слове :  ")
                if symbol in comp :
                    print("Эта буква присутствует в слове")
                else :
                    print ("буква отсутвует")
    quantity=quantity-1				
 
    varik=input("Ваш вариант :")
	
    print("Попытка :",attempt)
    attempt=attempt+1
	
   
if varik==comp :
    print("Вы угадали!")
else :
    print('Вы проиграли!!! Правильный ответ: ', comp )
     
input ('Нажмите Enter для выхода')