'''
Известен вес боксера-любителя (целое число). Известно, что вес таков, 
что боксер может быть отнесён к одной из трех весовых категорий:

Легкий вес – до 60 кг;
Первый полусредний вес – до 64 кг;
Полусредний вес – до 69 кг.
Напишите программу, определяющую, в какой категории будет выступать данный боксер.

Формат входных данных
На вход программе подаётся одно целое число.

Формат выходных данных
Программа должна вывести текст – название весовой категории.
'''

x = int(input())
if x < 60:
    print('Легкий вес')
elif 60<= x < 64:
    print('Первый полусредний вес')
elif 69> x>= 64:
    print('Полусредний вес')

    