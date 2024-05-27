from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Admin:
    Id: int
    Name: str

    def viewProducts(self):
        # Implement view products logic here
        pass

    def addProducts(self):
        # Implement add products logic here
        pass

    def deleteProducts(self):
        # Implement delete products logic here
        pass

    def modifyProducts(self):
        # Implement modify products logic here
        pass

    def makeShipment(self):
        # Implement make shipment logic here
        pass

    def confirmDelivery(self):
        # Implement confirm delivery logic here
        pass

@dataclass
class Products:
    Id: int
    Name: str
    Group: str
    Subgroup: str

@dataclass
class Guest:
    def viewProducts(self):
        # Implement view products logic here
        pass

    def getRegistered(self):
        # Implement get registered logic here
        pass

@dataclass
class Cart:
    Id: int
    NumberOfProducts: int
    Product1: str
    Product2: str
    Productn: str
    Price: float
    Total: float

@dataclass
class Customer:
    Id: str
    Name: str
    Address: str
    PhNo: int
    cart: Optional[Cart] = None

    def buyProducts(self):
        # Implement buy products logic here
        pass

    def viewProducts(self):
        # Implement view products logic here
        pass

    def makePayment(self):
        # Implement make payment logic here
        pass

    def addToCart(self):
        # Implement add to cart logic here
        pass

    def deleteFromCart(self):
        # Implement delete from cart logic here
        pass

@dataclass
class Payment:
    CustomerId: str
    Name: str
    CardType: str
    CardNo: str

    def processPayment(self):
        # Implement payment processing logic here
        pass
