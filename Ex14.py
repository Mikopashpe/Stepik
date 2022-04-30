'''
Напишите программу, которая упорядочивает три числа от большего к меньшему.
'''

a = int(input())
b = int(input())
c = int(input())
l = [a, b, c]
print(max(l))
print((a + b + c) - (max(l) + min(l)))
print(min(l))

