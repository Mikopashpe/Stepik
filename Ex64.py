'''
Дано натуральное число n (n≤ 9). 
Напишите программу, которая печатает таблицу размером n*5, где в i-ой строке указано число i (числа отделены одним пробелом).
'''

x = int(input())
for i in range(1, x+1):
    for j in range(5):
        print(i, end = ' ')
    print()
    
           
