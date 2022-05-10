
def is_pangram(text):
    s = sorted(set(text.lower().replace(' ', '')))
    al = 'abcdefghijklmnopqrstuvwxyz'
    if len(al) == len(s):
        return True
    else:
        return False

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))