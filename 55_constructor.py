import math


class Mathmatics:
    def __init__(self,first_number,second_number):
        self.a = first_number
        self.b = second_number

    def sum(self):
        print("addition is : ",self.a+self.b)

    def sub(self):
        print("subtraction is : ", self.a-self.b)

    def mul(self):
        print("multiply is  ",self.a*self.b)

a = int(input("Enter first number#>>>..."))
b = int(input("Enter second number#>>>..."))

obj = Mathmatics(a,b) #object is creating
obj.sum()
obj.sub()
obj.mul()