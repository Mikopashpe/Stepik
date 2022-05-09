'''
Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и 
возвращает значение True если указанный текст является палиндромом и False в противном случае.
'''

def is_palindrome(text):
    text = text.lower()
    a = [c for c in text if c.isalpha()]
    return a == a[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))

