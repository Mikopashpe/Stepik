'''
Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку 
в «верблюжьем регистре» и преобразует его в «змеиный регистр».
'''

def convert_to_python_case(text):
    symb = ''
    for i in text:
        if i.isupper():
            symb += '_'
        symb += i.lower()
    return symb[1:]

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))

