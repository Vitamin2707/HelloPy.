# from os import system
# system('cls')

# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр (отсекаем минус, считаем все в плюс).
# Пример:
# 67,82 -> 23
# 0,56 -> 11

# count= input('enter a number: ')
# sum = 0
# for i in count:
#     if i != '.':
#         sum += int(i)
# print(sum)

#  Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# N = int(input('input N: '))
# count = 1
# arr = []
# stroka = ''
# for i in range(1,N+1):
#         count *= i
#         arr.append(count)
#         stroka = stroka + str(i) + "*" + str(int(count/i)) + ', '
# print(f' {arr} -> ({stroka})')

# from functools import reduce

# def mul(a, b):
#      return a * b
    
# def f_string(n):
#      return reduce(mul, [i for i in range(1, n + 1)])
    
# def result(n):
#      return "*".join([str(i) for i in range(1, n + 1)])
  

# try:
#     N = int(input('число? '))
#     print('(' + ", ".join([result(i) for i in range(1, N + 1)]) + ') ' + '->', [f_string(i) for i in range(1, N + 1)])
# except:
#     print('Введите число')




# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа

# n = int(input("Введите число:"))
#  temp = n
# rev = 0
# while(n > 0):
#     dig = n % 10
#     rev = rev * 10 + dig
#     n = n // 10
# if(temp == rev):
#     print("Это палиндром!")
# else:
#     print("Это не палиндром!")

#  Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

# import time
# from random import randint

# arr = list()
# for i in range(10):
#     number = randint(1, 5)
#     time.sleep(0.5)
#     arr.append(int(str(time.time())[-number:]))
# print(*arr)
