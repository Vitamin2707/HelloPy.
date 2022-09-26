#  Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

# my_text = 'Напишите абв напиабв програбвмму программу, удаляющую из \
#     этого абв текста все вабвс слова, содерабващие содержащие "абв"'

# def del_some_words(my_text):
#     my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
#     return " ".join(my_text)

# my_text = del_some_words(my_text)
# print(my_text)

# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите). 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет(или сколько вы зададите). 
# Тот, кто берет последнюю конфету - проиграл.

# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. Осталось на столе {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# while True:
#     player2 = input("Введите имя второго игрока: ")
#     if player1 != player2:
#         break
#     else:
#          print("Данное имя занято, выберите другое")
# while True: 
#     value = int(input("Введите количество конфет на столе, не меньше 29 "))
#     if value >= 29:
#         break
# flag = randint(0,2) # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")

# Игра с ботом

# import random
# from random import randint, choice
 
# print(
#     '"Игра с конфетами"\n'
#     )
 
# messages = ['Ваш ход брать конфеты', 'Возьмите конфеты',
#             'сколько конфет берем?', 'берите еще', 'Ваш ход']
# max_number_move = 0
 
# def introduce_players():
#     player1 = input('Первый игрок, представьтесь\n')
#     player2 = 'Bot'
#     print(f'Очень приятно, сегодня Вы играете с искуственным  {player2}')
#     return [player1, player2]
 
# def sweets_game(players):
#     global max_number_move
#     total_sweets = int(input('Введите cколько всего у нас конфет:\n'))
#     max_number_move = int(input('Введите количество конфет, которое можно забрать за один ход:\n'))
#     first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу\n'))
#     if first != 1:
#         first = 0
#     return [total_sweets, max_number_move, int(first)]
 
# max_move = max_number_move
 
# def game_player_vs_bot(sweets, players, messages):
#     global max_number_move
#     count = sweets[2]
 
 
#     while sweets[0] > 0:
#         if sweets[0] == (max_number_move and sweets[0] < max_number_move and sweets[0] > 1):
#             move = sweets[0] -1
#             print(f'Я забираю {move}')
 
#         elif not count % 2:
#             move = random.randint(1, sweets[1])
#             print(f'Я забираю {move}')
#         else:
#             print(f'{players[0]}, {choice(messages)}')
#             move = int(input())
#             if move > sweets[0] or move > sweets[1]:
#                 print(
#                     f'Можно взять не более {sweets[1]} конфет, у нас всего {sweets[0]} конфет')
#                 chance = 2
#                 while chance > 0:
#                     if sweets[0] >= move <= sweets[1]:
#                         break
#                     print(f'Попробуйте ещё раз, у Вас {chance} попытки')
#                     move = int(input())
#                     chance -= 1
#                 else:
#                     return print(f'Попыток не осталось. Game over!')
#         sweets[0] = sweets[0] - move
#         if sweets[0] > 0:
#             print(f'Осталось {sweets[0]} конфет')
#         else:
#             print('Все конфеты разобраны.')
#         count += 1
#     return players[not count % 2]
 
 
# players = introduce_players()
# sweets = sweets_game(players)
 
# winer = game_player_vs_bot(sweets, players, messages)
# if not winer:
#     print('У нас нет победителя.')
# else:
#     print(
#         f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')

# Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка,
#  написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

# def set_tuple(list1:list, list2:list) -> tuple: 
#      ''' 
#      Функция объединяет два списка в кортеж 
#      ''' 
#      for i in range(len(list1)): 
#          list1[i] = list1[i].upper() 
#      list1 = [char.upper() for char in list1]
  
#      return dict(zip(list2, list1)) 
  
# def filter_elements(t_tuple:tuple) -> tuple: 
#      ''' 
# #      Функция осуществляет фильтрацию элементов и возвращает уже отфильтрованный кортеж 
# #      ''' 
#      new_tuple = {} 
#      for key, value in t_tuple.items(): 
#          t_sum_kod = 0 
#          for i in value: 
#              t_sum_kod += ord(i) 
  
#          proverka = t_sum_kod / key == int(t_sum_kod / key) 
#          if proverka: 
#              new_tuple[t_sum_kod] = value 
  
#      return new_tuple 
  
  
# language_list = ['Action Script', 'C++/CLI', 'C#', 'ColdFusion', 'Dart', 'Object Pascal', 'Dylan', 'Eiffel', 'Game Maker Language (GML)', 'Groovy', 'Haxe', 'Io', 'Java', 'JavaScript', 'MC#', 'Object Pascal'] 
# numbers_list = range(1, len(language_list) + 1) 
  
# rez = (set_tuple(language_list, numbers_list)) 
# print(rez) 
# print(filter_elements(rez))