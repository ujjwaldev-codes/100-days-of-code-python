# The Program asks for name and bid , storing the data, it ask if there is any other bidder.
# On pressing yes the screen clear to keep the bid amount private,
# and entry is taken for next bidder name and amount, same thing is asked again
# on pressing no, the result like who paid heighest, and what amount (fixed)won in auction
# In this program : key learnings, is getting heighest of all number, making use of dictinary, and clearning screen as well as loops

# Greetings and collecting data
print("\n\n********************* WELCOME TO SECRET AUCTION PROGRAM *********************\n")
any_bidder_left = True
name_list_of_bidders ={}
while any_bidder_left:
    name =input("What's your name ?  ")
    amount=int(input("What's your bid($) ?  "))
    if amount<0:
        print("Invalid sum, not record")
    else:
        name_list_of_bidders[name]=amount
    next_bidder =input("\nAre there any other bidder(s) left ? ('y' for yes/'n' for no)  ").lower()
    if next_bidder =="n":
        any_bidder_left = False
    #clearing screen if true
    print("\n"*100)
# Calculating the heighest bid and printing name of the bidder won
# There are several method for hiest bid but i am using loop
winner=[]
#There can be more than two winner with dsame bid
heighest_bid=0
for name in name_list_of_bidders:
    if name_list_of_bidders[name]>heighest_bid:
        winner=[]
        winner.append(name)
        heighest_bid=name_list_of_bidders[name]
    elif name_list_of_bidders[name]==heighest_bid:
        winner.append(name)
for index in range(len(winner)):
    print("\nThe Winner is "+winner[index]+" with a bid of $"+str(name_list_of_bidders[winner[index]]))
#Sorry, again I could not access and implement art logo
#It was not so challenging but the clearning the screen was the key takeaway, adn aslo the getting hiest bid.
