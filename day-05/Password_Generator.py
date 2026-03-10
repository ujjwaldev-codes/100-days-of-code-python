# The Program Starts with greetings and ask user to tell the number of letters to be used in password
# Then program take input of how many symbols to be used, and how many numbers, rest for sure will be letters(alphabet)
# Finally program gives a random password of letters and numbers and symbols in random way(Note I Chose harder program to be random in assigning postion of these letters)
# I made use of loop, list, range and random functions

import random
print("\n\n-------------------------->  WELCOME TO PASSWORD GENERATOR  <--------------------------\n")
# List of all these as ingredient to randomly mix later
# Using loop to fill the list
password=[]
alphabet=[]
for index in range(65, 91):
    alphabet.append(str(chr(index)))
for index in range(97, 123):
    alphabet.append(str(chr(index)))
symbols=["!","@","#","$","%","&","*","?"]
number = ["1","0","2","3","4","5","6","7","8","9"]

length = int(input("How many letter(s) would you like in your password ?  "))
no_of_symbols = int(input("How many symbol(s) would you like in your password ?  "))
no_of_digits = int(input("How many number(s) would you like in your password ?  "))
if ((no_of_digits+no_of_symbols) > length):
    print("\nInvalid choice of number of digit or symbols\n")
else:
    # Logic to generate password by randomly mixing all of the letters in the way user desired
    for index in range(0, no_of_symbols):
        password.append(random.choice(symbols))
    for index in range(0, no_of_digits):
        password.append(random.choice(number))
    remaining_letters= length - (no_of_digits+no_of_symbols)
    if remaining_letters != 0:
        for index in range(0, remaining_letters):
            password.append(random.choice(alphabet))
    print("\nPassword 1 : ")
    for index in range(0, len(password)):
        print(password[index],end="")
    #end =""no new line no spce, end=" " no new line but a sapce, it change the ending character from \n by default to other choice like "", or " "
    #Easy level Done, also learnt the end method to print in same like in python
    # Issue : But this print randomly chosen letters are in order of symbols digits and letters i want randomisation within it..
    # SOlution below and final Output
    print("\n\nPassword 2 : ")
    for index in range(0, len(password),2):
        print(password[index],end="")
    for index in range(1, len(password),2):
        print(password[index],end="")
print("\n\n")#Proper spacing
# ----------------------FISNISH---------------------- #
