word_list = ["camel", "baboon", "ardvarak"]

import random

chosen_word = random.choice(word_list)

guess = input("Enter the letter: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")