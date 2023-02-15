# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному 
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint


def check_index(list_1, max_el, min_el):
    list_res = []
    for i in range(len(list_1)):
        if min_el < list_1[i] < max_el:
            list_res.append(i)
    return list_res


n = int(input("Введите количество элементов массива: "))
list_01 = []
for i in range(n):
    list_01.append(randint(0,20))
print(f"Последовательность чисел - {list_01}")
max_elem = int(input("Введите верхнюю границу диапазона: "))
min_elem = int(input("Введите нижнюю границу диапазона: "))
print(check_index(list_01, max_elem, min_elem))
