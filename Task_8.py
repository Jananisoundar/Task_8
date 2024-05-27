class Circle:
    # Private class variable for pi
    __pi = 3.141

    def __init__(self, radii_list):
        # Initialize the object with a list of radii
        self.radii = radii_list

    def area(self):
        # Calculate the area for each radius in the list
        areas = [self.__pi * radius**2 for radius in self.radii]
        return areas

    def perimeter(self):
        # Calculate the perimeter for each radius in the list
        perimeters = [2 * self.__pi * radius for radius in self.radii]
        return perimeters


radii_list = [10, 501, 22, 37, 100, 999, 87, 352]
circle = Circle(radii_list)

# Calculate areas and perimeters
areas = circle.area()
perimeters = circle.perimeter()

# Display the results
print("Areas:", areas)
print("Perimeters:", perimeters)


    