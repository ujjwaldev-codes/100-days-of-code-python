from question_model import *
from question_data import *
# Making list of question object
score =0
question_bank =[Question(question_data[0]["text"],question_data[0]["answer"]),
                Question(question_data[1]["text"],question_data[1]["answer"]),
                Question(question_data[2]["text"],question_data[2]["answer"]),
                Question(question_data[3]["text"],question_data[3]["answer"]),
                Question(question_data[4]["text"],question_data[4]["answer"]),
                Question(question_data[5]["text"],question_data[5]["answer"]),
                Question(question_data[6]["text"],question_data[6]["answer"]),
                Question(question_data[7]["text"],question_data[7]["answer"]),
                Question(question_data[8]["text"],question_data[8]["answer"]),
                Question(question_data[9]["text"],question_data[9]["answer"]),
                Question(question_data[10]["text"],question_data[10]["answer"]),
                Question(question_data[11]["text"],question_data[11]["answer"])]
i = 0# counter
#greetings
print("\n\n================================================== WELCOME TO THE QUIZ CONTEST ==================================================\n\n")
# Proper spacing and keep question flow till last and finally score
for index in question_bank:
    score +=index.result(index.ask(i),i,score)
    i+=1
    # Every wrong answer -1 and right +4
print("\nFinal Score "+str(score)+f"/{len(question_bank)}\n")
print("\n================================================== QUIZ COMPLETED!  ==================================================\n\n")
