class BankAccount:
    def __init__(self,name,balance):
        self.name=name #public
        self.__balance=balance #private
        self.__transaction=[] #private
    def get_balance(self):
        return self.__balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.__transaction.append(f"Deposited: {amount}")
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount") 
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction.append(f"Withdrawn: {amount}")
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Insufficient balance or invalid amount")
            
    def show_transactions(self):
        print(f"Transaction history for {self.name}:")
        for t in self.__transaction:
            print(t) 
account= BankAccount("Priyanka", 1000)
print(account.name)
account.deposit(500)     
account.withdraw(200)    
account.withdraw(2000)
print("Current balance:", account.get_balance())
account.show_transactions()

