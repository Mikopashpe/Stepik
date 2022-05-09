'''
BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. 
Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
число a – должно быть палиндромом;
число b – должно быть простым;
число c – должно быть четным.
'''

def is_valid_password(password):
    def is_palindrome(n:int)->bool:
        return str(n) == str(n)[::-1]

    def is_prime(n:int)->bool:
        if n in (0, 1):
            return False
        if n%2 == 0:
            return False
        for i in range(3, round(n**(1/2)+1), 2):
            if n%i == 0:
                return False
        return True

    def is_even(n:int)->bool:
        return n%2 == 0

    w = password.split(':')
    a = int(w[0])
    b = int(w[1])
    c = int(w[2])
    if len(w)>3:
        return False
    if is_palindrome(a) and is_prime(b) and is_even(c):
        return True
    else:
        return False

# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))

