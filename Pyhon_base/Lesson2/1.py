# Lesson 2
# 1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
my_list = (1,-10,2.5,'Hello',[1,5,9],{'name': 'Maxim', 'age': 53})
print('Это наш список: {}'.format(my_list))
for el in my_list:
    print('Элемент списка {} - это {}'.format(el,type(el)))