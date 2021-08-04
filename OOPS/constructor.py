from instance_class_attribute import employee


class Employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def getinfo(self):
        print(f"the name of employee is {self.name}")
        print(f"the age is {self.age}")
        print(f"the salary is {self.salary}")        
Employeedetails= Employee("shreya",10,100000)
Employeedetails1=Employee("ishita",18,14000)
Employeedetails.getinfo()
Employeedetails1.getinfo()


