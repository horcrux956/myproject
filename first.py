from math import*

class MyError(Exception):
    def __init__(self, text):
        self.txt = text

class MyError2(Exception):
    def __init__(self, text):
        self.txt = text

class MyError3(Exception):
    def __init__(self, text):
        self.txt = text

try:
    s=int()
    a=int()
    Vnach=int(input())
    Vo=int(input())
    t=int(input())
    raise ValueError('числа')
    if t==0:
        raise MyError2('time')
    a=(Vnach*Vo)/t
    print('ускорение равно ', a)
    raise MyError('вычисление расстояния')


except MyError:
    s=(Vo*t)+(a*(t*t))/2
    print('расстояние равно ', s)

except MyError2:
    print('время не может быть равно 0')

except MyError3:
    print('данные не являются числами')

except ValueError:
    ('данные не являются числами')

finally:
    print('конец программы')

