import random

word_list = ['bananas', 'blueberries', 'apples', 'pears', 'raspberries']
word = random.choice(word_list)

guess = input('Guess a letter \n')

if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')