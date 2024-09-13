#make your own Area library so that it can calculate 

#circle (it calclate area of circle)
#rectangle (it calclate area of rectangle)
#square (it calclate area of square)
#triangle (it calclate area of triangle)


# class Area:
#     def circle(radius):
#         print("calculate")

#     def rectangle(widht, height):
#             print("calculate")

#     def square(height):
#          print("calculate")

#     def triangle(height):
#          print("calculate")
#     import math

import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius

circle = Circle(5)
print(f"Area of the circle: {circle.calculate_area()}")




class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

rectangle = Rectangle(4, 6)
print(f"Area of the rectangle: {rectangle.calculate_area()}")




class Square:
    def __init__(self, side_length):
        self.side_length = side_length

    def calculate_area(self):
        return self.side_length * self.side_length

square = Square(4)
print(f"Area of the square: {square.calculate_area()}")





class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

triangle = Triangle(5, 3)
print(f"Area of the triangle: {triangle.calculate_area()}")


