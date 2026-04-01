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
- [X] Day 14 - Higher Lower Game
- [X] Day 15 - The Coffee Machine
- [X] Day 16 - The Coffee Machine(OOP Based)
- [X] Day 17 - The Quiz Project
- [X] Day 18 - The Hirst Painting
- [X] Day 19 - The Turtle Racing
- [X] Day 20 - The Snake Game(Part I)
- [X] Day 21 - The Snake Game(Part II - Final)
- [X] Day 22 - The Pong Game
- [X] Day 23 - The Turtle Crossing Game
- [X] Day 24 - The Mail Merger
- [X] Day 25 - The States Of America Quiz
- [X] Day 26 - The NATO Phonetic Alphabet
- [X] Day 27 - Miles to Km Converter (GUI Based Application)
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



## Day 14: March 19, 2026
**What I Learned :**
Today, was not anything new but a simple recap of dictionary and list, also conditional statements like if-else and loops.

**Project Name :** Higher Lower Game

**What program do?**
This is one of the most interesting game I coded in python under 100-days of code python bootcamp of Angela Yu. In this game Player is asked to compare the number of followers the famous celebrities have in instagram. Unfortunatly I could not manage to get the art logo to make to program look fancy but I somehow followed the logic below or step:
1.) I Prepared dictionary of celebrities containing their names as key and the dictionary itself containing profession followers and country they belong to key and feeded their values.
2.) Then I used list and dictionary traversing using loop to keep asking and switching the person from a to b as we move on , in each choice correct score increments by 1, and for wrong the traversing stops and we get wrong answer message with final score.
3.) It is compulsory to fill more entries of celebrities in the dictionary celebrities.
4.) I used name profession and country to introduce them and no of followers to check the choice made of more famous is right or wrong.

**Files**
- [Code File](day-14/Higher_Lower_Game.py)
- [Image Of Teminal Output](day-14/OUTPUT-HIGHER_LOWER_GAME-SS.png)




## Day 15: March 20, 2026
**What I Learned :**
It was challenging project which made me to recall dictionary and loops as well as defining and calling fucntions.

**Project Name :** The Coffee Machine

**What program do?**
Coffee Machine Program Requirements
1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “ off ” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “ Sorry there is not enough water. ”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “ Sorry that's not enough money. Money refunded. ”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.

**Files**
- [Code File](day-15/The_Coffee_Machine.py)
- [Image Of Teminal Output](day-15/OUTPUT-SS-THE_COFFE_MACHINE.png)




## Day 16: March 21, 2026
**What I Learned :**
Procedural programming we set functions, we write set of instructions and but  we can get confused with when it comes to write complex program say self driving car, we need a modules and a seperate team to take charge of the data and functionality of modules of that program. to solve the major project.
Here comes OOP, we make objects having data and characteristics , and perfom their duty and contribute in the project.'
these objects are like, waiter receptionist, cook etc, of the restuarnt.
The programer or the main merger can be manager, who dicatcte but donot worry of how objects do.

CLASSES and OBJECTS:(Connect program with real world)
attributes(variables but not free floating but attached to a object and methods(functions),but defines functionality to particular object again attached to a particular object not floating anywhere in the program.

We have object we can even have many waiters with different name having different attributes or what they have, but function same, they are defined by a blueprint called class.
class is just a blueprint, which defines the object, but object can be many defined from same blueprint, ofcourse we can not have pens from blue print of pencils. Object are real which we use
car = carBlueprint() --> object = class() -> (activated function constructor)

Made design with turtle graphics
Function tied with object we called methods
we can use vaious modules from packaages and libraies that, the people have created, by creating the object adn usin gattributes and methods defined for them in documention


developed and shared by python community, pypi

**Project Name :** The Coffee Machine(OOP Based)

**What program do?**
Coffee Machine Program Requirements
1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
a. Check the user’s input to decide what to do next.
b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “ off ” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “ Sorry there is not enough water. ”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “ Sorry that's not enough money. Money refunded. ”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.

**Files**
- [Code File](day-16/The_Coffee_Machine(OOP-Based).py)
- [Image Of Teminal Output](day-16/TERMINAL-OUTPUT-The_Coffee_Machine(OOP-Based).png)




## Day 17: March 22, 2026
**What I Learned :**
Using oop, I made quiz project
I learnt to make custom class, and work with it using object
Made use of class keyword and pass, to avoid indent error

PascalCase - for class name
cameCase - not much used in python
snake_case - rest all python code other than class 


**Project Name :** The Quiz Project

**What program do?**
1.) Greetings
2.) Proper spacing and keep question flow till last and finally score
3.) Making list of question object
4.) Using concept of loops dictionary and oops classes and object, tried to make program simple and efficient, and less error prone.


