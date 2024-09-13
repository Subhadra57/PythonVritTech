class Mathmatics:

    def sum(self,a,b):
        print("addition is : ",a+b)

    def sub(self,a,b):
        print("subtraction is : ", a-b)

    def mul(self,a,b):
        print("multiply is  ",a*b)

a = int(input("Enter first number#>>>..."))
b = int(input("Enter second number#>>>..."))

obj = Mathmatics() #object is creating
obj.sum(a,b)
obj.sub(a,b)
obj.mul(a,b)