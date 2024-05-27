class Customer:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"{self.name}({self.id})"

class Account:
    def __init__(self, id, customer, balance=0.0):
        self.id = id
        self.customer = customer
        self.balance = balance

    def getID(self):
        return self.id

    def getCustomer(self):
        return self.customer

    def getBalance(self):
        return self.balance

    def setBalance(self, balance):
        self.balance = balance

    def getCustomerName(self):
        return self.customer.name

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Amount withdrawn exceeds the current balance!")
        return self

    def __str__(self):
        return f"{self.customer} balance=${self.balance:.2f}"


customer1 = Customer(1, "John Doe")
account1 = Account(101, customer1, 500.0)

print(account1)  # John Doe(1) balance=$500.00
account1.deposit(150.0)
print(account1)  # John Doe(1) balance=$650.00
account1.withdraw(200.0)
print(account1)  # John Doe(1) balance=$450.00
account1.withdraw(500.0)  # Amount withdrawn exceeds the current balance!
print(account1)  # John Doe(1) balance=$450.00
