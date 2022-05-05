'''
На вход программе подается два натуральных числа a и b (a< b). 
Напишите программу, которая находит натуральное число из отрезка [a;b] с максимальной суммой делителей.
'''

x = int(input())
total = 0
num = 0
y = int(input())
totaly =0
for i in range(x, y+1):
    maxnum = 0
    for j in range(1, i+1):
        if i % j == 0:
            maxnum += j
        if maxnum >= total:
            total = maxnum
            num = j
print(num, total) 

