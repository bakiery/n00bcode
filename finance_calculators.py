#import "math"
import math 
#print the main menu
print("MAIN MENU")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

#user input: they can choose which calculation they want to perform. convert to lowercase.
calculation = input("enter 'investment' or 'bond' to continue: ").lower()

#when the user chooses investment, they can obtain more info about the investment:
if calculation == 'investment':
    deposit = float(input("enter how much money you're depositing: ")) #deposit amount
    interest_rate = float(input("enter your interest rate: ")) #interest rate
    years = int(input("enter the number of years you plan on investing: ")) #investment duration
    interest = input("do you want 'simple' or 'compound' interest? ").lower() #interest type

#calculating investment return, based on type of interest user has chosen:
    if interest == "simple":
        A = deposit * (1 + interest_rate/100 * years) #simple intrerest calculation
        print("your investment would be worth: £" + str(A)) #investment return
    elif interest == "compound":
        A = deposit * math.pow((1 + interest_rate/100, years)) #compound interest calculation
        print("your investment would be worth: £" + str(A)) #investment return
    else:
        print("input is invalid, please try again. please enter 'simple' or 'compound': ") #error message, if interest type selected is not valid

#when the user chooses bond, they can obtain more info about the home loan:
elif calculation == "bond":
    present = float(input("enter the present value of the house: ")) #present value of house
    interest_rate = float(input("what is the interest rate? ")) #interest rate
    months = int(input("how many months do you plan to repay the bond? ")) #repayment duration (months)

#bond repayment amount calculations
    i = (interest_rate/100)/12 #monthly interest rate calculation
    repayment = (i * present)/(1 - math.pow(1+i, -months)) #monthly repayment formula
    print("your bond repayment will be: £" + str(round(repayment, 2))) #repayment amount, rounded to 2dp

#when the user input at the main menu is invalid:
else:
    print("invalid input, please enter 'investment' or 'bond': ")


