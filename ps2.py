# Introduction to Computation and Programming Using Python (2021)
# Problem Set 2 from 2016 MIT 60001 course

# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    return all(c in letters_guessed for c in secret_word)

"""
for debugging is_word_guessed function
secret_word = 'apple'
letters_guessed = ['e','i','k', 'p', 'r', 's', 'a']
print(is_word_guessed(secret_word, letters_guessed))
"""

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    # string = '_ ' * len(secret_word) # builds base case, but ultimately I didn't go this way
    # print([c in letters_guessed for c in secret_word]) # checks if letter in secret_word has been guessed and creates a list
    # print([c + ' ' if c in letters_guessed else '_ ' for c in secret_word]) # this creates a list that looks correct
    # print(''.join(c +' ' if c in letters_guessed else '_ ' for c in secret_word)) # this does what I want
    # return ''.join(c +' ' if c in letters_guessed else '_ ' for c in secret_word) # before making edits to remove white space
    return ''.join(c if c in letters_guessed else '_' for c in secret_word)

"""
for debugging is_word_guessed function
secret_word = 'apple'
letters_guessed = ['e','i','k', 'p', 'r', 's']
print(get_guessed_word(secret_word, letters_guessed))
"""

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    return ''.join(c for c in string.ascii_lowercase if c not in letters_guessed)
    # joins every letter not in letters_guessed to the string

"""
for debugging get_available_letters function
secret_word = 'apple'
letters_guessed = ['e','i','k', 'p', 'r', 's']
print(get_available_letters(letters_guessed))
"""

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} long.')
    print(get_guessed_word(secret_word, letters_guessed))
    while not is_word_guessed(secret_word, letters_guessed): # will need a second condition for guesses_remaining > 0
      if guesses_remaining <= 0:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
        return
      print(f'You have {guesses_remaining} guesses left.')
      print(f'Available letters: {get_available_letters(letters_guessed)}')
      g = input('Please guess a letter: ')
      status = ''.join(c + ' ' for c in get_guessed_word(secret_word, letters_guessed)) # to display status in a readable way
      # verifies the input meets requirements
      if str.isalpha(g) is False:
        if warnings_remaining > 0:
          warnings_remaining -= 1
          print(f'Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {status}')
          print('-'*8)
          continue
        else:
          print(f'Oops! That is not a valid letter. You have no warnings left so you lose one guess: {status}')
          guesses_remaining -= 1
          print('-'*8)
          continue
      g = str.lower(g)
      # verifies the input has not previously been guessed
      if g in letters_guessed:
        if warnings_remaining > 0:
          warnings_remaining -= 1
          print(f'Oops! You\'ve already guessed that letter. You now have {warnings_remaining} warnings: {status}')
          print('-'*8)
          continue
        else:
          print(f'Oops! You\'ve already guessed that letter. You no warnings left so you lose one guess: {status}')
          guesses_remaining -= 1
          print('-'*8)
          continue
      letters_guessed.append(g)
      if letters_guessed[-1] in secret_word:
        status = ''.join(c + ' ' for c in get_guessed_word(secret_word, letters_guessed))
        print(f'Good guess: {status}')
      else:
        print(f'Oops! That letter is not in my word: {status}')
        guesses_remaining -= 1
        if g in [c for c in 'aeiou']:
          guesses_remaining -=1
      print('-'*8)
      
    print('Congratulations, you won!')
    print(f'Your total score for this game is: {guesses_remaining * len(set(secret_word))}')



# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    # return all(c in other_word for c in my_word if c in string.ascii_lowercase) # this does not check order
    # my_word_no_gaps = ''.join(c for c in my_word if c != ' ')
    # print(my_word_no_gaps)
    # return all(my_word_no_gaps[i] == other_word[i] for i in range(len(my_word_no_gaps)-1) if my_word_no_gaps[i] in string.ascii_lowercase )
    return all(my_word[i] == other_word[i] for i in range(len(my_word)) if my_word[i] in string.ascii_lowercase)

"""
# Debug for match_with_gaps
my_word = 'a__le'
other_word = 'apple'
print(match_with_gaps(my_word, other_word))
"""

