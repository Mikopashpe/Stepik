'''
На вход программе подается последовательность слов, каждое слово на отдельной строке. 
Концом последовательности является одно из трех слов: «стоп», «хватит», «достаточно» (маленькими буквами, без кавычек). 
Напишите программу, которая выводит общее количество членов данной последовательности.
'''

a = input()
counter = 0
flag = True
while a != 'достаточно' and a != 'хватит' and a != 'стоп':
    counter +=1
    a = input()
print(counter)

