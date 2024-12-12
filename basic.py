
print("Basic Calculator")
print("For addition press 1\nFor subtraction press 2\nFor division press 3\nFor multiplication press 4")

choice = int(input("Enter your choice here: "))

if choice == 1:
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    print("The result of addition (a + b):", a + b)

elif choice == 2:
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    print("The result of subtraction (a - b):", a - b)

elif choice == 3:
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    if b != 0:
        print("The result of division (a / b):", a / b)
    else:
        print("Error: Division by zero is not allowed!")

elif choice == 4:
    a = int(input("Enter number a: "))
    b = int(input("Enter number b: "))
    print("The result of multiplication (a * b):", a * b)

else:
    print("Invalid choice! Please select a valid option.")
