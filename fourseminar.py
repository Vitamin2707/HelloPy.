# line = '1, 2, 3, 4, 5'
# list = []

# for i in range(len(line)):
#     if line[i] != ',' and line[i] != ' ':
#         list.append(int(line[i]))

# print(*list)
# print(f'Min: {min(list)}')
# print(f'Max: {max(list)}')
# 1 - Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.
# """""
# 2 - Задайте два числа. Напишите программу, которая найдет 
# НОК (наименьшее общее кратное) этих двух чисел. НОК - наименьшее общее кратное, которое делится и на первое, и на второе число.
                
# """

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a % b)


# a, b = map(int, input().split())

# print(a*b//gcd(a, b))

# def lcm(a, b):
#     lcm.multiple = lcm.multiple + b
#     if (lcm.multiple % a == 0) and (lcm.multiple % b == 0):
#         return lcm.multiple
#     else:
#         lcm(a, b)
#     return lcm.multiple


# lcm.multiple = 0
# a = int(input("Ввендите первое чило: "))
# b = int(input("Введите второе число: "))
# if (a > b):
#     LCM = lcm(b, a)
    
# else:
#     LCM = lcm(a, b)
    
# print(f'НОК {LCM}')





# Задать список из N элементов, заполненных числами из [-N, N]. Найти произведение элементов на указанных позициях. Число N вводится пользователем. Позиции хранятся в файле file.txt в одной строке одно число
# Позиции в файл вам нужно программно положить в файл в зависимости от выбранного N: если пользователь введет двойку, то в файле вряд ли будут индексы 5 или 16.
# В решении должны быть и запись в файл, и чтение из файла.