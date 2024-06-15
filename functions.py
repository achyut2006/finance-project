class AmountError(Exception):
    pass


class BankAccount():
    def __init__(self, name, balance):
        self.account_holder = name
        self.account_balance = balance
    
    def retrieveBalance(self):
        return f"\n***************\n**Retrieving Balance**\nAccount Holder: {self.account_holder}\nCurrent Balance: {self.account_balance}\n***************"
    
    def deposit(self, amount):
        prev = self.account_balance
        self.account_balance += amount
        return f"\n***************\n**Updating Balance**\nAccount Holder: {self.account_holder}\nPrevious Balance: {prev}\nAmount Deposit: {amount}\nCurrent Balance: {self.account_balance}\n***************"

    def authenticate(self,amount):
        total = self.account_balance - amount
        if total < 0:
            raise AmountError("Insufficient funds for transaction.")
        else:
            return
        
    def withdraw(self, amount):
        prev = self.account_balance
        try:
            self.authenticate(amount=amount)
            self.account_balance = self.account_balance - amount
            return f"\n***************\n**Updating Balance**\nAccount Holder: {self.account_holder}\nPrevious Balance: {prev}\nAmount Withdrawn: {amount}\nCurrent Balance: {self.account_balance}\n***************"
        except AmountError as e:
            return e

        
    def transfer(self,receiver,amount):
        prev = self.account_balance
        try:
            self.authenticate(amount=amount)
            self.account_balance = self.account_balance - amount
            receiver.deposit(amount)
            return f"\n***************\n**Updating Balance**\nAccount Holder: {self.account_holder}\nPrevious Balance: {prev}\nAmount Transferred: {amount}\nCurrent Balance: {self.account_balance}\n***************"

        except AmountError as e:
            return e



