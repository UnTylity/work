import random
from tracemalloc import stop

def game():
    player = input ("Камень, Ножницы, Башмак?")

    b1 = "Камень" 
    b2 = "Ножницы"
    b3 = "Башмак"
    list = (b1 , b2 , b3)
    bot = random.choice(list)

    if ((player == b1 and bot == b1) or (player == b2 and bot == b2) or (player == b3 and bot == b3)):
        end  = 'Ничия'
    elif ((player == b1 and bot == b3) or (player == b2 and bot == b1) or (player == b3 and bot == b2)):
        end = 'Победил Компютер'
    elif ((player == b1 and bot == b2) or (player == b2 and bot == b3) or (player == b3 and bot == b1)):
        end = 'Победил Игрок'

    elif player == '0':
        stop
    else:
        end= "ERR"

    print ("Компютер:", bot , "|" , "Игрок:", player)
    print ('Исход:', end)

    game()
game()