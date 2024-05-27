from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class User:
    userId: str
    password: str
    loginStatus: str

    def verifyLogin(self) -> bool:
        # Implement login verification logic here
        pass


@dataclass
class Customer(User):
    customerName: str
    address: str
    email: str
    phone: int
    creditCardInfo: str
    shippingInfo: str

    def register(self):
        # Implement registration logic here
        pass

    def login(self):
        # Implement login logic here
        pass

    def updateProfile(self):
        # Implement profile update logic here
        pass


@dataclass
class Administrator(User):
    adminName: str
    email: str

    def updateCatalog(self) -> bool:
        # Implement catalog update logic here
        pass


@dataclass
class ShoppingCart:
    cartId: int
    productID: int
    quantity: int
    dateAdded: str

    def addCartItem(self):
        # Implement add cart item logic here
        pass

    def deleteCartItem(self):
        # Implement delete cart item logic here
        pass

    def updateQuantity(self):
        # Implement update quantity logic here
        pass

    def viewCartDetails(self):
        # Implement view cart details logic here
        pass

    def checkout(self):
        # Implement checkout logic here
        pass


@dataclass
class OrderDetail:
    orderId: int
    productId: int
    productName: str
    quantity: int
    unitCost: float
    subtotal: float

    def calcPrice(self):
        self.subtotal = self.quantity * self.unitCost


@dataclass
class ShippingInfo:
    shippingId: int
    shippingType: str
    shippingCost: float
    shippingRegionId: int

    def updateShippingInfo(self):
        # Implement update shipping info logic here
        pass


@dataclass
class Orders:
    orderId: int
    dateCreated: str
    dateShipped: str
    status: str
    customerId: str
    customerName: str
    shippingId: int
    orderDetails: List[OrderDetail] = field(default_factory=list)

    def placeOrder(self):
        # Implement place order logic here
        pass


@dataclass
class Product:
    productId: int
    name: str
    description: str
    price: float
    imageFileName: str

    def displayProduct(self):
        # Implement display product logic here
        pass

    def getProductDetails(self):
        # Implement get product details logic here
        pass


@dataclass
class Category:
    categoryId: int
    departmentId: int
    categoryName: str
    description: str

    def getProductsInCategory(self):
        # Implement get products in category logic here
        pass


@dataclass
class Department:
    departmentId: int
    name: str
    description: str

    def getCategoryInDepartment(self):
        # Implement get category in department logic here
        pass


@dataclass
class SessionManager:
    userId: str
    departmentName: str

    def getDepartment(self):
        # Implement get department logic here
        pass
