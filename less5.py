monday_temperatures = [9.1, 3.5, 7.6]
student_grades = {"Marry":9.1, "Tiki":9.5, "John":8.8}

mysum= sum(student_grades.values())
length = len(student_grades)
mean = mysum / length
print (mean)

#use dictionary to sort from the list all your values or keys
#student_grades.values() > will sort values from you list(num in my case)
#student_grades.keys()  > will sort keys from the list (all names) 