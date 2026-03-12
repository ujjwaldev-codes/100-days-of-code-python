# HangMan is one of the most beautiful guessing game.
# Not only to play but while its creation I polished my concepts : for and while loop,
# if/else, lists, strings, ranges, modules
# here is the link of demo hangman i refer while coding it on python, under guidance of my teacher Angela Yu -  https://appbrewery.github.io/python-day7-demo/

# Firstly I made flowchart programming for the game, the game is like we are given a definite number of lettered words.
# We are given limited no, of chance to guess its word.
# For each correct it become easy for we can guess the word(of course meaningful one) and make less miss
# But as we have correct misses, the game start building a rope to hand the man, after finite no, of miss, the game over.

# There were many ways to acheieve.

# # Logic or flowchart(algorithm of the program): WORKING:
# 1. Generate a random word.
# 2. Print no. of underscore as may letters in that word.
# 3. Ask for guess and check if any letter of word match the guessed letter
# 4. If guessed letter in the random word, then, print underscores for word with, aswer yess
# 5. If all the blanks filled : Won, else ask for other letter
# 6. If the gueesed letter wrong count the miss with grwoing hangman and if balnk filled won but before that hang man grwe miss exceeded then pemit levell lost

# Making meaningful english words list: and randomly choose one for user guess

import random
miss=0
list_of_words = ["About", "After","Again","Always","Around","Ask","Back","Before","Come","Do","Down","Eat","Every","Find","First","Get","Good","Hand","Help","Hold","Home","House","Keep","Know","Life","Like","Make","Man","Many","Meet","Put","Reach","See","Show","Small", "fish", "meat","computer", "robot", "mouse"]
choosen_word = (random.choice(list_of_words)).lower() # To make the game case insensitive
hidden_word=[]
final_word=""
print("\n")
#initialiszation of the game and as moved on updating either miss(counter variable or final_word)
for index in range(len(choosen_word)):
    hidden_word.append("_")
for index in range(len(choosen_word)):
    final_word+=hidden_word[index]
while miss !=5 and not(final_word == choosen_word):
    guess = input("Guess a letter for : "+ final_word + "\n")
    if not (guess in choosen_word):
        print("Wrong...")
        miss +=1
        print((str(5-miss))+"/5 Choice(s) left: \n")
    if(miss==5):
        print("LOST !!! ---- It was --> "+ choosen_word.lower())
    else:
        for i in range(len(choosen_word)):
            if(guess ==choosen_word[i]):
                print("Right...")
                position=i
                hidden_word[i]=choosen_word[i]
                final_word=""
                for index in range(len(choosen_word)):
                    final_word+=hidden_word[index]
    if(final_word == choosen_word):
        print("\nWON !!! yes, it was ------> "+choosen_word+"\n")    

# Visual of hangman was bit tricky and complex so took help my instructor code, only for that purpose
# It was most challenging as of now, motivated in solving on my own

