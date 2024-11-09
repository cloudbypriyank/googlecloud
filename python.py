print("********\n")
account = int(input("Enter Account Number to Get Started : "))
print("Your Account Number is:", account)
pin = int(input("Enter Your Pin:"))

print("*******\n")
print("Services\n", "1) Deposit", "2) Transfer To Bank")

choice = int(input("Enter Your Choice:"))

def deposit():
    amount = int(input("Enter Amount to Deposit into Your Bank: "))
    print("$", amount, "is successfully deposited in your account.")
    
def tf():
    bank = int(inut("Enter Bank Account Number"))

if choice == 1:
    deposit()
else:
    print("No option available.")
