# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

from random import randint

def Result(count):
    i = 0
    list = []
    while i < count:
        list.append(randint(0,1))
        i += 1
    print(list)
    count_first = 0
    count_second = 0
    i = 0
    while i < len(list):
        if list[i] == 0:
            count_first += 1
        else:
            count_second += 1
        i += 1
    if count_first < count_second:
        print(f"Минимальное количество монет, которые нужно перевернуть, - {count_first}")
    else:
        print(f"Минимальное количество монет, которые нужно перевернуть, - {count_second}")

n = int(input("Введите количество монеток: "))
Result(n)
