# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число
# вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# array = []
# a1 = int(input('Введите первый элемент: '))
# d = int(input('Введите разность: '))
# n = int(input('Введите количество элементов: '))
# for i in range(1, n+1):
#     array.append(a1 + d * (i - 1))
# print(*array)

# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного максимума)
# Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

min_val = int(input("Введите минимальное значение: "))
max_val = int(input("Введите максимальное значение: "))
my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

result = []
for i in range(len(my_list)):
    if min_val <= my_list[i] <= max_val:
        result.append(i)

print(result)
