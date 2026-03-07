# 100 Days of Python – Angela Yu Bootcamp

My personal journey through Dr. Angela Yu's **100 Days of Code: The Complete Python Pro Bootcamp** (Udemy).  
Daily Python practice, small projects, notes, and fun experiments! 🐍✨

**Goal:** Code every day for 100 days → build real projects from beginner basics to advanced apps, games, websites & more.  
**Started:** March 6, 2026 
**Tracking:** #100DaysOfCode

## Progress Tracker
- [X] Day 1 – Band Name Generator  
- [ ] Day 2 – Tip Calculator  
- [ ] Day 3 – ...  
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
- [Image Of Teminal Output](day-01/day-01-ss.png)



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

