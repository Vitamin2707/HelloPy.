# Урок 1. Знакомство с Python
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# day = int(input('Введите день недели '))
# if day<=7 and day>=1:
#     if day ==6 or day ==7:
#         print(str(day) + '->да')
#     else:
#         print(str(day) + '->нет')
# else:
#      print ('Введен не существующий день')

# Задача 1
# Есть список a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89].

# решение 1 вариант с for

#  a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# # for i in a:
# #     if i < 5:
# #         print(f"{i}")

# print(list(filter(lambda elem: elem < 5, a)))



# 
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# ними в 2D пространстве.


# Задачи:
# Напишите программу, которая принимает на вход два числа и проверяет, является ли одно число квадратом другого.
# Примеры:
# 5, 25 -> да
# 4, 16 -> да
# 25, 5 -> да
# 8,9 -> нет

# one = int(input(' введите первое число '))
# two = int(input(' введите второе число число '))
# if two == one ** 2 or one == two**2:
#     print(' yes ')
# else:
#     print(' no ')

# def is_number_power( x,y ):
#     if y == x ** 2 or x == y ** 2:
#         return True
#     else:
#         return False

# x = int(input(' введите первое число '))
# y = int(input(' введите второе число число '))
# print(is_number_power())


# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# Примеры:
# 1, 4, 8, 7, 5 -> 8
# 78, 55, 36, 90, 2 -> 90

# from random import randint

# numbers = [randint(1,100) for i in range(5)]
# max = numbers[0]

# for i in numbers[1:]:
#     if i > max:
#         max = i
# print(f'{numbers} -> {max}')

# i = 1
# a = list(range(1,6)) #a = list(range(5))
# while i <= 5:
#     number = input(f'Введите {i}-е число + enter: ')
#     a[i-1] = number
#     if i == 1:
#         max = number
#     elif number > max:
#         max = number
#     i += 1
# print(f'max = {max}')


# number = int(input('Введите число'))
# a = list(range(-number, number+1))

# print(a)

# Напишите программу, которая будет на вход принимать число N 
# и выводить числа от -N до N
# Примеры:
# 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# N = int(input(f'Введите число N + enter: '))
# i = -1*N
# print(f'{N} -> ', end = '')
# while i < N:
#     print(f'{i}, ', end = '')
#     i = i + 1 
# else:
#     print(f'{N}')
