# Bank Account Class
# Create a BankAccount class with attributes owner and balance.
#implement methods deposit(amount), withdraw(amount) (with validation for insufficient funds), and a string
# representation

class BankAccount:
    def __init__(self, owner, balance= 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0: 
            self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False
