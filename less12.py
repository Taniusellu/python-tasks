#If the number is positive, we print an appropriate massage

num = -2
if num > 0:
    print(num, "is a negative number")
    print("This is always printed")

num = 5
if num > 0:
    print(num, "is a positive  number")
    print("this is always printed")

    #PRogram checks if the number is positive or negative
    #And displays an appropriate message

    num = -2
    if num >= 0:
        print("Positive or Zero")
    else:      #it means (in other case )
        print("Negative number")

    #In this program, I check if the number is positive or negative or zero and display an appropiate message

    num = 3.4
    if num > 0:
        print("Print number is positive")
    elif num == 0:   #The elif is short for else if. It allows us to check for multiple expressions.
        #If all the conditions are False, body of else is executed.
        #The if block can have only one else block. But it can have multiple elif blocks.
        print("Zero")
    else:
        print("Negative number")
    #When variable num is positive, Positive number is printed
    #If num equal to 0, Zero is printed
    #If num is negative, Negative number is printed