# типы данные и переменные
# int (целые  числа)  foalt(числа с плавающей точкой применяетсядля дробных /не целых чисел) boolean(логические числа) s(строки ) 
# list- Списки (масссивы)
# None (Присваевается переменной для дальнейшего использования по коду)
#Type функция отображающая тип данных int,float итд
# print Вывод строки
# \n переход на новую строку
#boolean(логические числа)  F(используетсядля обозначения) 
# // при использовании двух знаков деления число будет округленно
# ** при использовании двух знаков умножения число возводится в степень
# round если не предавать значения данной функции она округлит математический остаток до целого числа
# += при использовании не обязательно писать переменную дважды аналогично для всех арифметических операций
# == операция сравнение
# !=
# range????

from multiprocessing.sharedctypes import Value
from re import A

Value = None
a = 123
b = 1.23
#print (type(a))
#print(type(b))
value = 1234 
#print(type(value))

#s='helo world'
#print(s)
#print(a, '-',b, '-',s)
#print('{} - {} - {}'. format(a,b,s))
#print(f'{a} - {b} - {s}')
#print('{1} - {2} - {0}'. format(a,b,s))

#f = True
#f = False
#print(f)
#list =['1', '2', '3', 'hello python']
#list =['1', '2','3']
#col= ['hello', 1,2,3, True]
#print(list)
#print(col)

#print('Введите a');
#a = int(input())
#print('Введите b');
#b = int(input())
#print(a, '+', b, '=', a+b)
#print('{}{}'.format(a, b))Примеры вывода
#print(f'{a} {b}')

# print('Введите a');
# a = float(input())
# print('Введите b');
# b = float(input())
# print(a, '+', b, '=', a+b)

# a = 2
# b = 8
# c =  a-b
# print(c)

#  Логические операции
# a = 1==
# print(a)

# a = int(input('a ='))
# b = int(input('b ='))
# if a > b:
#     print(a)
# else:
#     print(b)


# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура это же маша')
# elif username =='Марина':
#     print('Я так ждал вас Марина')
# elif username == 'Ильнар':
#     print('Ильнар-топ')
# else:
#     print('Привет,', username)

# origin = 23
# inwert = 0
# while origin != 0:
#     inwert = inwert * 10 + (origin % 10)
#     origin  //= 10
# print(inwert)

# origin = 23
# inwert = 0
# while origin !=0:
#     inwert = inwert * 10 + (origin % 10)
#     origin  //= 10
# else:
#     print('пожалуй')
#     print('хватит')
# print(inwert)

# for i in 1,2,3,4,5:
#     print(i**2)

# list =[1,2,3,4, 10,5]
# for i in list:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

# text = 'сьешь еще этих мягких французских будлк'

# text.
# print(len(text))    #39
# print('еще' in text)  #true
# print(text.isdigit())   #false
# print(text.islower()) # True
# print(text.replace('еще','ЕЩЕ')