def show_possible_matches(my_word, letters_guessed):
    '''
    my_word: string with _ characters, current guess of secret word
    letters_guessed: list of strings of lower case letters, previously guessed by the player # note that I added this argument to exclude words that have letters already guessed
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # pass
    # possible_matches = [other_word for other_word in wordlist if len(other_word) == len(my_word) and match_with_gaps(my_word, other_word)] # this is overinclusive, showing words where letters have been guessed
    # possible_matches = [other_word for other_word in possible_matches for i in range(len(my_word)) if my_word[i] == '_' and other_word[i] not in my_word] # tried to use this to modify above
    # possible_matches = [other_word for other_word in wordlist for i in range(len(my_word)-1) if len(other_word) == len(my_word) and match_with_gaps(my_word, other_word) and my_word[i] == '_' and other_word[i] not in my_word] # this was printing doubles
    possible_matches = [other_word for other_word in wordlist if len(other_word) == len(my_word) and match_with_gaps(my_word, other_word) and all(c not in other_word for c in string.ascii_lowercase if c in letters_guessed and c not in my_word) and all(my_word.count(c) == other_word.count(c) for c in my_word if c in string.ascii_lowercase)]
    if len(possible_matches) == 0:
      print('No matches found')
      return
    for i in possible_matches:
      print(i, end= ' ')
    print('')
"""
# debug for show_possible_matches
my_word = 'anple'
other_word = 'apple'
show_possible_matches(my_word)
"""

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass
    letters_guessed = []
    guesses_remaining = 6
    warnings_remaining = 3
    print('Welcome to the game Hangman!')
    print(f'I am thinking of a word that is {len(secret_word)} long.')
    print(get_guessed_word(secret_word, letters_guessed))
    while not is_word_guessed(secret_word, letters_guessed): # will need a second condition for guesses_remaining > 0
      if guesses_remaining <= 0:
        print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
        return
      print(f'You have {guesses_remaining} guesses left.')
      print(f'Available letters: {get_available_letters(letters_guessed)}')
      g = input('Please guess a letter: ')
      status = ''.join(c + ' ' for c in get_guessed_word(secret_word, letters_guessed)) # to display status in a readable way
      # verifies the input meets requirements
      if str.isalpha(g) is False:
        if g == '*': # asks for a hint
          show_possible_matches(get_guessed_word(secret_word, letters_guessed), letters_guessed)
          continue
        if warnings_remaining > 0:
          warnings_remaining -= 1
          print(f'Oops! That is not a valid letter. You have {warnings_remaining} warnings left: {status}')
          print('-'*8)
          continue
        else:
          print(f'Oops! That is not a valid letter. You have no warnings left so you lose one guess: {status}')
          guesses_remaining -= 1
          print('-'*8)
          continue
      g = str.lower(g)
      # verifies the input has not previously been guessed
      if g in letters_guessed:
        if warnings_remaining > 0:
          warnings_remaining -= 1
          print(f'Oops! You\'ve already guessed that letter. You now have {warnings_remaining} warnings: {status}')
          print('-'*8)
          continue
        else:
          print(f'Oops! You\'ve already guessed that letter. You no warnings left so you lose one guess: {status}')
          guesses_remaining -= 1
          print('-'*8)
          continue
      letters_guessed.append(g)
      if letters_guessed[-1] in secret_word:
        status = ''.join(c + ' ' for c in get_guessed_word(secret_word, letters_guessed))
        print(f'Good guess: {status}')
      else:
        print(f'Oops! That letter is not in my word: {status}')
        guesses_remaining -= 1
        if g in [c for c in 'aeiou']:
          guesses_remaining -=1
      print('-'*8)
      
    print('Congratulations, you won!')
    print(f'Your total score for this game is: {guesses_remaining * len(set(secret_word))}')


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    # secret_word = choose_word(wordlist)
    # secret_word = 'apple'
    # hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    # secret_word = 'apple' # uncomment this line and comment prior line for testing
    hangman_with_hints(secret_word)
