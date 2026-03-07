# The Tip Calculator is a program that ask user for input of total bill, 
# Percentage of tip wanna give, 
# No of people among which final bill including tip amount split to be paid by each...

print("\n\n----------------> WELCOME TO TIP CALCULATOR <----------------\n\n") #fancy greeting

# gathering required inputs
bill = float(input("Enter the total Bill ?  "))
tip_percentage = float(input("How much % tip want to give ? 0, 10, 12, 15 or 20 : "))
no_of_people = float(input("No. of People splitting the bill :  "))
# calculation
final_bill = bill*(1+(tip_percentage/100))
individual_paying_amount = final_bill/no_of_people
#printing appropriate to 2 decimal places
print("\n\nTotal Bill inlc. Tip :  "+ str(round(final_bill, 2)))
print("Each person will pay :  "+ str(round(individual_paying_amount, 2)))


# Note: I made mistake and learnt that input() always return string
#  final_bill = bill*(1+(tip_percentage/100))
#                           ~~~~~~~~~~~~~~^~~~
# TypeError: unsupported operand type(s) for /: 'str' and 'int'
# and "10"/100 raise error, so....
# SOLUTION : use float(input()), to get number : in bill percent ad no. of people

#----------------------FINISH---------------------#
