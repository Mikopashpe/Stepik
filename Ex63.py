'''
Дано натуральное число n (n≤ 9). 
Напишите программу, которая печатает таблицу размером n*3 состоящую из данного числа (числа отделены одним пробелом).
'''

x = int(input())
for i in range(x):
    for j in range(3):
        print(x, end =' ')
    print()

    