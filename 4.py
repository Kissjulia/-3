# Напишите программу, которая будет преобразовывать десятичное число в двоичное. Без применения встроеных методов (арифметически)
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10
d = ''
n = int(input("Введите число :\n"))
while n != 0:
    d = str(n%2) + d
    n //=2
print(d)