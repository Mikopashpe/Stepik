'''
На вход программе подается натуральное число n. 
Напишите программу, которая находит цифровой корень данного числа. 
Цифровой корень числа n получается следующим образом: если сложить все цифры 
этого числа, затем все цифры найденной суммы и повторить этот процесс, то в результате будет получено однозначное число (цифра), которое и называется цифровым корнем данного числа.
'''

x = int(input())
counter = 0
counter2 = 0
counter3 = 0
while x !=0:
    l = x%10
    counter += l
    x = x//10
while counter !=0:
    m = counter%10
    counter2 += m
    counter = counter//10
while counter2 !=0:
    m = counter2%10
    counter3 += m
    counter2 = counter2//10
print(counter3)
