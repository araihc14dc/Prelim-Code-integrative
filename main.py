import time

accounts = {}

def register():
    
    account_number = input("Enter account number: ")
    if account_number in accounts: 
        return
    pin = input("Enter PIN: ")
    if len(pin) != 4 or not pin.isdigit():
        print("---- Register ----")
        print("Account already exists. Please try again.")
        print("Invalid PIN. Please try again.")
        
        return
    accounts[account_number] = {'pin': pin, 'balance': 0}
    print("Account successfully registered.\n")

def login():
    
    account_number = input("Enter account number: ")
    if account_number not in accounts:
        
        return None
    pin = input("Enter PIN: ")
    if accounts[account_number]['pin'] != pin:
        print("---- Login ----")
        print("Account not found. Please try again.")
        print("Incorrect PIN. Please try again.")
        return None
    print("Login successful.\n")
    return account_number

def check_balance(account_number):
    print(f"Your current balance is ₱{accounts[account_number]['balance']}\n")

def deposit(account_number):
    try:
        amount = float(input("Enter amount to deposit:"))
        if amount <= 0:
            print("Invalid amount. Please try again.")
            return
        accounts[account_number]['balance'] += amount
        print(f"₱{amount} deposited successfully.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def withdraw(account_number):
    try:
        amount = float(input("Enter amount to withdraw:"))
        if amount <= 0:
            print("Invalid amount. Please try again.")
            return
        if accounts[account_number]['balance'] < amount:
            print("Insufficient balance.\n")
            return
        accounts[account_number]['balance'] -= amount
        print(f"₱{amount} withdrawn successfully.\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")

def menu(account_number):
    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Logout")
        choice = input("Enter choice: ")

        if choice == '1':
            check_balance(account_number)
        elif choice == '2':
            deposit(account_number)
        elif choice == '3':
            withdraw(account_number)
        elif choice == '4':
            print("Logged out\n")
            break
        else:
            print("Invalid choice. Please try again.\n")

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            register()
        elif choice == '2':
            account_number = login()
            if account_number:
                menu(account_number)
        elif choice == '3':
            print("Thank you. Goodbye!")
            time.sleep(1)
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
