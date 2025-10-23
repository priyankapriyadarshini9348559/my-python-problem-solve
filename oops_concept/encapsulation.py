class BankAccount:
    def __init__(self,name,blance):
        self.name=name
        self.__blance=blance
    def get_balance(self):
        return self.__blance
    def deposit(self,amount):
        if amount > 0:
            self.__blance+=amount
            print(f"{amount} deposited. New balance: {self.__blance}")
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if 0 <amount<=self.__blance:
             self.__blance -= amount
             print(f"{amount} withdrawn. New balance: {self.__blance}")
        else:
            print("Insufficient balance ")

account = BankAccount("Priyanka", 1000)
print(account.name)
print(account.get_balance())
account.deposit(500)   
account.withdraw(200) 
account.withdraw(2400) 