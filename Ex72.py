'''
На вход программе подается два натуральных числа a b (a< b). 
Напишите программу, которая находит все простые числа от a до b включительно.
'''

x = int(input())
y = int(input())

for i in range(x, y+1):
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0:
            break
    else: 
        print(i)

        