**Files**
- [Code File](day-17/The_Quiz_Project.py)
- [Image Of Teminal Output](day-17/TERMINAL-OUTPUT-SS-The_Quiz_Project.png)




## Day 18: March 23, 2026
**What I Learned :**
I learnt various random things in turtle package's Screen and Turtle class. Creating their object to access their methods and attributes. Some of the methods : penup(), pendown(), setpos(), xcor(), ycor(), teleport(), exitonclick() --> of Screen class, setheading(), dot(), circle(), color, etc 

Went through [documentation link :](https://docs.python.org/3/library/turtle.html)
Before making final hirst painting project I drew various shapes and design. [Link to that directory](day-18/Extra-OUTPUT-DESIGN-SS)

Also glad to mention few more learnings like :)
If we use only import or from import 
import Turtle
timmy = turtle.Turtle()
-->but if
from turtle import Turtle
timmy = Turtle()

or everything
from turtle import *

It is avoided, to use third to avoid confuse of origin,
also if making very less object try to just import to exclysively tell, the reader or other programmer about, claasses and package you are using module of.

ALIAS NAME
import turtle as t
timmy = t.Turtle()
--> it is just like using t as turtle name recomednded only if module name is large

Not all modules can be imported as before, like heroes(it will be error that nomodules ),
it does not come as pacakges predownloaded, we need to install the packages.

Learnt tuples(list which remain constant in its content and size)
Also got exposure of RGB color system, and Hexa decimal code form.


**Project Name :** The Hirst Painting

**What program do?**
1.) The program first extract 30 shades of color from a random downloaded hirst painitng
2.) Then using color and size and loops logic also the movement and pso(), of turtle class.
3.) The program somehow manage to end up with random dot like painting in hirsat pattern.
4.) Finally to improve visibility in (main project) Hirst painting, I used hideturtle().

**Files**
- [Code File](day-18/Hirst_Painting.py)
- [Image Of Teminal Output](day-18/OUTPUT-SS-Hirst_Painting.png)




## Day 19: March 24, 2026
**What I Learned :**
Today I learnt about more on Turtle Graphics, Event Listeners, State and Multiple Instances.
I made drawing game which cn be controlled by keyboard, random turtle rancing game, as the final project.
We use event listeners provided by turtle modules Screen class, they generally take function as one of the parameter,
and call if something pressed or clicked depending on their behaviour or functionality.
When we pass a function as input to another fucntion, we donot use parenthesis so the fucntion may not be called on its own.
THE CONCEPT - Higher order fucntion, function that can work with other fucntions. But not all languages supports this.

used onkey(), difference between clear() of Screen class and of Turtle class etc

For coding for The Turtle Racing I made many turtles called object just like rahul rishabh are the objects of human class.
these turtle objects(seperate instances) say timmy tommy, may have to be different in their methods or operation or even attributes at a same time, even though they belong to same class
their attributes like color are defined, but may have different values like color, one is yllow or one is red

**Project Name :** The Turtle Racing

**What program do?**
1.) Understanding the coordinate system in Turtle.
Learnt the teaching from my instructor : Expand the solutions and combine and reproduce new possibilities and make it better expand donot be limited and satisfied by solution codes.
2.) Used setup(), goto(),pos(),loops logic, coordinate system of turtgle graphics, use of color and shape attribute, concept of class and object, penup().
3.) Before setup of the window of racing playground, user choice of guesss of the turtle color gonna win is asked using textinput() of Screen class, which later on checks if the turtle win has same color attribute as of user choice, if so user won, else lose.
4.) The turtle is considered to be won if it cross the or reach at x = 225, at earliest, random.choice() is used to choose turtle randomly to move, random paces.


