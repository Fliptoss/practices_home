# import random

# coin = random.choice(["heads", "taisl"])

# print(coin)

# from random import choice

# coin = choice(["heads", "taisl"])

# print(coin)

'''
you can either write random.choice to print any random number
or you can define "from random import choice

and then you just simply write choice()
either way it works the same
'''
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card)
