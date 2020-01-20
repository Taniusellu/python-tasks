#what output will print?
x = -10
if x * 2 > x:
    print("Greater")
else:
    print("Less or Equal")
#Less or Equal

#What is the ouptup for this task?
def foo(x, array):
    if x in array:
        return True
    else:
        return False
 
print(foo(1, [1, 2, 3]))
print(foo(1, [2, 3]))
print(foo(1, ['1', 2, 3]))

#1 - True False False
#2 - True False True
#3 - False False False 

#N1 - because 1 is actually in the list [1, 2, 3], therefore, the first output is True. 1 is not in [2, 3], so the second
#output is False. 1 is not in ['1', 2, 3], so the third output is also False. Note the third list has '1', but
#not 1. 1 is not the same as '1'. They are of different types.

#one more task

if isinstance(x, int) or insinstance(x, float) or x == '1':
 print("Valid type")
else:
    print("Not valid")
# If any of the conditions in line 1 is met, the code will execute line 2. In other words, if x has
#a value of '1' that means one of the conditions in line 1 was met.