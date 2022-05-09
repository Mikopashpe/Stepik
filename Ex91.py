'''
Напишите функцию get_next_prime(num), которая принимает 
в качестве аргумента натуральное число num и возвращает первое простое число большее числа num.
'''

def get_next_prime(num):
    while True:
        num += 1
        count = 0
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
        if count == 2:
            return num
        
# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))

