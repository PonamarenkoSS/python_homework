# Задача 28
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

# Пример:
# 2 4
# 2


def sum_of_two(n, m):
    if m == 0:
        return n
    return sum_of_two(n+1, m-1)


A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))

if A > B:
    print(sum_of_two(A, B))
else:
    print(sum_of_two(B, A))