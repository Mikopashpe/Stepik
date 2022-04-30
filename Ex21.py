'''
Напишите программу, вычисляющую значение тригонометрического выражения
'''

from math import *

x = radians(float(input()))
z = sin(x)+ cos(x)+ tan(x)*tan(x)
print(z)