**Files**
- [Code File](day-19/Turtle_Racing.py)
- [Image Directory Of Teminal Output](day-19/OUTPUT-SS-TurtleRacing)




## Day 20 & 21: March 25, 2026 & March 26, 2026
**What I Learned :**
Refreshed concepts of OOPS --> Classes and Objects.
Also revised loops, and constants, lists, tracer(), coordinate system listen() and onkey() of Screen class etc
Learnt Slicing and Inheritance concept, and in turtle graphics I learnt  about setting up screens,setup() and update() of Screen class ,sleep function of Time class, distance() of turtle class
Learning by doing i.e. making snake game, which requires, all these features.
IMP TPOICS THE DAY :
1.) Inheritance : Very useful principle or feature of OOP programming :
                 Suppose there is a chef class and checf knows how to cook, bake, boil, stir, measure, 
                 peel,etc. and we also want a PastryChef class to get its object making pastery. Inheritance helps us to use to functions of another class, within another class, 
                 like here we can inherit some properties of Chef in PastryChef, instead of making it from scratch.
                 So, the functions we generally inherit, may be like bake, stir and measure
                 and ofcourse, we need to make manymore not limited to inherit !
                 We can inherit not only behaviour but also attributes, vice versa.
                 # Example/procedure:(super/parent class --> Animal && subclass/child class --> Fish)
                 class Fish(Animal):
                        def __init__(self):
                            super().__init__()
                      
2.) Slicing lists, tuples etc in pyhton:
                suppose we have list of pianos keys, and we want to get a small sections of list say only c, d and e of the list, 
                say piano is the list, piano_keys[2:5]
EXAMPLE :

piano=["a","b","c","d","e","f"]
print(piano[2:5]) c d e
print(piano[:5]) up to 5 frm beginning
print(piano[::2]) every second item from beginning
print(piano[2:5:2]) every second item fromc, d,e --> c, e
print(piano[::-1]) print reverse 
Same with tuple

**Project Name :** The Snake Game

**What program do?**
In this project I have got oppertunity to make/code for Snake Game though simple, yet the world's most famous and legendary childhood game of many.
I was supposed to complete this in two days.
Features or working of the program :
1.) Body and ground of snake
2.) Detection logic for touching a wall or its own body to lose, or randomly appearing fruit/food
to increase its body size and scre.
4.) It shall be controlled by arrows and conitnuously move as set its heading.
5.) More the score, winner is the player.(Higher scores need better control since body size grows and result in quicker end of game by eating its own body).

NOTE : Delay after each segment move
        for seg in segments:
        seg.forward(20)
        but we want to turn the snake say left right, so head first take turn then other body part
        in this loop we gonna loop through the last segment to first segment in reverse order
        start is from where we start stop is where loop gonna end, and step is, how we gonna move from start to stop
        1 2 3 , start is 1 stop is 3 and step is 1; 4,3,2 is start is 4 stop is 2 and step is -1
        in this case we want to go from 3 2 1 0, so start is 3 and stop is 0 and step is -1
        but this is error to write start stop step, but good for understanding
        range comes from c there is no aruments postional
        for seg_num in range(start=len(segments)-1,0,step=-1):
        We use classes for snake and food and scoreboard(seperate files managing one thing, )
        all following the head
detection its own tail.
Detect collision with food
        Managed to show and update score on scoreboard using turtle only 
        detection of collison with walls 
        size increase and score increase
We avoid having game over in the beginning due to checking distance of snake's head from its head(first body segments) to be less than 10
        for index in range(1,len(snake.segments)-1):
                if snake.segments[0].distance(snake.segments[index])<15:
                        score.update_score(0)
                        game_is_on=False    
        used slicing to make it better work with less code

