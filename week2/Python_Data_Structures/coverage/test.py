""" tuple """
Data1 = (7, False, "Apple", True, 7, 98.6)

""" Set """
Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"}

""" list """
Data3 = ["A", 7, -1, 3.14, True, 7]

""" Dictionaries """
Data4 = {"name" : "Joe",  "age" : 26,   "active" : True,  "hourly_wage" : 14.75}

print("Task for Data1 questions = Tuple Data")
print("1.Count the number of items in Data1")
print(len(Data1))
print("2.Find the value of the third item stored in the data set in Data1")
print(Data1[3])
print("3.Count the number of times 7 appears in Data1")
print(Data1.count(7))

print("Task for Data2 questions = Set Data")
print("1.Remove a random element from the data set in Data2")
print(Data2)
randomElement = Data2.pop()
print(randomElement, "Was removed from the list")
print("New list after it removed", randomElement)
print(Data2)
print("2.Add Alpha to the data set in Data2")
Data2.add("Alpha")
print("3.Print data set in Data2")
print(Data2)

print("Task for Data3 questions = List Data")
print("1.Print the data set in reverse order in Data3")
Data3.reverse()
print(Data3)
print("Change the second value in the data set to B in Data3")
Data3[1]="B"
print(Data3)
print("Remove the last item and print the data set in Data3")
Data3.pop()
print(Data3)

print("Task for Data4 questions = Dictionaries Data")
print("1.Change active to False")
Data4.update({"active":"False"})
print(Data4)
print("Add address with a value of 123 West Main Street in Data4")
print(Data4.setdefault("address","123 West Main Street"))
print(Data4)
print("Print the weekly salary for Joe if he worked a full 40 hour week in Data4")
hour=40
salary=Data4.get("hourly_wage")
weeklySalary=salary*hour
print(weeklySalary)
print("Print the data set in Data4")
print(Data4)