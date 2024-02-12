class BankAccount:
    def __init__(self,owner,balance=0):
        self.__owner__= owner
        self.__balance__= balance
    def __str__(self):
        return f"owner of the account {self.__owner__} has currently {self.__balance__}"    
    def deposit(self,amount):
        self.__balance__+=amount
    def withdraw(self, amount):    
        if self.__balance__< amount:
            print("error.there is not enough money")
        else:
            self.__balance__-= amount
if __name__ == "__main__":
    person1 = BankAccount("person1",500)
    print(person1)
    person1.deposit(100)
    print(person1)
    person1.withdraw(300)
    print(person1)
    person1.withdraw(400)
    print(person1)
    person2 = BankAccount("person2")
    print(person2)
    person2.deposit(200)
    print(person2)
    person2.withdraw(100)
    print(person2)
    person2.withdraw(200)
    print(person2)