**Files**
- [Image and Codes Directory](day-20&21/snake-game)





## Day 22: March 27, 2026
**What I Learned :**
I learnt about advance Feature or use of Turtle graphics, and refreshed almost all topics gone through till now in the course.
Logic of moving after collision and calucaltion of touching walls and paddle was challenging as well as fun.

**Project Name :** The Pong Game 

**What program do?**
Pong is legendary arcade game, and Today I ceated it in python from nothing new much, but what all I learnt up till today.
BREAKDOWN OF PROGRAM(PROBLEM):
--> Code enough in main program : screen setup, 
--> May better fit in seperate class : scoreboard, ball, pongs.
Went through the following logical steps, to acheieve screen adn functioning of pong game.
1.) Moving and bouncing logic, bounce only when touch up and down, sidesways only if touched paddle else it will be miss.
2.) Also increase the speed every time paddles hit the ball
3.) Condition of win and lose and score board update.(if opponent miss ball to hit back, other get +1 point)



**Files**
- [Code Files Directory ](day-22/pong_game)
- [Image Directory Of Output(Game)](day-22/OUTPUT_IMAGES-SS)




## Day 23: March 28, 2026
**What I Learned :**
Today I did not learn any specific topic, but revised old concepts and, practised logic by myself, except msking car to move, continuously, in the program , I managed to do everything else by myself.

**Project Name :** The Turtle Crossing Game

**What program do?**
1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.

2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.
3. When the turtle hits the top edge of the screen, it moves back to the original position and the player levels up. On the next level, the car speed increases.

4. When the turtle collides with a car, it's game over and everything stops.


**Files**
- [Code Files Directory](day-23/turtle_crossing)
- [Image Directory Of Output(Game)](day-23/IMAGES-OUTPUT-SS)






## Day 24: March 29, 2026
**What I Learned :**
Today I went through the most interesting and useful topics. They were related to file input and output adn file handling, which includes : 

1.) Reading files using python.
2.) Open method to open the file in that directory, and mode to open with.
3.) I also learnt about managing local files and directories.
also made snake game better by implmenting feature of high score pannel, using the lesson 's learnt today.
4.) After keeping a high_score panel, I also open read and write a file in python, so unlike varibale file store the data permanently.
5.) To retrieve and store to refer to highest score evry time game starts.
6.) Try to unload burden by closing files, just like closing chrome unecessary tabs 
file.close(), to free up resources,
7.) Now we have contents of file in var contents with no mode, it is readble only
8.) Suppose you have to send a invitation letter to say 100 people, so this is sth very help to use python and except most part some part like dear <name>, must be 
different for 100 people.
9.) This can be example of python automation.

10.) Paths system :
===================================================================================================
In compiuter there are files and folders, and files can be stored in folder, but not vice versa.

example structure of the directories 

/(root)
    work
        doc.txt
        project
            main.p
            supportive
        assessts
        readme.md
    personal
        images

NOTE : root is generally c drive in windows.
absolute file path(relative to root) for main is /work/project/main.py
relative path, is relative to some directories, generally we are in and the location of desired files or folder
but what if we are in project folder ofcourse root path is same, but relative path in that case will be:
./main.py (since we are in current directory or working directory )
suppose we want to go to main.py from work
./project/main.py
suppose we are in project directory, and want to visit doc.txt
../doc.txt
../ --> get a step back, upward in directory from current directory
===================================================================================================
11.) Links used for refernce :
( strip(), read(), write(), readlines(), open, with open as so on...)
i.) [LINK-1](https://www.w3schools.com/python/ref_file_readlines.asp)
ii.) [LINK-1](https://www.w3schools.com/python/ref_string_replace.asp)
iii.) [LINK-1](https://www.w3schools.com/python/ref_string_strip.asp)

**Project Name :** The Mail Merger

**What program do?**
Mail-Merger to avoid writing mails new for each or to use file handling or automation to also avoid copy paste. The Program produces bunch of letters in the targeted directory from scratch. It takes Body of Letter and list of names as input and give bunch of letters each having names provided, with relatable names as txt files. 


**Files**
- [Code File](day-24/main_merger.py)
- [Input](day-24/Input)
- [Output](day-24/bunch_of_letters)





## Day 25: March 30, 2026
**What I Learned :**
1.) Today I learnt about working with CSV files which are unlike normal txt files, are data files, and then analysing data with with pandas library, which is the most important, library for data analysis.
2.) CSV is a way to represent data generally in tabular form.(Comma Seperated Value)
3.) more on pandas library, data is dataframe object of pandas
4.) Type of data["temp <or> "condition" <or> "day"] --> is pandas' Series object
5.) Series is euivalent to list, single column of table
6.) dataframe is equivalent to whole table here
7.) series and data frame are two imp data structures or concept in pandas library
8.) Used methods of Pandas object i.e. dataframe, like to_dict(), to_list(), max(), etc mor on documnetation below :
9.) [Pandas Documnetation](https://pandas.pydata.org/docs/)
10.) After a lot of struggle in making the quiz type state of america game, I learnt many overlapping adn interconnecting concepts.
11.) Using Screen 's class mainloop method instead of exitonclick(), is preffered in this program.

