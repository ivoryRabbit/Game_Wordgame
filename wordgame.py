
# coding: utf-8

# In[1]:

from ps4a import loadWords, getFrequencyDict, displayHand, dealHand
import random, string

# In[2]:

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


# In[3]:

def getWordScore(word, n):
    length = len(word)
    A = 0; V = 0
    for i in range(length):
        A = A + SCRABBLE_LETTER_VALUES[word[i]]
    if length == n:
        V += 50
    return length * A + V


# In[4]:

#getWordScore("test", 4)

def getwordscore(word, n):
    a = 0; w = len(word)
    for char in word:
        a += SCRABBLE_LETTER_VALUES[char]
    a *= w
    if w == n:
        return a+50
    else:
        return a


# In[5]:

def updateHand(hand, word):
    for i in word:
        if i in hand:
            hand[i] += -1
    return hand


# In[6]:

#test updateHand:
u = updateHand({'c': 1, 'u': 1, 'e': 1, 'p': 2, 'a': 1, 'l': 1, 'f': 1, 'd': 1, 'y': 1}, 'apple')
print(u)


# In[7]:

def isValidWord(word, hand, wordList):
    count = 0; u = updateHand(hand, word)
    for i in word:
        if i not in u.keys():
            return False
        else:
            if u[i] >= 0:
                count += 1
    if (count == len(word)) & (word in wordList):
        return True
    else:
        return False


# In[8]:

#test isValidWord:
wordList = loadWords()
print(isValidWord("kwijibo", {'k': 1, 'o': 1, 'w': 1, 'j': 1, 'b': 1, 'i': 2}, wordList))
print(isValidWord("chayote", {'z': 1, 'o': 2, 'c': 2, 'a': 1, 't': 2, 'y': 1, 'u': 2, 'h': 1}, wordList))
print(isValidWord("hammer", {'e': 1, 'r': 1, 'a': 1, 'h': 1, 'm': 2}, wordList))
print(isValidWord("pear", {'x': 1, 'r': 1, 'v': 1, 'e': 1, 'q': 1, 'u': 1, 'a': 1, 'p': 1}, wordList))


# In[9]:

def calculateHandlen(hand):
    hand_sum = 0
    for i in hand.keys():
        hand_sum += hand[i]
    return hand_sum


# In[10]:

#test calculateHandlen:
calculateHandlen({'x': 1, 'r': 0, 'v': 0, 'e': 0, 'q': 0, 'u': 0, 'a': 0, 'p': 0})


# In[23]:

def playHand(hand, wordList, n):
    global y
    command = ""; finish = 1; total_score = 0
    y = 0
    while True:
        finish = 0
        current_hand = ""; temp = ""
        for i in hand.keys():
            temp += i * hand[i]
            finish += hand[i]
        if finish == 0:
            break
        for j in temp:
            current_hand = current_hand + " " + j
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
        print("\"" + str(command) + "\" earned " + str(getwordscore(command, n)) + " points. Total: " + str(total_score))
    if command == ".":
        print("Good bye! Total Score: " + str(total_score) + "points.")
    elif finish == 0:
        y = 1
        print("\n")
        print("Run out of letters. Total score: " + str(total_score) + " points.")


# In[24]:

#test playHand:
playHand({'a': 4}, wordList, 2)


# In[25]:

from copy import copy


# In[26]:

def playGame(wordList):
    print("Loading word list from file..." + "\n" + "\t" + str(len(wordList)) + " words loaded" )
    A = ["n", "r", "e"]
    Command = input("Enter \"n\" to deal a new hand, \"r\" to replay the last hand, or \"e\" to end game: ")
    a = 0; b = 0;
    while Command != "e":
        while Command not in A:
            Command = input("""Invalid command
Enter \"n\" to deal a new hand, \"r\" to replay the last hand, or \"e\" to end game: """)
        while (Command == "r") and (a == 0):
            Command = input("""You have not played a hand yet. Please play a new hand first
Enter \"n\" to deal a new hand, \"r\" to replay the last hand, or \"e\" to end game: """)
        if Command == "r":
            playHand(copy_hand, wordList, b)
        elif Command == "n":
            a = random.randint(2, 10)
            b = random.randint(2, 6)
            current_hand = dealHand(a)
            copy_hand = copy(current_hand)
            playHand(current_hand, wordList, b)
        if y == 1:
            break
        Command = input("Enter \"n\" to deal a new hand, \"r\" to replay the last hand, or \"e\" to end game: ")
    if y != 1:
        print("The end")


# In[27]:

playGame(wordList)

