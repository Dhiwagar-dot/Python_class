a = int(input("Enter the 'a' value: "))
b = int(input("ENter the 'b' value: "))
# print(type(a))
option = input("Enter the operation you want to perform: 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: ")
if option == '1':
    print("The result of addition is:", a + b)
elif option == '2':
    if a > b:
        print("The result of subtraction is:", a-b)
    elif b > a:
        print("The result of subtraction is:", b-a)
    else:
        print("The result of subtraction is:", a-b)                                      
elif option == '3':
    print("The result of multiplication is:", a * b)
elif option == '4':
    print("The result of division is:", a / b)
else:
    print("Invalid option selected")

