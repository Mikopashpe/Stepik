'''
На числовой прямой даны два отрезка: |a:b|, |a2:b2|. 
Напишите программу, которая находит их пересечение.

Пересечением двух отрезков может быть:

отрезок;
точка;
пустое множество.
Формат входных данных
На вход программе подаются 4 целых числа a, b, a2, b2.
Гарантируется, что a<b, a2<b2.
Формат выходных данных
Программа должна вывести на экран границы отрезка, являющегося пересечением, либо общую точку, либо текст «пустое множество».
'''

a = int(input())
b = int(input())
a2 = int(input())
b2 = int(input())
if a2>b or b2<a:
    print('пустое множество')
elif a<a2 and b2<b:
    print(a2, b2)
elif a<a2 and b<b2 and a2 != b:
    print(a2, b)
elif a2<a and b<b2:
    print(a, b)
elif a2<a and b2<b and a != b2:
    print(a, b2)
elif a2 == a and b2 == b:
    print(a, b)
elif a == a2 and b<b2:
    print(a, b)
elif a == a2 and b2<b:
    print(a, b2)
elif b == b2 and a<a2:
    print(a2, b2)
elif b == b2 and a2<a:
    print(a, b2)
elif b == a2:
    print(b)
elif a == b2:
    print(a)
    