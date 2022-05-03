'''
На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке. 
Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
'''

x = int(input())
largest = -1
large = -1
for i in range(x):
    num = int(input())    
    if num > largest:
        large = largest
        largest = num
    elif num > large:
        large = num
print(largest)
print(large)

