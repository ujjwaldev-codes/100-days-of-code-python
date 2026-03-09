# WELCOME, to the most famous and most played game world wide : Rock, Paper, Scissor
# This is achieved in python program using concept of randomisation, conditionals, lists

# After greetings the program ask to choose either rock paper scissor
# Then randomly result into either of three, and using conditional statements decide whether program won or user or it is draw...
# The program also teminates with wrong input error
import random
print("\n---------------------------> ROCK, PAPER, SCISSOR <---------------------------\n")
options=["Rock", "Paper", "Scissor"]
user_choice=int(input("PRESS 0 for rock, 1 for paper and 2 for scissor:  "))
    # ASCII ARTS (Designs downloaded from google)
    # ERROR ---- CORRECT WAY BELOW
        # print('    _______
        #        ---    ____)____
        #                  ______)
        #                  _______)
        #                _______)
        #        --- __________)
        #     ')
        # ERROR ---- CORRECT WAY BELOW
paper =["   _______",
        "--    ____)____",
        "          ______)",
        "          _______)",
        "        _______)",
        "--- __________)"]
scissor = ["   _______",
          "---    ____)____",
          "          ______)",
          "       __________)",
          "      (____)",
          "--- __(___)",]
rock=["    _______",
     " ---'   ____)",
     "       (_____)",
     "       (_____)",
     "       (____)",
     " ---.__(___)",]
if(user_choice==1 or user_choice==0 or user_choice ==2):
    if user_choice==1:
        print(paper[0]+"\n"+paper[1]+"\n"+paper[2]+"\n"+paper[3]+"\n"+paper[4]+"\n"+paper[5]+"\n")
    if user_choice==2:
        print(scissor[0]+"\n"+scissor[1]+"\n"+scissor[2]+"\n"+scissor[3]+"\n"+scissor[4]+"\n"+scissor[5]+"\n")
    if user_choice==0:
        print(rock[0]+"\n"+rock[1]+"\n"+rock[2]+"\n"+rock[3]+"\n"+rock[4]+"\n"+rock[5]+"\n")
    program_choice_index = random.randint(0, 2)
    program_choice = options[program_choice_index]
    print("\nProgram choice: "+program_choice+"\n")
    #conditionals
    if program_choice_index==1:
        print(paper[0]+"\n"+paper[1]+"\n"+paper[2]+"\n"+paper[3]+"\n"+paper[4]+"\n"+paper[5]+"\n")
    if program_choice_index==2:
        print(scissor[0]+"\n"+scissor[1]+"\n"+scissor[2]+"\n"+scissor[3]+"\n"+scissor[4]+"\n"+scissor[5]+"\n")
    if program_choice_index==0:
        print(rock[0]+"\n"+rock[1]+"\n"+rock[2]+"\n"+rock[3]+"\n"+rock[4]+"\n"+rock[5]+"\n")
    if program_choice == options[user_choice]:
        print("DRAW !")
    elif (program_choice == options[1] and options[user_choice] == options[0]) or (program_choice == options[0] and options[user_choice] == options[2]) or (program_choice == options[2] and options[user_choice] == options[1]):
        print("YOU LOST !")
    else:
        print("YOU WON !")
else:
    print("Wrong input")

# Initially quiet hesitating to write so many combinations of lose or win untill got a good idea
# On using ASCII codes I stuck in syntax error : unterminated string literal:: SOLUTION --> Put each line in a list and printed listes with new line for each element
# Happy to use ASCII ARTS to make Program alive
# Art credit: Joan Stark — thank you!
# Art credit: Joan Stark — thank you!
# ------------------> FINISH <------------------ #
