'''
Назовем число интересным, если в нем разность максимальной и минимальной цифры равняется средней по величине цифре. 
Напишите программу, которая определяет интересное число или нет. 
Если число интересное, следует вывести – «Число интересное» иначе «Число неинтересное».
'''

x = int(input())
a = x%10
b = (x%100)//10
c = x//100
l = [a, b, c]
if max(l)-min(l) == ((a + b + c)- (max(l)+min(l))):
    print('Число интересное')
else:
    print('Число неинтересное')

    