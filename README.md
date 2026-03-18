# 100 Days of Python – Angela Yu Bootcamp

My personal journey through Dr. Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp** (Udemy).  
Daily Python practice, small projects, notes, and fun experiments! 🐍✨

**Goal:** Code every day for 100 days → build real projects from beginner basics to advanced apps, games, websites & more.  
**Started:** March 6, 2026 
**Tracking:** #100DaysOfCode

## Progress Tracker
- [X] Day 1 – Band Name Generator  
- [X] Day 2 – Tip Calculator  
- [X] Day 3 – Treasure Island
- [X] Day 4 - Rock Paper Scissor Game
- [X] Day 5 - Password Generator
- [X] Day 6 - Maze Escape
- [X] Day 7 - Hangman
- [X] Day 8 - Ceaser Cipher
- [X] Day 9 - The Secret Auction
- [X] Day 10 - Calculator
- [X] Day 11 - The Blackjack Game
- [X] Day 12 - Number Guessing Game
- [X] Day 13 - NO Project(learnt Error Handling Tips)
(→ I'll check these off as I go! Feel free to fork or ⭐ if you're following along)

## About the Course
- Link: [Udemy Course](https://www.udemy.com/course/100-days-of-code/)  
- Instructor: Dr. Angela Yu  
- Focus: Hands-on projects, no fluff — perfect for beginners like me!

## How to Run the Projects (Using Visual Studio Code)

All projects are simple Python scripts you run in VS Code. Here's the easiest way:

1. **Open the repo in VS Code**  
   - Download/clone this repo to your computer.  
   - In VS Code: File → Open Folder → select the folder (e.g., `100-days-of-python`).

2. **Make sure Python is set up in VS Code**  
   - Install the official **Python extension** by Microsoft (search "Python" in Extensions tab if not already installed).  
   - VS Code will ask to select your Python interpreter — choose the one you installed (usually shows as Python 3.x).

3. **Run any day's script** (choose your favorite method):  
   - **Easiest (recommended for beginners):** Open the .py file (e.g., `day-01/band_name_generator.py`) → click the green **▶️ Run Python File** play button in the top-right corner of the editor.  
     This opens a terminal automatically and runs the code!  
   - **Alternative:** Right-click inside the code editor → select **Run Python File in Terminal**.  
   - **Manual way (using terminal):**  
     Open the integrated terminal in VS Code (Terminal → New Terminal or Ctrl+` ) → type:  
     ```bash
     python day-01/band_name_generator.py
     ```  
     (Replace with the correct day/folder/file name. On some systems use `python3` instead of `python`.)

4. **Interact with the program**  
   - The terminal will ask questions (e.g., "What's the city?") → type your answer and press Enter.  
   - See the output right there!

**Note:** For days with libraries (like Turtle or Requests later), you might need to install them once with `pip install turtle` (or similar) in the terminal — but most early days need nothing extra.

Happy running! 🐍 If you run into issues, check that Python is in your PATH or ask in the course community.


## Day 1: March 6, 2026
**What I Learned :**
print(), input(), string concatenation, len(), comments, variable and rules to name them debugging 

**Project Name :** Band Name Generator

**How Program Works**
1. Greetings to user of the program.
2. Taking two pieces of information : name of home-town and pet.
3. Printing the suggested name of band by simple fun logic of combining the two names above.

**Files**
- [Code File](day-01/band_name_generator.py)
- [Image Of Teminal Output](day-01/band_name_generator-OUTPUT-SS.png)



## Day 2: March 7, 2026
**What I Learned :**
Today I learnt, mathematical operation in python, data type and type conversions, f-strings(Useful to insert number with strings in printing statements, since direct concatenation of strings and int not possible.
Numbers(int float etc), functions( breif idea), type(), round(), and str() function and built: bmi calculator and a Tip Calculator, 

NOTE: I made mistake and learnt that input() always return string
final_bill = bill*(1+(tip_percentage/100))
TypeError: unsupported operand type(s) for /: 'str' and 'int'
and "10"/100 raise error, so....
SOLUTION : use float(input()), to get number : in bill percent ad no. of people

**Project Name :** Tip Calculator

**How Program Works**
1. Greetings to user of the program.
2. Taking three pieces of information : Bill, Tip Percentage, No. of people splitting bill.
3. Printing the Final Bill incl. Tip and amount each has to pay.
4. I tried to have fanciness by proper spacing and also made good use of round and type casting to produce result as per money calculation 2 decimal place.

**Files**
- [Code File](day-02/Tip_Calculator.py)
- [Image Of Teminal Output](day-02/Tip_Calculator-OUTPUT-SS.png)


## Day 3: March 8, 2026
**What I Learned :**
Today I learnt, the conditionl statements, block codes, logical operators (to combine two or more condition in a line) and their scopes, BMI interpretation (coding exercise) and voting eligibility test using python code, even or odd number analysis and logic, pizza delivery program(as per course exercise), The Treasure Island(Project of the day)
Finally make use of Logical and other operators in my python code file for treasure island project, I concluded my today's learning chunk by practising if/elif/else/nested if(s) and knowing .lower() function.

NOTE: conditional statements direct the flow of program as per the conditions specified which will checked during execution and generally depends on the input from user. 
NOTE: I also learnt to use \' to use apostrophe and to use quotation in printing statement, we must enclose string between '' instead of "" in that case.

**Project Name :** Treasure Island

**How Program Works**
1. Greetings to user of the program.
2. Program keep asking choices like to move left or right, use boat or swim and to open which door to reach to treasure, in each condition either make you conitnue and another says game over, terminating the game.

**Files**
- [Code File](day-03/Treasure_Island.py)
- [Image Of Teminal Output](day-03/Treasure_Island-OUTPUT-SS.png)
 

## Day 4: March 9, 2026
**What I Learned :**
1. Randomisation is very important and it is amazing that deterministic machines can be used as random number generators(leading to random results).
2. Lists used a lot in python codes
3. Idea of import keyword to use modules and their predefined function in the program
4. Idea of modules in python: Module: consider set of instruction that deals with a task providing teamwork and modularity in program, it devide the task into small chunks.
5. Using modules provides resuability.
6. Generated numbers with random.randint() and random.random()
7. Head tail program
8. Offset and Appending Items to List
9. When we have something common among itms or are in some order and can be grouped together called list.
10. Defining using lists in python and using append(), extend(), random.choice(list).
11. Also learnt the concept of list of list and IdexError in list.
12.  And finally a rock paper scissor game specially to make use of randomisation

NOTE: Initially quiet hesitating to write so many combinations of lose or win untill got a good idea. On using ASCII codes I stuck in syntax error : unterminated string literal:: SOLUTION --> Put each line in a list and printed listes with new line for each element
Happy to use ASCII ARTS to make Program alive
Art credit: Joan Stark — thank you! 

**Project Name :** Rock Paper Scissor Game

**How Program Works**
This is achieved in python program using concept of randomisation, conditionals, lists
After greetings the program ask to choose either rock paper scissor
Then randomly result into either of three, and using conditional statements decide whether program won or user or it is draw...
The program also teminates with wrong input error.

**Files**
- [Code File](day-04/Rock-Paper-Scissor.py)
- [Image Of Teminal Output](day-04/day-04-rock-paper-scissor-terminalOutputSS.png)



## Day 5: March 10, 2026
**What I Learned :**
Passwords these days must be strong and different for different accounts, to aviod breaches.
Today other than learning loop and using them in list, I finally end up with a random password generator.
Implemented max() and try to make my own code for same functionality in python list and sum of all numbers in list using loop, as well as sum() of python list.
Used range(), function and studied its behaviour, found it has to be used with other function like loop in this case.

NOTE: Learning random.shuffle was turning point of the project

**Project Name :** Password Generator

**How Program Works**
The Program Starts with greetings and ask user to tell the number of letters to be used in password
Then program take input of how many symbols to be used, and how many numbers, rest for sure will be letters(alphabet)
Finally program gives a random password of letters and numbers and symbols in random way(Note I Chose harder program to be random in assigning postion of these letters)
I made use of loop, list, range and random functions.

In-Projet-Learnings and Challenges:
List of all letters as ingredient to randomly mix later, storing in a list, for alphabet I used loops. 
Logic to generate password by randomly mixing all of the letters in the way user desired.
Also learnt end keyword to use with print statement: end =""no new line no spce, end=" " no new line but a sapce, it change the ending character from \n by default to other choice like "", or " "(During priting each string in password list to make word not in different line or with sapcing, I used end="".
Challenge : But this print randomly chosen letters are in order of symbols digits and letters I want randomisation within it... So I learnt and implemented random.shuffle() which take list as input and shuffle the elements randomly each time. this makes password UNEVEN.


**Files**
- [Code File](day-05/Password_Generator.py)
- [Image Of Teminal Output](day-05/PasswordGeneratorTerminalOutput-SS.png)




## Day 6: March 11, 2026
**What I Learned :**
I learnt about functions.
After solving so many Karel Robot, links below. Function are like modules of set of instructions, that perform the task on beign invoked or call
and may or may not return value. It may or may not take input. It can be defined by user or can be predefined to use in the program, python libraries has various functions, many we used them intensively.
e.g. print(), len(), shuffle(), they belongs to various modules and libraries. 
def keyword helps us to create a function
Fucntion reduces code lines, and provides not only modularity but also reusability

Karel robot - For Concept of function
https://docs.python.org/3/library/functions.html
why to always repeat telling the processes like to make robot bringing milk for you daily, just put all those set of instruction on a page and entitile the page as Bring_Milk()
More readble and easy error debugging
https://reeborg.ca/reeborg.html
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

Spaces are preffered over tabs by most of online developer community for indentation
Indentation imp in defining loop conditional statement and also for defining functions...
While Loop - Continue running while the condition is true

For Statement : for item_in_list:
                        Do sth
                 for number in range(a,b):
                        print(number)

While Statement : while sth_true:
                          Keep Moving

https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json
for list traversing and range, while when we donot care how many times while is better
Avoid infinite loops, more prone in while loop()
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

Very happy motivated by learning the function by learning various hurdles level of karel robot of Reeborg's world(LINKS ABOVE)


NOTE: Highly Challenging.

**Project Name :** Escape Maze

**How Program Works**
https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json
Reeborg was exploring a dark maze and the battery in its flashlight ran out.

Write a program using an if/elif/else statement so Reeborg can find the exit. The secret is to have Reeborg follow along the right edge of the maze, turning right if it can, going straight ahead if it can’t turn right, or turning left as a last resort.

What you need to know
The functions move() and turn_left().
Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
How to use a while loop and if/elif/else statements.
It might be useful to know how to use the negation of a test (not in Python).

**Files**
- [Image Of Teminal Output + Code](day-06/MAZE-OUTPUT+CODE.png)



## Day 7: March 12, 2026
**What I Learned :**
HangMan is one of the most beautiful guessing game.
Not only to play but while its creation I polished my concepts : for and while loop,
if/else, lists, strings, ranges, modules
Here is the link of demo hangman I refer while coding it on python, under guidance of my teacher Angela Yu -  https://appbrewery.github.io/python-day7-demo/
Firstly I made flowchart programming for the game, the game is like we are given a definite number of lettered words.

**Project Name :** Hangman

**How code work :**
We are given limited no, of chance to guess its word.
For each correct it become easy for we can guess the word(of course meaningful one) and make less miss
But as we have correct misses, the game start building a rope to hand the man, after finite no, of miss, the game over.
There were many ways to acheieve.
Logic or flowchart(algorithm of the program): WORKING:
1. Generate a random word.
2. Print no. of underscore as may letters in that word.
3. Ask for guess and check if any letter of word match the guessed letter
4. If guessed letter in the random word, then, print underscores for word with, aswer yess
5. If all the blanks filled : Won, else ask for other letter
6. If the gueesed letter wrong count the miss with grwoing hangman and if balnk filled won but before that hang man grwe miss exceeded then pemit levell lost

Making meaningful english words list: and randomly choose one for user guess
Very happy motivated by learning, unfortunatly at present I could not implement hangman hanging visual, will try soon or then.

NOTE: Highly Challenging.

**Files**
- [Code File](day-07/Hangman.py)
- [Image Of Teminal Output 1](day-07/Hangman(OUTPUT-1).png)
- [Image Of Teminal Output 2](day-07/Hangman(OUTPUT-2).png)
 

## Day 8: March 13, 2026
**What I Learned :**
More on functions: Defining fucntion and calling with inputs(parameters and argument)
Suppose we want everytime different name...
Variable that function have is parameter and the actual value that function receive to store in that variable is argument
name , name1 and name2 are parameter
girl and boy is variable containing actual value do they are argument
Positional Arguments:
Learnt about ord() function which returns the ASCII value of a character
keyword argument to avoid interchange problem
Learnt about the function count() ---> it counts the no of times a string appears in the given string
e.g name.count("l")
Positional Arguments.

**Project Name :** Ceaser Cipher(encoding and decoding)

**How code work :**
This progrgam is inpired by the Ceasar Cipher who in order to send secret military signal
used to encrypt it by shifting letters of alphabet like for a can be represented by say d
This program using the same methodology asks for the input and shift no. and return he encoded string.
I made use of function to get modula approach
I am preferring only lower cases to work with
ord() function which returns the ASCII value of a character.(Learning)
NOTE: my teacher made a list of alphabet but I used ascii codes for both encode and decode, working same way.
Encode and decode opion in while loop and logo.art of cipher

NOTE: Quiet Challenging, But went through completely different approach with respect to my teacher.

**Files**
- [Code File](day-08/Carsar_Cipher.py)
- [Image Of Teminal Output](day-08/Ceaser_Cipher_OUTPUT-SS.png)


## Day 9: March 14, 2026
**What I Learned :**
In Python dictionaries are written with curly brackets, and they have keys and values.
They are similiar to lists but they have keys instead of indexes.
A dictionary can be created by placing a sequence of elements within curly braces {} separated by commas, with a key and a value separated by a colon :.
E.g. key is bug so value is errors that prevents the program from running as expected
{"Bug": "An error in a program that prevents the program from running as expected", ... much more}
the correct ways to define dictionary now to retrieve it..
with key
looping through the dictonary --> Just key
spell the key correctly, with correct data type: string or integer

NESTING : a key can be given value in dictonary as a list or dictinary itself
The structure becomes complex but gives flexibilty to use the dictonary
It is like loop inside another loop, and list inside list
Each key only one value, suppose  moved to cities of uttarakhand so...

**Project Name :** The Secret Auction

**How code work :**
The Program asks for name and bid , storing the data, it ask if there is any other bidder.
On pressing yes the screen clear to keep the bid amount private,
and entry is taken for next bidder name and amount, same thing is asked again
on pressing no, the result like who paid heighest, and what amount (fixed)won in auction
In this program : key learnings, is getting heighest of all number, making use of dictinary, and clearning screen as well as loops

Greetings and collecting data
clearing screen if true
    print("\n"*100)
Calculating the heighest bid and printing name of the bidder won
There are several method for hiest bid but i am using loop
There can be more than two winner with same bid.
NOTE : Sorry, again I could not access and implement art logo
It was not so challenging but the clearning the screen was the key takeaway, adn aslo the getting hiest bid.

**Files**
- [Code File](day-09/The_Secret_Auction.py)
- [Images Folder Of Teminal Output](day-09/OUTPUT_SS)



## Day 10: March 15, 2026
**What I Learned :**
1. Predefined function title(), more on functions.
Function with outputs and return keyword under its definition.Learnt about enumerate() and traverse through string using for loop.
return replaces the fucntion calling to output.
difference between return and print - we can not use output of function which print output only
2. We can have many return in a function, like to give invalid msg and stop fucntion to move ahead
3. All statements after in a fucntion are not executed if return executed
4. Docstrings to mention info and docs like things of the function we defined
5. We can also use docstring """--""" as multiline comment
6. We trigger function by adding parenthesis to it.
but if we want to store a function to a variable like a string or integer.
7. We can do it without parenthese and use the var name as fucntion which will store 
the returned value of fucntion for the given parameter.

**Project Name :** Calculator

**How code work :**
The Calculator is the python program which I have coded on my own as a part
of my 100 days of code by Angela Yu.
Through this I got a thorough idea of functions, and not only defining or calling but also passing arguments and returning and storing its value or passing it to another 
fucntion or printing results

What program do?
1.) The program asks for two value and choice of operations to be performed on the two input values
2.) Then user need to make choice either to continue with same calculation(taking previous result as first input) or with new calculations or exit the program...

**Files**
- [Code File](day-10/Calculator.py)
- [Image Of Teminal Output](day-10/OUTPUT-SS-CALCULATOR.png)


## Day 11: March 16, 2026
**What I Learned :**
1. Predefined function title(), more on functions.
Function with outputs and return keyword under its definition.Learnt about enumerate() and traverse through string using for loop.
return replaces the fucntion calling to output.
difference between return and print - we can not use output of function which print output only
2. We can have many return in a function, like to give invalid msg and stop fucntion to move ahead
3. All statements after in a fucntion are not executed if return executed
4. Docstrings to mention info and docs like things of the function we defined
5. We can also use docstring """--""" as multiline comment
6. We trigger function by adding parenthesis to it.
but if we want to store a function to a variable like a string or integer.
7. We can do it without parenthese and use the var name as fucntion which will store 
the returned value of fucntion for the given parameter.

**Project Name :** The Blackjack Game

**How code work :**
Learnt and used append(), sum() and remove fucntion of lists in python...

**What program do?**
The game is simple yet highly challenging to code. Jack king and queen is counted as 10.
and we have to figure out the sum of the numbers we have, and each time either to choose hit or stand.
We risk by hit to complete 21 near, and on getting a card, on satisfying 
dealer(computer), Chose to hit or stand, and finally sum is checked.
If we exceeds 21 we won else other will have chance to hit on our any random card who so ever sum of card value is more each time, wins.

NOTE: 
Sorry for not able to add complete fucntionality and not coded in readable way
Actually I could not properly understand or able to, implement ace being 2 or 11
And doubted if one has black jack so won in all case how ???

**Files**
- [Code File](day-11/The_Blackjack_Game.py)
- [Image(1) Of Teminal Output](day-11/OUTPUT-SS-(1)-The_Blackjack_Game.png)
- [Image(2) Of Teminal Output](day-11/OUTPUT-SS-(2)-The_Blackjack_Game.png)
- [Image(3) Of Teminal Output](day-11/OUTPUT-SS-(3)-The_Blackjack_Game.png)




## Day 12: March 17, 2026
**What I Learned :**
I have learnt namespaces : Local and Global Variable.
1.) Scope is the concept in programming that defines the part of the program that can access a particular variable or fucntion
2.) Global variable can be accessed by any part of the program.
3.) Variable donot have block scope in python unlike c, c++, java etc !!!
4.) Scope is restricted to functions, inside the fucntion it is lower scope than outside
5.) Global scope is when, variable is defined out of all above fucntion most probably at the top of program and can be accessed by any fucntion in the program.
6.) No block restriction like if-else and for etc.
7.) Within a fucntion a variable is in local scope.
8.)Modifying Global Scope : inside any fucntion we can modify globle scope varible by using global keyword
9.)Not recomended, then change will be at global level, instead use the value and modify version use in return or printing purpose
10.)This won't cause huge change and also we fullfill purpose with value in the global variable.
11.)Many times using global scope is helpful.suppose we donot want to use value of pie as 3.145159 etc everytime
12.) SO, to make it accessible everywhere we can store it in a variable say pi and decalring it in global scope
13.) Not only pi but any url like https://google/com etc

**Project Name :** Number Guessing Game

**What program do?**
Using random.randint(),I generated a random no. between 1 to 100.
User need to guess it, in 5 attepmts, if he chose hard level, or in 10 attempts if he chose easy level.
Then if he hit a guess on right number he is winner else he lost. In both the cases, the random number will be disclosed.
the program works in loop and there is proper focus kept on spacing and handling situation of  wrong inputs.

**Files**
- [Code File](day-12/Number_Guessing_Game.py)
- [Image Of Teminal Output](day-12/OUTPUT-SS-NUMBER_GUESSING_GAME.png)



## Day 13: March 18, 2026
**What I Learned :**
Today there was no project, I just went through lecture videos.
The lecture was amazing and informational. Bug in computer refers to error that avoid desired output from program.
We programmers deal with bug on daily basis.
Firstly we should understand that bug are inevitable. Secondly more we fix the bug more we learn and grow in coding.
Thirdly below are the steps to go in order to fix bug and instead of getting demotivated, we need to take it as oppertunity.

[Click for More Information](day-13/Learnings_of_the_day.txt)  