**Project Name :** The States Of America Quiz

**What program do?**
This is a game, in which we type names of states of america, and if right spell, we get score out of 50 on the top of prompt screen. 
We can have it with timer with our friends. 
Great thing is that, no points for keep answering same state, as well as no changes. 
Moreover, If correct the name appears on the image where actually the state lies on map of USA.
It is fun to play but challenging to code the logic.

**Files**
- [Code Files Directory](day-25/States_Of_America_Quiz)
- [Image Of Output(Quiz)](day-25/OutPut-SS-Demostration-of-Quiz.png)






## Day 26: March 31, 2026
**What I Learned :**
Using list comprehension, I made it get NATO style naming of words. like a for alfa, and so on ...
This concept is unique in python and makes or cut the down amount of typing. makes the code a lot shorter and easier to read.
Creating a list using new list.

APLLICATION : list is [1,2,3]
now we want a new list that contain, list of numbers one added to this list say 2, 3, 4
so conventionally we will use for loop to go through each element and store as below in new list:
num_list=[1,2,3]
new_list=[]
for num in num_list:
    new_list.appen(num+1)

LIST COMPREHENSION:
new_list = [new_item for item in list]
here patter now,
new_list = [(item+1) for item in num_list]
item+1 is the each item of new list, for each item of num_list

also:
new_list=[operations with num for num in range(a,b)]

also:
new_list=[new_item for item in list if test]
e.g.
name=["alibaba","momo","naag","mota"]
short_names= [name for name in names if len(name)<5]
or advance version
short_names= [name.lower() for name in names if len(name)<5]
Dictionary Comprehensions
new_dict ={new_key:new_value for (key,value) in dict.items if test}

Also used : Using split() method
The split() method is the most straightforward and commonly used method to split a sentence into words. It splits the sentence based on spaces by default.

Iterate comprehension through panda dataframe
dataframe comprehension or looping is same as looping through python dictionary
iterrows() --> method used for above purpose


**Project Name :** The NATO Phonetic Alphabet

**What program do?**
I used all the topics of the todays and previous days' learnings specially comprehension of list and dictionary and pandas library use, to make this wonderful and nteresting project.

** GENERAL INFORMATION :
What is the NATO Phonetic Alphabet?
The NATO Phonetic Alphabet (also called the International Radiotelephony Spelling Alphabet or ICAO Phonetic Alphabet) is a standardized system that assigns a unique code word to each letter of the English alphabet.
It is used to spell out words, names, codes, or callsigns clearly over radio, telephone, or noisy communication channels where normal speech might be misunderstood.

Numbers also have standard pronunciations (e.g., Three is said as "Tree", Five as "Fife", Nine as "Niner") to avoid confusion.
Why was it created? (The "Why")
In radio communication (military, aviation, maritime, emergency services), letters like B, C, D, E, G, P, T, V sound very similar, especially with static, accents, poor signal, or background noise.

