class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
    def ask(self,index):
        choice = (input(f"Q.{index+1}) "+self.text + " (true/flase) ? ")).lower()
        return choice
    def result(self, choice, index, score):
        if choice == (self.answer).lower():
            print(f"You got it Right ! Correct answer is {(self.answer).lower()}")
            score+=1
            print(f"Your current score : {score}/{index+1}\n")
            return 1
        else:
            print(f"Sorry, You are wrong. Correct answer is {(self.answer).lower()}.")
            print(f"Your current score : {score}/{index+1}\n")
            return 0