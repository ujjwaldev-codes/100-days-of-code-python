final_score=0
wrong = False
celebrities={"Shahrukh Khan":{"profession":"an Actor","followers":49000000,"country":"India"},
             "Virat Kholi":{"profession":"a cricketer","followers":275000000,"country":"India"},
             "Sara Ali Khan":{"profession":"an Actress","followers":46000000,"country":"India"},
             "Amir Khan":{"profession":"an actor","followers":182000,"country":"India"},
             "Salman Khan":{"profession":"an actor","followers":70000000,"country":"India"}}
# This Dictionary Will/Shall be Extended...
# Making a list of keys to keep the flow moving across statement A and B 
i =0
list_of_celebrities_key={}
for key in celebrities:
    list_of_celebrities_key[i]=key
    i=i+1
j=0
print("\n\n========================================== WELCOME TO HIGHER LOWER GAME ==========================================\n")
while wrong==False and j!=(len(list_of_celebrities_key)-1):
    a =f"Compare A : {list_of_celebrities_key[j]}, {celebrities[list_of_celebrities_key[j]]["profession"]} from {celebrities[list_of_celebrities_key[j]]["country"]}.\n"
    b =f"Against B : {list_of_celebrities_key[j+1]}, {celebrities[list_of_celebrities_key[j+1]]["profession"]} from {celebrities[list_of_celebrities_key[j+1]]["country"]}.\n"
    print("\n")
    print(a,b)
    choice = input("Who has more followers ? Type : 'A' or 'B':  ").lower()
    if (choice =="a" and celebrities[list_of_celebrities_key[j+1]]["followers"]<celebrities[list_of_celebrities_key[j]]["followers"]) or (choice =="b" and celebrities[list_of_celebrities_key[j+1]]["followers"]>celebrities[list_of_celebrities_key[j]]["followers"]):
        final_score =final_score+1
    else:
        print(f"\nSorry that is wrong ! Your final score is {final_score}.\n")
        wrong = True
    j=j+1
if(wrong ==False):
    print(f"Your final score is {final_score}.\n")
print("\n\n========================================== GAME OVER !!! ==========================================\n")
