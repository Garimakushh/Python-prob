first = input("Enter the first number:")
operator = input("Enter the operator (+,-,*,/,%) :")
second = input("Enter the second number:")
first = int(first)
second = int(second)
if operator == "+":
    print("sum =",first+second)
elif operator =="-":
    print("Difference =",first-second)
elif operator =="*":
    print("Product =",first*second) 
elif operator =="/":
    print("Division =",first/second)
elif operator =="%":
    print("Remainder =",first%second)
else :
    print("Invalid entry")