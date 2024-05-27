class Customer:
    def __init__(self, ID, name, discount):
        self.__ID = ID
        self.__name = name
        self.__discount = discount

    # Getter for ID
    def getID(self):
        return self.__ID

    # Getter for name
    def getName(self):
        return self.__name

    # Getter for discount
    def getDiscount(self):
        return self.__discount

    # Setter for discount
    def setDiscount(self, discount):
        self.__discount = discount

    # String representation of the customer
    def __str__(self):
        return f"{self.__name}({self.__ID})"


customer1 = Customer(1, "John Doe", 10)
print(customer1)  # John Doe(1)
print(f"ID: {customer1.getID()}")  # ID: 1
print(f"Name: {customer1.getName()}")  # Name: John Doe
print(f"Discount: {customer1.getDiscount()}%")  # Discount: 10%

customer1.setDiscount(15)
print(f"Updated Discount: {customer1.getDiscount()}%")  # Updated Discount: 15%
