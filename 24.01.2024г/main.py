from BankAccount import BankAccount


if __name__ == "__main__":
      Account1 = BankAccount("Kaloyan","Vlahov",2000)
      Account1.deposit(100)
      Account1.withdraw(200)
      Account1.print_all_transactions()
      print(Account1)