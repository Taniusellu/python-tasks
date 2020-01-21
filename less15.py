
def absolute_value(num):
	"""This function returns the absolute
	value of the entered number"""

	if num >= 0:
		return num
	else:
		return -num

print(absolute_value(-4))

print(absolute_value(6))



#write a conditional block:
message = "hello there"
if "hello" in message:
    print("hi")
else:
    print("I do not understand")

#Write a conditional block of multiple conditions:

message = "hello there"
 
if "hello" in message:
    print("hello")
elif "hi" in message:
    print("hello")
elif "hey" in message:
    print("hello")
else:
    print("I don't understand")

#Use the and operator to check if both conditions are True at the same time:

x = 1
y = 1
 
if x == 1 and y==1:
    print("Yes")
else:
    print("No")
#Output is YES since both x and y are 1

#Use the or operator to check if at least one condition is True:

x = 1
y = 2
 
if x == 1 or y==2:
    print("Yes")
else:
    print("No")
#Output is YES since x is 1

#Check if a value is of a certain type with:

isinstance("abc", str)
isinstance([1, 2, 3], list)