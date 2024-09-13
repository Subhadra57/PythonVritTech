class Employee:
    def __init__(self,name,current_salary): #5000 , bonus, tax
        self.name = name 
        self.current_salary = current_salary 
        print(f"{self.name} current salary is {self.current_salary}")
        self.bonus()
        self.tax()

    def bonus(self):
        #bonus with price
        bonus = 100
        self.bonus_with_salary = bonus 
        print(f"bonus is added to {self.name}",self.bonus_with_salary)
        bonus = 0.5 #percentage
        self.bonus_s = bonus 
        print(f"bonus is added to {self.name}",self.bonus_s)

    def tax(self):
        #tax with price
    # @@ -20,26 +20,18 @@ def tax(self):

    def total_salary(self):
        #total salary with price
        self.total_salary = self.current_salary + self.bonus_with_salary - self.tax_with_salary
        self.total_salary = self.current_salary + self.bonus_s - self.tax_with_salary
        print("total salary ",self.total_salary,"\n**********************")




ram_obj = Employee("ram",5000)
ram_obj.total_salary()


ram_obj = Employee("shyam",50000)
ram_obj.total_salary()


ram_obj = Employee("hari",10000)
ram_obj.total_salary()


staff_data = [{"name":"umesh","salary":40000},{"name":"pradeep","salary":60200},{"name":"sagar","salary":19500}]

# staff_data = [{"name":"umesh","salary":40000,'bonus':34,'tax':12,'total_salary':40022},{"name":"pradeep","salary":60200...},{"name":"sagar","salary":19500....}]

print(staff_data)