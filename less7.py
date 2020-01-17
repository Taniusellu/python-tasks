#Append the value of current to the end of the list seconds. Please use the list.append() method to do that.
seconds = [1.1234566, 1.543356, 1.23567777, 1.8754688]
current = 1.59395524
seconds.append(current)
print(seconds)

#Remove item 1.1234566 from seconds
seconds = [1.1234566, 1.543356, 1.23567777, 1.8754688]
current = 1.1234566
seconds.remove(current)
print(seconds)

#Remove all items from seconds
seconds = [1.1234566, 1.543356, 1.23567777, 1.8754688]
seconds.remove(1.1234566)
seconds.remove(1.543356)
seconds.remove(1.23567777)
seconds.remove(1.8754688)
print(seconds)
