'''
На вход программе подается два вещественных числа a и b, каждое на отдельной строке.
Программа должна вывести 4 числа – среднее арифметическое, геометрическое, гармоническое и квадратичное.
'''

from math import *

a = float(input())
b = float(input())
x = (a+b)/2
y = sqrt(a*b)
z = (2*a*b)/(a+b)
w = sqrt((a**2 + b **2)/2)
print(x)
print(y)
print(z)
print(w)

