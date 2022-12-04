# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример: [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from random import randint

my_list = []
for i in range (5):
    my_list.append(randint(1, 10))
print(my_list)
s = 0
for i in range (1, len(my_list), 2):
    s += my_list[i]
print(f'в {my_list} - сумма элементов на нечетных позициях: {s}.')