import random

word_list = ['bananas', 'blueberries', 'apples', 'pears', 'raspberries']
word = random.choice(word_list)

def ask_for_input():
    while True:
        guess = input("Guess a letter \n")
        if len(guess) == 1 and guess.isalpha():
            break
        else:
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

def check_guess(guess):
    guess = guess.lower()
    if guess in word:
        print("Good guess! {} is in the word".format(guess))
    else:
        print("Sorry, {} is not in the word. Try again.".format(guess))

ask_for_input()