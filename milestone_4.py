import random

class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        word = random.choice(self.word_list)

        word_guessed = []
        for i in range(len(word)):
            word_guessed = word_guessed.append('_')
        
        num_letters = len(set((letter for letter in word)))

        list_of_guesses = []