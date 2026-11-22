balance = 1000000
correct_pin = "1234"
attempts = 3

print("Welcome to ATM Simulator!")

while attempts > 0:

    pin = input("Enter your PIN: ")

    if pin == correct_pin:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Incorrect PIN.")
        print("Attempts remaining:", attempts)

if attempts == 0:
    print("Your account is locked.")
else:

    while True:

        print("\n===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Your balance is:", balance, "Toman")

        elif choice == "2":
            amount = int(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount.")

            elif amount <= balance:
                balance -= amount
                print("Withdrawal successful!")
                print("Remaining balance:", balance, "Toman")

            else:
                print("Insufficient balance!")

        elif choice == "3":
            amount = int(input("Enter deposit amount: "))

            if amount <= 0:
                print("Invalid amount.")

            else:
                balance += amount
                print("Deposit successful!")
                print("New balance:", balance, "Toman")

        elif choice == "4":
            print("Thank you for using ATM Simulator!")
            break

        else:
            print("Invalid option. Please try again.")
