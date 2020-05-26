"""
The License plate Game is an in-terminal game where the objective is to think of words
that contain letters in a certain order.
for example:
letters B U T
Think of words: but, distribute, robust, bust, busted, etc.
"""


def gen_dictionary(filepath):
    words = []
    with open(filepath) as f:
        line = f.readline()
        while line:
            # Add each word to the word list.
            # Subtract 1 to avoid \n
            words.append(line[:len(line)-1])
            line = f.readline()
    print(f'Created Dictionary with {len(words)} words.')
    return words


class WordFinder:
    """WordFinder takes a string of letters, and
    finds all words containing those letters
    in that order, but not necessarily next to each other.
    """
    filepath = "words.txt"
    characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    def __init__(self):
        self.words = gen_dictionary(WordFinder.filepath)
        self.found_words = []

    def find_words(self, letters):
        """
            Find all words with the letters found in order
        """
        self.found_words = []
        for w in range(len(self.words)):
            sub_str = self.words[w]
            for l in range(len(letters)):
                # Check if the letter is in the substring

                if letters[l] in sub_str:
                    # New substring is the rest of the word
                    if l == len(letters) - 1:
                        self.found_words.append(self.words[w])
                        print(f'{self.words[w]}')
                    elif len(sub_str) != 0:
                        sub_str = sub_str[sub_str.index(letters[l]):]
                else:
                    break
        return self.found_words


class LicensePlateGame:
    def __init__(self, letters=None):
        self.letters = letters
        self.wf = WordFinder()
        self.words_to_find = []
        self.found_words = []

    def start_game(self):
        """
        Begins the game. Sets the letters from user input.
        Finds words from those letters.
        Initializes user-word-guessing phase
        """
        print('Welcome to the License Plate Game')
        if self.letters is None:
            print('Pick 2-4 letters -- like ones you might see on a license plate (without the numbers)')

            good_input = False

            while not good_input:

                i = input()
                for letter in range(len(i)):
                    if i[letter] not in WordFinder.characters:
                        good_input = False
                        continue
                    elif letter == len(i)-1:
                        self.letters = i
                        good_input = True
                        break
                print('Please enter 2-4 letters...')

        print(f'You have chosen these letters: {self.letters}')
        print('For this game, you need to think of all words that have those letters in them.')
        print('The letters must be in order, but do not have to be consecutive.')
        self.set_words()
        self.user_hunt_phase()

    def set_words(self):
        self.words_to_find = self.wf.find_words(self.letters)
        self.found_words = []

    def user_hunt_phase(self):
        print('Quit at any time by entering "quit!!" or enter "help!!" for a hint')
        print('Enter a word...')
        w = input()
        if w == "quit!!":
            return
        elif w in self.words_to_find or w == "help!!":
            if w != "help!!":
                print("You've found a word!")
                self.found_words.append(w)
                self.words_to_find.pop(self.words_to_find.index(w))
            else:
                print(f"Here's a word: {self.words_to_find[0]}")
                self.words_to_find.pop(0)
            if 0 == len(self.words_to_find):
                print(f"You've found all {len(self.found_words)} words!")
                return self.start_game()
            else:
                print(f'There are {len(self.words_to_find)} more words to find.')
        else:
            print("That word isn't in the list. Please try another.")
        return self.user_hunt_phase()


lpg = LicensePlateGame()
lpg.start_game()
