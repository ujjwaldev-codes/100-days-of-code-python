"""The Calculator is the python program which I have coded on my own as a part
of my 100 days of code by Angela Yu.
Through this I got a thorough idea of functions, and not only defining or calling but also passing arguments and returning and storing its value or passing it to another 
fucntion or printing results

What program do?
1.) The program asks for two value and choice of operations to be performed on the two input values
2.) Then user need to make choice either to continue with same calculation(taking previous result as first input) or with new calculations or exit the program...
"""

#Defining fucntions
def add(n1, n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def divide(n1, n2):
    return n1/n2
def multiply(n1,n2):
    return n1*n2
def calc(num_1,num_2,choice):
    if choice =="*":
        return multiply(num_1,num_2)
    elif choice =="/":
        return divide(num_1,num_2)
    elif choice =="+":
        return add(num_1,num_2)
    elif choice =="-":
        return subtract(num_1,num_2)
    else:
        return "Invalid Operator Choice!!!"
choose ="" 
result = calc  
c=0     
#Greetings and visuals
print("\n\n******************CALCULATOR******************\n")
# looping
while choose!= "e":
    if c==1:
        num_1 =final_result
    else:
        num_1 =int(input("Enter a number :  "))
    choice = input("Which operation you wish to go with : (type) \n'*' --> multiply\n'+' --> Add\n'-' --> Subtract\n'/' --> Divide\n")
    num_2 =int(input("Enter another number :  "))
    final_result = result(num_1,num_2,choice)
    print("\nYour Answer :  "+str(final_result)+"\n")
    choose = input("Enter 'n' to continue with new calculations, else 'e' for exit or 'any other letter' to continue calculation with the answer:  ")
    if choose =="n":
        c=0
    else:
        c=1

# Finished, It was quiet challenging not because of dealing with fucntion but because of looping and giving choice either to retain same result or new calculation or exit

    
    

