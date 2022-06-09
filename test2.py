import random
from tracemalloc import stop


class colors:
    RED = '\u001b[31m'
    GREAN = '\u001b[32m'
    NEUTRAL = '\u001b[37m'
    YELLOW = '\u001b[36;1m'
    ENDC = '\033[0m'

def game():
    player = input (colors.YELLOW + "Камень, Ножницы, Башмак?")

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

    print (colors.RED + "Компютер:", bot , colors.NEUTRAL + "|" , colors.GREAN + "Игрок:", player + colors.ENDC)
    print ('Исход:', end)

    game()
game()