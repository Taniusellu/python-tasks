#how to check for one single condition
x = 1 
if x == 1:
    print("YES")
else:
    print("No")

#you can also check if two conditions are met at the same time using an and operator:
#That will return YES since x == 1 and y == 1 are both TRUE

x = 1
y = 1

if x == 1 and y == 1:
    print("YES")
else:
    print("No")

#You can also check if on of two conditions are met using an or operator:
#That will return YES since at least one of the condition is TRUE. In this case x == 1 is True
x = 1
y = 1

if x == 1 or y == 2:
    print("Yes")
else:
    print("No")



