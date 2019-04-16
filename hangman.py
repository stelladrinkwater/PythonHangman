#Program runs interactive hangman game
#Program assumes secret word is in lowercase

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
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

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed): #Problem 1
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if len(secretWord) == 1:
        if secretWord in lettersGuessed:
            return True
        else:
            return False
    else:
        if secretWord[0] in lettersGuessed:
            return isWordGuessed(secretWord[1:], lettersGuessed)
        else: 
            return False

def getGuessedWord(secretWord, lettersGuessed): #Problem 2
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    temp = ''
    for l in secretWord:
        if l in lettersGuessed:
            temp += l
        else:
            temp += '_'
    return temp

def getAvailableLetters(lettersGuessed): #Problem 3
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    temp = ''
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for l in alpha:
        if l in lettersGuessed:
            pass
        else: temp += l
    return temp       
    
def hangman(secretWord): #Problem 4
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    def explainStart():
        print('Welcome to the game, Hangman!')
        print('I am thinking of a word %s letters long.' % len(secretWord))
    
    explainStart()
    lettersGuessed = []
    spacer = '-------------'
    guessesLeft = 8
    
    print(spacer)
    
    while guessesLeft > 0 and isWordGuessed(secretWord, lettersGuessed) == False:
        print('You have %s guesses left.' % guessesLeft)
        print('Available letters: ' + getAvailableLetters(lettersGuessed))
        letterGuessed = input('Please guess a letter: ')
        lettersGuessed.append(letterGuessed.lower()) 
       
        if letterGuessed in lettersGuessed[:-1]:
            print("Oops! You've already guessed that letter: " + getGuessedWord(secretWord, lettersGuessed))
        
        elif letterGuessed.lower() in secretWord:
            print('Good guess: ' + getGuessedWord(secretWord, lettersGuessed))
            if isWordGuessed(secretWord, lettersGuessed) == True:
                break                
        else:
            print('Oops! That letter is not in my word: ' + getGuessedWord(secretWord, lettersGuessed))
            guessesLeft -= 1
            
        print(spacer)
    
    if isWordGuessed(secretWord, lettersGuessed) == True:
        print(spacer)
        print('Congratulations, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' + secretWord)
            
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
