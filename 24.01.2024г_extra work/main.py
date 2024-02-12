from BankAccount import BankAccount
import os

def is_bank_number_unique(accounts, bank_number):
    for account in accounts:
        if account._number_of_bank_account == bank_number:
            return False
    return True

def find_account_by_number(accounts, bank_account_number):
    for account in accounts:
        if account._number_of_bank_account == bank_account_number:
            return account
         
def create_new_account(accounts):
    first_name = input("Enter first name: ")
    second_name = input("Enter last name: ")
    balance = int(input("Enter balance: "))
    new_account = BankAccount(first_name, second_name, balance, accounts)
    accounts.append(new_account)
    print("Account created successfully.")
    print(f"Account number: {new_account._number_of_bank_account}")

def deposit_money(accounts):
    bank_account_number = int(input("Enter bank account number: "))
    existing_account = find_account_by_number(accounts, bank_account_number)
    
    if existing_account:
        amount = int(input("Enter deposit amount: "))
        existing_account.deposit(amount)
    else:
        print("Account not found.")

def withdraw_money(accounts):
    bank_account_number = int(input("Enter bank account number: "))
    existing_account = find_account_by_number(accounts, bank_account_number)
    
    if existing_account:
        amount = int(input("Enter withdrawal amount: "))
        existing_account.withdraw(amount)
    else:
        print("Account not found. Please check the entered details.")

def transfer_money(accounts):
    from_bank_account_number = int(input("Enter source account bank account number: "))
    to_bank_account_number = int(input("Enter destination account bank account number:"))

    from_account = find_account_by_number(accounts, from_bank_account_number)
    to_account = find_account_by_number(accounts, to_bank_account_number)

    if from_account and to_account:
        amount = int(input("Enter transfer amount: "))
        from_account.transfer(to_account, amount, accounts)
    else:
        print("One or both accounts not found. Please check the entered details.")

def print_transactions(accounts):
    bank_account_number = int(input("Enter bank account number: "))
    account = find_account_by_number(accounts, bank_account_number)
    
    if account:
        account.print_all_transactions()
    else:
        print("Account not found. Please check the entered details.")

def print_all_accounts(accounts):
    print("List of all accounts:")
    with open("accounts.txt", "w") as writer:
        i = 0
        for account in accounts:
            i += 1
            print(account.get_account_info())
            writer.write(f"{i}. {account.get_account_info()}\n")

def load_accounts(accounts):
    new_accounts = []
    text_name = input("Enter file name: ")
    with open(text_name, "r") as reader:
            lines = reader.readlines()
             
    for line in lines:
        account_info = line.strip().split(',')
        bank_number = int(account_info[0].split(":")[1].strip())
        owner = account_info[1].split(":")[1].strip()
        first_name, second_name = owner.rsplit(' ', 1)
        balance = int(account_info[2].split(":")[1].strip())
        account = BankAccount(first_name, second_name, balance, accounts)
        account._number_of_bank_account = bank_number 
        new_accounts.append(account)
    accounts.extend(new_accounts)
    print("Accounts loaded successfully.")
   

if __name__ == "__main__":
    accounts = []
    while True:
        os.system("clear" if os.name == "posix" else "cls")
        print("\nMenu:")
        print("1. Create new account")
        print("2. Deposit money in account")
        print("3. Withdraw money from account")
        print("4. Transfer money between accounts")
        print("5. Print all transactions of an account")
        print("6. Print list of all accounts")
        print("7. Load accounts from file")
        print("8. Exit")

        choice = int(input())
        os.system("clear" if os.name == "posix" else "cls")

        if choice == 1:
            create_new_account(accounts)
        elif choice == 2:
            deposit_money(accounts)
        elif choice == 3:
            withdraw_money(accounts)
        elif choice == 4:
            transfer_money(accounts)
        elif choice == 5:
            print_transactions(accounts)
        elif choice == 6:
            print_all_accounts(accounts)
        elif choice == 7:
            load_accounts(accounts)
        elif choice == 8:
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 8.")
        
        input("\nPress Enter to continue...")