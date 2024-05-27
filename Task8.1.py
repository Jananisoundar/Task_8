class Circle:
    # Private class variable for pi
    __pi = 3.141

    def __init__(self, radius=1.0, color="red"):
        self.__radius = radius
        self.__color = color

    # Getter for radius
    def getRadius(self):
        return self.__radius

    # Setter for radius
    def setRadius(self, radius):
        self.__radius = radius

    # Getter for color
    def getColor(self):
        return self.__color

    # Setter for color
    def setColor(self, color):
        self.__color = color

    # Method to calculate the area
    def getArea(self):
        return self.__pi * self.__radius ** 2

    # Method to calculate the circumference
    def getCircumference(self):
        return 2 * self.__pi * self.__radius

    # Method to return a string representation of the object
    def toString(self):
        return f"Circle[radius={self.__radius},color={self.__color}]"


circle1 = Circle()
print(circle1.toString())  # Circle[radius=1.0,color=red]

circle2 = Circle(5.0)
print(circle2.toString())  # Circle[radius=5.0,color=red]
print(f"Area: {circle2.getArea()}")  # Area: 78.525
print(f"Circumference: {circle2.getCircumference()}")  # Circumference: 31.41

circle3 = Circle(2.5, "blue")
print(circle3.toString())  # Circle[radius=2.5,color=blue]
print(f"Area: {circle3.getArea()}")  # Area: 19.63125
print(f"Circumference: {circle3.getCircumference()}")  # Circumference: 15.705
