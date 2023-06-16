#initialise the variables
count = 0
total = 0

#input a number
num = float(input("please enter a number. if you enter the number -1 it will stop: "))

#the while loop will ensure it keeps asking the user for input, until -1 is entered:
while num!= -1:
    total += num
    count += 1
    num = float(input("enter another number. if you enter the number -1, it will stop: "))

#this will calculate the average, if at least one number is entered:
if count > 0:
    avg = total/count
    print("the average of the numbers entered is: ", avg)

else:
    print("no numbers have been entered")