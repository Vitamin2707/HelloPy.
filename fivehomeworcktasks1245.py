# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]'

# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")

# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. 
# Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# print(f"Исходный список: {lst}")
# new_lst = []
# [new_lst.append(i) for i in lst if i not in new_lst]
# print(f"Список из неповторяющихся элементов: {new_lst}")


# 4- Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо. 
# При расшифровке происходит обратная операция. 
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, 
# "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

# Функция, принимающая текст и сдвиг для шифровки
# и записывающая зашифрованный текст в файл (если файла нет, она его создает - режим w+)

# def encryptor(text, shift):
#     encrypted_text = ''
#     with open('encrypted_message.txt', 'w+', encoding='utf-8') as encrypted_message:
#         for letter in text:
#             encrypted_letter = chr(ord(letter) + shift)
#             encrypted_text += encrypted_letter
#         encrypted_message.write(encrypted_text)


# # Функция, принимающая файл с защифрованным текстом и сдвиг для дешифровки
# # и записывающая дешифрованный текст в новый файл (если файла нет, она его создает - режим w+)
# def decryptor(file, shift):
#     decrypted_text = ''
#     with open('decrypted_message.txt', 'w+', encoding='utf-8') as decrypted_message:
#         with open(file, 'r', encoding='utf-8') as encrypted_message:
#             for line in encrypted_message:
#                 for letter in line:
#                     decrypted_letter = chr(ord(letter) - shift)
#                     decrypted_text += decrypted_letter
#         decrypted_message.write(decrypted_text)


# encryptor('абба', -2)
# decryptor('encrypted_message.txt', -2)

# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.


# первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# import encode_module
# import decode_module


# # Функция для считывания текста из файла, его шифровки и записи шифрованного сообщения в другой файл
# def encoded_writer(file):
#     encrypted_text = ''
#     with open('encrypted_message.txt', 'w+', encoding='utf-8') as encrypted_message:
#         with open(file, 'r', encoding='utf-8') as initial_text:
#             for line in initial_text:
#                 encrypted_text = encode_module.encoder(line)
#         encrypted_message.write(encrypted_text)


# # Функция для считывания зашифрованного текста из файла, его дешифровки и записи дешифрованного сообщения в другой файл
# def decoded_writer(file):
#     decrypted_text = ''
#     with open('decrypted_message.txt', 'w+', encoding='utf-8') as decrypted_message:
#         with open(file, 'r', encoding='utf-8') as encrypted_message:
#             for line in encrypted_message:
#                 decrypted_text = decode_module.decoder(line)
#         decrypted_message.write(decrypted_text)


# encoded_writer('initial text.txt')
# decoded_writer('encrypted_message.txt')