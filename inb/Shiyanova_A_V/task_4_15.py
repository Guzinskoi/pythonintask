# Задача 4. Вариант 15.
#Напишите программу, которая выводит имя, под которым скрывается Анри Мари Бейль. 
#Дополнительно необходимо вывести область интересов указанной личности, место рождения, годы рождения и смерти (если человек умер), вычислить возраст на данный момент (или момент смерти).
# Для хранения всех необходимых данных требуется использовать переменные. 
#После вывода информации программа должна дожидаться пока пользователь нажмет Enter для выхода.

#Shiyanova A.V.
#22.02.2017

print("Анри Мари Бейль более известен, как Стендаль")

year_of_birth = 1783
year_of_death = 1842
age = year_of_death - year_of_birth
birthplace = "Гренобль, Франция"
interess = "французский писатель, один из основоположников психологического романа."

print("Дата рождения:", year_of_birth )
print("Дата смерти:", year_of_death)
print("Возраст:", age )
print("Место рождения:", birthplace)
print("Область интересов:", interess)

input("\n\nНажмите Enter для выхода")
