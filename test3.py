from random import randint


def game():
    a=input('от 1 до 7:')
    b=randint(1, 7)
    c = list(range(1,8))
    if(a==c):
     print(b|a)
game()