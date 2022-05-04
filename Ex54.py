'''
Дано натуральное число. 
Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
'''


x = int(input())
n = x
s = 0
counter = 0
while x !=0:
    l = x%10
    counter +=1
    s +=l
    x = x//10
m = n%10
v = n//10**(counter -1)
srar = s/counter
if srar == m and m == v:
    print('YES')
else:
    print('NO')

    