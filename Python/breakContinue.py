#break
students=["Ram","shyam","Mohan","Radha","sita"]
for student in students:
    if student == "Radha":
       break;
    print(student)

#continue
print(" ")
for student in students:
    if student == "Mohan":
        continue;
    print(student)
