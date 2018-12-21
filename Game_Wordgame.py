# The 6.00 Word Game

import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code

WORDLIST_FILENAME = "words.txt"

def loadWords():
    # load a list of words.
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print("  {0} words loaded.".format(len(wordList)))
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
# (end of helper code)
# -----------------------------------

def displayHand(hand):
    # displays the letters currently in the hand.
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line

def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

# coding: utf-8

import random, string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

def getwordscore(word, n):
    # score of your word.
    length = len(word); point = 0
    for i in range(length):
        point = point + SCRABBLE_LETTER_VALUES[word[i]]
    score = length * point
    if n == length:
        score += 50
    return score
# test getwordscore
#getwordscore("test", 4)

def updateHand(hand, word):
    for letter in word:
        if letter in hand:
            hand[letter] += -1
    return hand
# test updateHand:
#u = updateHand({'c': 1, 'u': 1, 'e': 1, 'p': 2, 'a': 1, 'l': 1, 'f': 1, 'd': 1, 'y': 1}, 'apple')
#print(u)

def isValidWord(word, hand, wordList):
    count = 0; upHand = updateHand(hand, word)
    for letter in word:
        if letter not in upHand.keys():
            return False
        else:
            if upHand[letter] >= 0:
                count += 1
    if (count == len(word)) & (word in wordList):
        return True
    else:
        return False
#test isValidWord:
#wordList = loadWords()
#print(isValidWord("kwijibo", {'k': 1, 'o': 1, 'w': 1, 'j': 1, 'b': 1, 'i': 2}, wordList))
#print(isValidWord("chayote", {'z': 1, 'o': 2, 'c': 2, 'a': 1, 't': 2, 'y': 1, 'u': 2, 'h': 1}, wordList))
#print(isValidWord("hammer", {'e': 1, 'r': 1, 'a': 1, 'h': 1, 'm': 2}, wordList))
#print(isValidWord("pear", {'x': 1, 'r': 1, 'v': 1, 'e': 1, 'q': 1, 'u': 1, 'a': 1, 'p': 1}, wordList))

def calculateHandlen(hand):
    hand_sum = 0
    for letter in hand.keys():
        hand_sum += hand[letter]
    return hand_sum
#test calculateHandlen:
#calculateHandlen({'x': 1, 'r': 0, 'v': 0, 'e': 0, 'q': 0, 'u': 0, 'a': 0, 'p': 0})

def playHand(hand, wordList, n):
    global y
    command = ""; finish = 1; total_score = 0
    y = 0
    while True:
        finish = 0
        current_hand, temp = "", ""
        for letter in hand.keys():
            temp += letter * hand[letter]
            finish += hand[letter]
        if finish == 0:
            break
        for letter in temp:
            current_hand = current_hand + " " + letter
        print("\n")
        print("Current Hand: " + current_hand)
        command = input("Enter word, or a \".\" to indicate that you are finished: ")
        if command == ".":
            break
        while (isValidWord(command, hand, wordList) == False) and (command == "."):
            print("\n")
            print("Current Hand: " + current_hand)
            command = input("Try Again. Enter word, or a \".\" to indicate that you are finished: ")
        if command == ".":
            break
        total_score += getwordscore(command,n)
        print("\"{0}\" earned {1} points. Total: {2}".format(command,getwordscore(command, n),total_score))
    if command == ".":
        print("Good bye! Total Score: {0} points.".format(total_score))
    elif finish == 0:
        y = 1
        print("\n")
        print("Run out of letters. Total score: {0} points.".format(total_score))
#test playHand:
#playHand({'a': 4}, wordList, 2)

from copy import copy
wordList = loadWords()

def playGame(wordList):
    choice = ["n", "r", "e"]
    command = input("Enter \"n\" to deal a new hand, \"r\" to replay the last hand, or \"e\" to end game: ")
    a = 0; b = 0;  # this two number will be random integers for your score.
    while command != "e":
        while command not in choice:
            command = input("""Invalid command
Enter \"n\" to deal a new hand, \"r\" to replay the last hand, or \"e\" to end game: """)
        while (command == "r") and (a == 0):
            command = input("""You have not played a hand yet. Please play a new hand first
Enter \"n\" to deal a new hand, \"r\" to replay the last hand, or \"e\" to end game: """)
        if command == "r":
            playHand(copy_hand, wordList, b)
        elif command == "n":
            a = random.randint(2, 10)
            b = random.randint(2, 6)
            current_hand = dealHand(a)
            copy_hand = copy(current_hand)
            playHand(current_hand, wordList, b)
        if y == 1:
            break
        command = input("Enter \"n\" to deal a new hand, \"r\" to replay the last hand, or \"e\" to end game: ")
    print("The end")

# play the game.
playGame(wordList)