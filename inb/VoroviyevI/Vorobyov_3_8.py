# Задача №3 м8
# Воробьев Илья Андреевич ИНБ-2016-1
# Напишит программу, которая выводит имя "Борис Николаевич Бугаев", и запрашивает его псевдоним.

print("Герой нашей сегоднешней программы - Борнис Николаевич Бугаев")
while True:
    ask = input("Под каким же именем вы знаете этого человека? Ваш ответ: ")
    if ask == "Андрей Белый":
        print("Все верно: Борис Николаевич Бугаев - ", ask)
        break
    else:
        print("Неверно, попробуй еще.")

end = input("Нвжмите Enter для выхода")