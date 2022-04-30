'''
Напишите программу, вычисляющую значение ⌈x⌉+⌊x⌋ по заданному вещественному числу x.
'''

from math import *

x = float(input())
y = ceil(x) + floor(x)
print(y)

