'''
Красный, синий и желтый называются основными цветами, потому что их нельзя получить путем смешения других цветов. 
При смешивании двух основных цветов получается вторичный цвет:

если смешать красный и синий, то получится фиолетовый;
если смешать красный и желтый, то получится оранжевый;
если смешать синий и желтый, то получится зеленый.
Напишите программу, которая считывает названия двух основных цветов для смешивания. 
Если пользователь вводит что-нибудь помимо названий «красный», «синий» или «желтый», 
то программа должна вывести сообщение об ошибке. 
В противном случае программа должна вывести название вторичного цвета, который получится в результате.

Формат входных данных
На вход программе подаются две строки, каждая на отдельной строке.

Формат выходных данных
Программа должна вывести полученный цвет смешения либо сообщение «ошибка цвета», если введён был не цвет.

Примечание 1. Если смешать красный и красный, то получится красный и т.д.

Примечание 2. Поиграйтесь с настоящим цветовым микшером 🙂
'''

color1 = input()
color2 = input()
color_list = ['красный', 'желтый', 'синий']
if color1 not in color_list or color2 not in color_list:
    print('ошибка цвета')
elif color1 == 'красный' and color2 == 'желтый':
    print('оранжевый')
elif color1 == 'красный' and color2 == 'синий':
    print('фиолетовый')
elif color1 == 'желтый' and color2 == 'красный':
    print('оранжевый')
elif color1 == 'желтый' and color2 == 'синий':
    print('зеленый')
elif color1 == 'синий' and color2 == 'красный':
    print('фиолетовый')
elif color1 == 'синий' and color2 == 'желтый':
    print('зеленый')
elif color1 == color2:
    print(color1)

    