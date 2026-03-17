import random
print("\n*****************************  WELCOME  TO  NUMBER  GUESSING  GAME  ******************************\n")
attempts = 0
n=0
status=input("Do you want to start the game -> 'yes' or 'no' : \n")
while status =="yes":
    print("I am thinking of a number between 1 and 100 :")
# Asking level to fix attempts to give for correct guess
    while n==0:
        level = input("Choose the difficulty level : 'hard' or 'easy' (type) :  ")
        if(level=="hard"):
            attempts=5
            n=1
        elif(level =="easy"):
            attempts=10
            n=1
        else:
            print("Invalid Level Choice")
            n=0
    random_number = random.randint(1,101)
# print(random_number)
# print(level)
# print(attempts)
# Above were checking routine by print statement

    while attempts!=0:
        print(f"\nYou Have {attempts} attempts left to guess the number...")
        guess = int(input("\nMake a guess : "))
        if(guess ==random_number):
            print(f"\nYou made it ! The Number Is --> {random_number}\n\n")
            attempts=0
        else:
            if guess > random_number:
                print("It is High.\nGuess again.")
            if guess <random_number:
                print("It is Low.\nGuess again.")
            attempts =attempts-1
            if attempts==0:
                print(f"Attempts Over... The number is --> {random_number}\n\n")
    status =input("Do you want to play again -> 'yes' or 'no' : \n ")
print("\n******************************  GAME  TERMINATED  ****************************\n")
