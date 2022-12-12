import random

word_list = ['banana']

# 'blueberries', 'apples', 'pears', 'raspberries']

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list)
        self.word_guessed = []
        for _ in range(len(self.word)):
            self.word_guessed.append('_')

        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print('Good guess! {} is in the word.'.format(guess))
            for i, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[i] = letter
            self.num_letters = self.num_letters - 1
            print(self.word_guessed)
        else:
            self.num_lives = self.num_lives -1
            print('Sorry, {} is not in the word.'.format(guess))
            print('You have {} lives left.'.format(self.num_lives))

    def ask_for_input(self):
        while True:
            guess = input('Guess a letter ')
            if len(guess) != 1 or not guess.isalpha():
                print('Invalid letter. Please, enter a single alphabetical character.')
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break

def play_game(word_list):
    game = Hangman(word_list, 3)
    while True:
        if game.num_lives == 0:
            print('You lost!')
            break
        elif game.num_letters > 0:
            game.ask_for_input()
        else:
            print('Congratulations. You won the game!')
            break

play_game(word_list)