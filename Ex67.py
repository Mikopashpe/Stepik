'''
Дано натуральное число n. 
Напишите программу, которая печатает численный треугольник с высотой равной n, в соответствии с примером:
'''

x = int(input())
for i in range(1, x+1):
    for j in range(1, i +1):
        print(j, end='')
    for k in range(j-1, 0, -1):
        print(k, end='')
    print()

    