# Welcome to trasure island...
# This is a fun random choice game which is made using conditional statements(if elif else, nested if and mutiple of all these, also using logical operators) and takes various input and on basis of input produce output
# One should play and see the working.


#Greetings
print("\n\n--------------------------------->WELCOME TO TREASURE ISLAND<---------------------------------\n")
direction=input("Enter l to move left andn r to move right:  ")
if direction=="l" or direction=="L":
    move=input('There is lake and middle of lake is the Island\nDo you want to wait for boat press w, if not for swim press s :  ')
    if move=="w" or move=="W":
        door=input("You are reached island unharmed, there are three door to choose: Red(r), Yellow(y), Blue(b):  ")
        if door=="r" or door=="R":
            print("\nOOPS!, LOST, Game Over!")
        elif door=="b" or door=="B":
            print("\nOOPS!, LOST, Game Over!")
        elif door=="Y" or door=="y":
            print("\nCONGRATS! You Won...")
        else:
            print("Wrong choice, re-run game there's no meaning to continue")
    elif move=="s" or move=="S":
        print("\nOOPS!, LOST, Game Over!")
    else:
        print("Wrong choice, re-run game there's no meaning to continue")
elif direction=="r" or direction=="R":
    print("\nOOPS!, LOST, Game Over!")
else:
    print("Wrong choice, re-run game there's no meaning to continue")

#------------------>I think I can also have use .lower() for removing case sensitivity of choices<------------------#
#------------------>FINISH<------------------#
