import random



class Hangman:
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(self.word_list)

        self.word_guessed = []
        char_list = []

        for i in range(len(self.word)):
            self.word_guessed = self.word_guessed.append('_')
            char_list.append(self.word[i])

        self.num_letters = set((char_list))

        self.list_of_guesses = []