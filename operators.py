#add

a=int(input("Enter a:"))
b=int(input("Enter b:"))

operation = input("Do you want to 'add' or 'sub' or 'div' or 'mult' ? ").strip().lower()

# Performing the chosen operation
if operation == 'add':
    result = a + b
    print(f"The result of addition is: {result}")
elif operation == 'sub':
    result = a - b
    print(f"The result of subtraction is: {result}")
elif operation == 'div':
    result = a / b
    print(f"The result of division is: {result}")
elif operation == 'mult':
    result = a * b
    print(f"The result of multiplcation is: {result}")

else:
    print("Invalid operation. Please enter 'add' or 'sub' or 'div' or 'mult'.")
