class Customer:
    def __init__(self, ID, name, discount):
        self.__ID = ID
        self.__name = name
        self.__discount = discount

    def getID(self):
        return self.__ID

    def getName(self):
        return self.__name

    def getDiscount(self):
        return self.__discount

    def setDiscount(self, discount):
        self.__discount = discount

    def __str__(self):
        return f"{self.__name}({self.__ID})"


class Invoice:
    def __init__(self, ID, customer, amount):
        self.__ID = ID
        self.__customer = customer
        self.__amount = amount

    def getID(self):
        return self.__ID

    def getCustomer(self):
        return self.__customer

    def setCustomer(self, customer):
        self.__customer = customer

    def getAmount(self):
        return self.__amount

    def setAmount(self, amount):
        self.__amount = amount

    def getCustomerName(self):
        return self.__customer.getName()

    def getAmountAfterDiscount(self):
        discount = self.__customer.getDiscount()
        return self.__amount * (1 - discount / 100)

    def __str__(self):
        return f"Invoice[ID={self.__ID}, customer={self.__customer}, amount={self.__amount:.2f}]"



customer1 = Customer(1, "John Doe", 10)
invoice1 = Invoice(101, customer1, 1000.0)

print(invoice1)  # Invoice[ID=101, customer=John Doe(1), amount=1000.00]
print(f"Customer Name: {invoice1.getCustomerName()}")  # Customer Name: John Doe
print(f"Amount After Discount: {invoice1.getAmountAfterDiscount():.2f}")  # Amount After Discount: 900.00

# Updating the amount
invoice1.setAmount(1200.0)
print(f"Updated Amount: {invoice1.getAmount():.2f}")  # Updated Amount: 1200.00
print(f"Amount After Discount: {invoice1.getAmountAfterDiscount():.2f}")  # Amount After Discount: 1080.00

# Updating the customer
customer2 = Customer(2, "Jane Smith", 15)
invoice1.setCustomer(customer2)
print(invoice1)  # Invoice[ID=101, customer=Jane Smith(2), amount=1200.00]
print(f"Amount After Discount: {invoice1.getAmountAfterDiscount():.2f}")  # Amount After Discount: 1020.00
