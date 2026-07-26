#Modify the summary method of the Account class to display the name and phone number of each client

class Client:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

class Account:
    def __init__(self, clients, number, balnce=0):
        self.balnce = 0
        self.clients = clients
        self.number = number
        self.operations = []
        self.deposit(balance)

    def summary(self):
        print(f"AC N{self.number} Balance: {self.balance:10.2f}")
        for client in self.clients:
            print(f"Name: {client.name}\nPhone: {client.phone}\n")

    def withdraw(self, value):
        if self.balance >= value:
            self.balance -= value
            self.operations.append(["WITHDRAW", value])
        else:
            print("Insufficient balance!")

    def deposit(self, value):
        self.balance += value
        self.operations.append(["DEPOSIT", value])

    def statement(self):
        print(f"Statement AC N {self.number}\n")
        for o in self.operations:
            print(f"{o[0]: 10s} {o[1]:10.2f}")
        print(f"\n   Balance: {self.balance:10.2f}\n")

mary = Client("Mary", "1243-3321")
john = Client("John", "5554-3322")

account = Account([mary, john], 1234, 5000)
account.summary()
