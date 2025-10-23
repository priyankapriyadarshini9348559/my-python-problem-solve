class Bank_account:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print(f"{amount} deposit.new balance{self.balance}")
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance -=amount
            print(f"{amount} withdrawn. New balance: {self.balance}")
        else:
            print("Insufficient balance!")
    def display_balance(self):
         print(f"Owner: {self.owner}, Balance: {self.balance}")
account1=Bank_account("priya",10000)
account2=Bank_account("smruti",20000)
account1.deposit(1000)
account2.deposit(2000)
account1.withdraw(500)
account2.withdraw(300)
account1.display_balance()
account2.display_balance()

        
