"""
The game is simple yet highly challenging to code.
jack king and queen is counted as 10.
and we have to figure out the sum of the numbers we have, and each time either to choose hit or stand 
we risk by hit to complete 21 near, and on getting a card, on satisfying 
dealer(computer), Chose to hit or stand, and finally sum is checked.
if we exceeds 21 we won else other will have chance to hit on our any random card who so ever sum of card value is more each time, wins.

"""
import random
# GREETINGS 
print("\n\n****************** The Blackjack Game ******************\n")
loop_status=""
loop_status=input("DO YOU WANT TO PLAY THE BLACK JACK :('yes'/'no') \n")
while loop_status!="no":
    status = ""
    user_card ={}
    computer_card={}
    card_values=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    c=0
    user_card=[random.choice(card_values),random.choice(card_values)]
    computer_card=[random.choice(card_values),random.choice(card_values)]
    print("Your cards :  "+str(user_card)+", Current score :  "+str(sum(user_card)))
    print("Computer's first card :  "+str(computer_card[0]))
    status = input("Type 'y' to get another card, type 'n' to pass :  ")
    while status != "n":
        user_card.append(random.choice(card_values))
        print("Your cards :  "+str(user_card)+", Current score :  "+str(sum(user_card)))
        print("Computer's first card :  "+str(computer_card[0]))
        if sum(user_card)>21:
            status="n"
            c=1
        else:
            status = input("Type 'y' to get another card, type 'n' to pass :  ")
    if c==1:
        print("\nYou went over, lost\n-------------------------------------------------")

    else:
        while not sum(computer_card)>=17:
            computer_card.append(random.choice(card_values)) 
        print("\nYour final card(s) :  "+str(user_card)+"\nComputer final card(s) :  "+str(computer_card))   
        if sum(computer_card)>21:
            print("\nYOU WON !!!\n-------------------------------------------------")
        elif sum(computer_card)<=21 and sum(user_card)<=21:
            if sum(user_card)>sum(computer_card):
                print("\nYOU WON !!!\n-------------------------------------------------")
            elif sum(user_card)==sum(computer_card):
                print("\nOOPS, DRAW!!!\n-------------------------------------------------")
            else:
                print("\nCOMPUTER WON !!!\n-------------------------------------------------")
    loop_status=input("DO YOU WANT TO CONTINUE WITH THE BLACK JACK :('yes'/'no') \n")
print("\n----------------------------------------------\nYour Final Cards : "+str(user_card)+f"      and Score : {sum(user_card)}\nComputer Final Cards : "+str(computer_card)+f"      and Score : {sum(computer_card)}\n----------------------------------------------")
print("\n********************* GAME TERMINATED ********************* \n")

# Sorry for not able to add complete fucntionality and not coded in readable way
# Actually I could not properly understand or able to, implement ace being 2 or 11
# And doubted if one has black jack so won in all case how ???
