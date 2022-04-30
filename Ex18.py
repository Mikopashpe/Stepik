'''
Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
'''

from math import *

a = float(input())
b = float(input())
a2 = float(input())
b2 = float(input())
z = sqrt((a-a2)**2 + (b-b2)**2)
print(z)

