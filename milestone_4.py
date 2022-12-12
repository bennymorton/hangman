import random

word_list = ['bananas', 'blueberries', 'apples', 'pears', 'raspberries']

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

test = Hangman(word_list)

print(test.word)
print(test.word_guessed)
print(test.num_letters)
print(test.list_of_guesses)