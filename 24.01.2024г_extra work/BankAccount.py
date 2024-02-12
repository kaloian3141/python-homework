import random

class BankAccount:
    def __init__(self, first_name, second_name, balance, accounts):
        self._first_name = first_name
        self._second_name = second_name
        self._balance = balance
        self._transactions = []
        self._transactions_count = 0
        self._number_of_bank_account = self.generate_unique_bank_number(accounts)
    def __str__(self):
        return f"{self._number_of_bank_account}"
        
    def generate_unique_bank_number(self, accounts):
        while True:
            bank_number = random.randint(1000, 9999)
            is_unique = True
            for account in accounts:
                if account._number_of_bank_account == bank_number:
                    is_unique = False
            if is_unique:
                return bank_number        

    def withdraw(self, amount):
        if self._balance >= amount and amount != 0:
            self._balance -= amount
            self._transactions_count += 1
            self.save_transaction(False, amount)
            return True
        elif self._balance < amount:
            print(f"Error: There is not enough money in account {self._number_of_bank_account}")
            return False

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self._transactions_count += 1
            self.save_transaction(True, amount)

    def save_transaction(self, is_deposit, amount):
        if is_deposit:
            type_of_transaction = "deposit"
        else:
            type_of_transaction = "withdraw"
        current_transaction = f"account:{self._number_of_bank_account}, transaction {self._transactions_count}, type - {type_of_transaction}, amount - {amount}, new balance {self._balance}"
        self._transactions.append(current_transaction)

    def print_all_transactions(self):
        for transaction in self._transactions:
            print(transaction)

    def transfer(self, other, amount, accounts):
        if self.withdraw(amount) and self != other:
            other.deposit(amount)
            print(f"Transfer of {amount} from {self} to {other} successful.")
        elif self == other:
            print("Transfer failed. Source and destination accounts are the same.")
        else:
            print("Transfer failed. Insufficient funds.")

    def get_account_info(self):
        return f"Account Number: {self._number_of_bank_account} , owner: {self._first_name} {self._second_name} , balance: {self._balance}"