# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81


# Подсказка: округление значений можно сделать через round(..., 2)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиций может быть более двух, пользователь вводит индексы с клавиатуры.
# Реализуйте алгоритм перемешивания списка. (не использовать из модуля random метод shuffle другие методы допускается)


# int(input('Введите число N'))



# n=int(input('Введите число N '))
 
# numbers = []

# for i in range(0, n ):
#     numbers.append((-3)** i) 

# print(numbers)

# def return_list(n):
#     list = [1]
#     temp = 1
#     while(n > 1):
#         temp = temp * (-3)
#         n = n-1
#         list.append(temp)
#     print(list)


# return_list(int(input('Введите число: ')))


# 2.Найти сумму элементов массива, лежащих между максимальным и минимальным по значению элементами

# A = [1, 2, 3, 8, 9, 10]
# sum = 0
# poz_min = 0
# poz_max = 0
# i = 1
# size = len(A)
# while i < size:
#     if A[i] > A[poz_max]:
#         poz_max = i
#     elif A[i] < A[poz_min]:
#         poz_min = i   
#     i += 1
# print(poz_min, poz_max)
# if poz_max > poz_min:
#     for i in range(poz_min, poz_max+1):
#         sum = sum + A[i]
# elif poz_max < poz_min:
#     for i in range(poz_max, poz_min+1):
#         sum = sum + A[i]   
# else:
#     sum = A[poz_max]
# print(A, sum)

# from random import randint

# list = []
# def create_list():

#      for x in range(0, 10):
#          list.append(randint(0, 99))

#      print(list)
#      return list

# def find_distance_result(array):
#     minimal_digit = min(array)
#     maximal_digit = max(array)

#     min_index = array.index(minimal_digit)
#     max_index = array.index(maximal_digit)

#     summa = 0
#     if min_index < max_index:
#         i = min_index + 1
#         while i < max_index:

#             summa += array[i]
#             i += 1
#     else:
#         i = min_index - 1
#         while i > max_index:
#             summa += array[i]
#             i -= 1

#     print(summa)

# find_distance_result(create_list())


# 3.Найдите количество элементов массива, которые отличны от наибольшего элемента не более чем на 10%

# A = [2, 3, 6, 98, 56, 45, 78, 100, 49]
# max = A[0]
# for i in A[1:]:
#     if i > max:
#         max = i
# count = 0
# for i in A:
#     if  max*0.9 < i and i !=max:
#         count += 1 
# print(count)
