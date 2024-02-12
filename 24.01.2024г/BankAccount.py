class BankAccount:
    def __init__(self,first_name,second_name,balance):
        self.__first_name__ = first_name
        self.__second_name__ = second_name
        self.__balance__=balance 
        self._transactions = []
        self._transactions_count = 0

    def __str__(self):
        return f"{self.__first_name__} {self.__second_name__} has currently {self.__balance__} in his bank account"    
    def withdraw(self, amount):    
        if self.__balance__>= amount and amount!=0:
            self.__balance__-= amount
            self._transactions_count +=1
            self.save_transaction(False, amount)
        elif self.__balance__< amount:
            print(f"error:there is not enough money in {self.__first_name__} {self.__second_name__}'s account")
    def deposit(self, amount): 
        if amount > 0:
            self.__balance__ += amount       
            self._transactions_count +=1
            self.save_transaction(True, amount)

    def save_transaction(self, is_deposit, amount):
        if is_deposit:
            type_of_transaction = "deposit"
        else:
            type_of_transaction = "withdraw"
        current_transaction = f"transaction {self._transactions_count}, type - {type_of_transaction}, amount - {amount}, new balance {self.__balance__}"
        self._transactions.append(current_transaction)
    def print_all_transactions(self):
        for transaction in self._transactions:
            print(transaction)