"B" can sound like "D" or "P"
"M" can sound like "N"
"S" and "F" are easily mixed up

Example:

Saying "My call sign is BD-137" over radio → easily misheard as "PD-137" or "BT-137"
Using phonetic: "Bravo Delta one three seven" → much clearer

It was developed to eliminate ambiguity and save lives in critical situations.
How and When it was developed (The "How")

During World War II, different countries and branches of the military used their own phonetic alphabets (e.g., Royal Air Force used "Able Baker Charlie", US Army used another).
This caused confusion when allies tried to communicate with each other.
In 1956, NATO (North Atlantic Treaty Organization) adopted a single, universal version after years of testing.
It was designed by linguists and communications experts to work well across many languages and accents.
The words were chosen because they are:
Easy to pronounce for most non-native English speakers
Distinct from each other even in bad conditions
Not easily confused with other common words


It is now the global standard used by:

All military forces in NATO and many others
Civil aviation (pilots and air traffic control)
Maritime (ships at sea)
Police, firefighters, ambulance services
International organizations

Quick Examples of Use

Spelling a name: "My name is Rahul" → "Romeo Alpha Hotel Uniform Lima"


**Files**
- [Code Files Directory](day-26/NATO_Phonetic_Alphabet/main.py)
- [Image(OUTPUT) Directory](day-26/OUTPUT-SS)






## Day 27: April 01, 2026
**What I Learned :**
Today I dive into GUI using inbuilt tkinter module and also learnt about function arguments.
This is much more in-depth than Turtle Graphics.
Features or learning of the day: 
1.) Creating lables and buttons, text input and program design adn layout, responding to button.
2.) Also going advance in python function, default arguments and *args and **Kwargs.
3.) Using all this I code a mile to km converter(GUI based). 

INTRO :
History of GUI ----> previously in order to intereact computer we need to writing command. Later GUI were graphical, point and click. Mac lisa first to allow gui, for user.
Controversy led Windows to court. That's enough, so GUI is IMP.

links --> https://docs.python.org/3/library/tkinter.html#the-packer
tkinter is inbuilt and installed with python, already.

How we can define unlimited positional arguments, unlimited keyword arguments in the function.
used basic tkinter methods, like Label(), pack(), write(), minsize(), title(), mainloop(), 

using advanced arguments to expand range of inputs arguments.
arguments with default values

type(args) --> <class 'tuple'>
kwargs is a dictionary, with key as keyword of argument and value the argument's value


*** pack, place and grid : layout method from tkinter module
1.) pack ==> pack is by default top, but using side parameter we can chnge it to let right bottom also 
So many layout manager since not one can do all layout works.
2.) Place ==>  is abnout precise postion
3.) grid ==> rows --> horizontal
 and columns --> vertical 

 NOTE : Suppose we have many widgets, so precise corner of widgets is nightmare.
 So grid is conept of cell, generally for many widgets case.
 Grid is relative

 NOTE : We can not mix pack and grid together, often grid is chosen

Tk doc --> https://www.tcl-lang.org/man/tcl8.6/TkCmd/entry.htm
More on bringing other components of GUI Tkinter into screen other than label
Anything appearing on screen should have some sort of layout so we use pack for each component

More on tkinter widgets:
1.) labels
2.) buttons
3.) Entry(textbox)
4.) Text Entry(multiline input)
5.) Scale to move along
6.) checkbox
7.) Radiobuttons
8.) Listbox
9.) Spinbox
Finally ! Learnt the ways to organise widgets on screen or say laying out.
easiest way to change padding(spaces around) of each widget is <Tk'Object>.config(padx=20, pady=20)

**Project Name :** Miles to Km Converter (GUI Based Application)

**What program do?**
This is mile to kilomter converter GUI Application.
Logic was simple, 1 mile has 1.5 km.
But components and packing them on screen and taking input to and
maintaing functionality of the program
How Program Works : User need to type the miles in the input bar and,
answer will be, the converted value in kilometer, ofcourse we prefer floats instead integers.


**Files**
- [Code Files Directory]()
- [Image Of Output(Quiz)]()
