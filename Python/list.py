#operation on list
marks = [99,93,95]
print(marks)

#score at certain index
print("Element at index :",marks[2])

#iterate using loop
print("Marks list using loop:")
for score in marks:
    print(score)

#append- to add element in last
marks.append(99)
print("The appended marks is:",marks)

#insert - to add at certain element
marks.insert(1,30)
print("List after insert",marks)

#to check whether element exist in list or not
print("Element check:",98 in marks)
print("Element check:",99 in marks)
#length of the list
print("Length of marks:",len(marks))

#clear all
marks.clear()
print("Finally:",marks)