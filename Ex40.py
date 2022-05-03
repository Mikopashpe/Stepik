'''
На вход программе подается натуральное число n. 
Напишите программу вычисления знакочередующей суммы
'''

x = int(input())
total = 0
for i in range(1, x+1):
    if i%2 == 0:
        total -= i
    else:
        total +=i
print(total)

