# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2

# numberOfCoins = int(input('Введите количество монеток: '))
# import random
# list = [0,1]
# list2 = []
# i = 0
# nullQuintity = 0
# oneQuintity = 0
# for i in range (numberOfCoins):
#     list2.append(random.randint(0,1))
#     if list2[i] == 0:
#         nullQuintity += 1
#     if list2[i] == 1:
#         oneQuintity += 1
# print(list2)
# print('Количество нулей: ', nullQuintity)
# print('Количество единичек: ', oneQuintity)
# if nullQuintity < oneQuintity:
#     print('Минимальное количество монет, которые нужно перевернуть: ', nullQuintity)
# else:
#     print('Минимальное количество монет, которые нужно перевернуть: ', oneQuintity)

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

# sum = int(input('Введите сумму чисел: '))
# multiplication = int(input('Введите произведение чисел: '))
# for x in range (multiplication):
#     for y in range(multiplication):
#         if (x*y)==multiplication and (x+y)==sum:
#             print(x,y)
#         else:
#             print('Вы ввели неверные значения')
            
            
## Как вывести пользователю об ошибке введеных данных, если x и y не определяются?

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

# try:
#     numberOfUser = int(input('Введите число предела: '))
#     degree = 0
#     finalNumb = 1

#     if numberOfUser <=1:
#         print('Вы ввели слишком маленькое число')
        
#     while finalNumb < numberOfUser:
#         finalNumb = 2**degree
#         degree+=1
#         if finalNumb < numberOfUser:
#             print(finalNumb)
# except ValueError:
#     print('Вы ввели некорректное значение')


# Задача 5 - HARD необязательная
# Напишите программу, которая принимает на вход координаты
# двух точек и находит расстояние между ними в N-мерном пространстве.
# Сначала задается N с клавиатуры, потом задаются координаты точек.

# import math
# try:
#     numberOfDimensionsOfSpace = int(input('Введите мерность пространства: '))
#     distance = 0
#     for i in range(numberOfDimensionsOfSpace):
#         x2 = int(input('Введите координату второй точки: '))
#         x1 = int(input('Введите координату первой точки: '))
#         distance = math.sqrt(math.pow((x2 - x1),2)) + distance
#     print(distance)
# except ValueError:
#     print('Вы ввели некорректное значение')


# задача 4 необязательная Задайте число.
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

# Не решил до конца

# numberOfFibonacci = int(input('Введите число Фибоначчи: '))

# def getFibonacci(numberOfFibonacci):
#     fibNumbers = []
#     first = 1
#     second = 1
#     for i in range(numberOfFibonacci):
#         fibNumbers.append(first)
#         first, second = second, first + second
#     first, second = 0, 1
#     for i in range (numberOfFibonacci):
#         fibNumbers.insert(0,first)
#         first, second = second, first - second
#     return fibNumbers

# fibNumbers = getFibonacci(numberOfFibonacci)
# print(getFibonacci(numberOfFibonacci))
