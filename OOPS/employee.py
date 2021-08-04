# class Employee:
#     company="google" #specific to each class
# shreya = Employee()
# shreya.company  #object instantation
# Employee.company ="Youtube" #changing the class attribute
    # CLASS ATTRIBUTE
class Employee: #class name
    company="google" #Attribute name
shreya=Employee()
sanskriti=Employee()
print(shreya.company)
print(sanskriti.company)
Employee.company= "youtube"   #attribute name chage through class
shreya.salary= 10  #instance attribute gets printed
sanskriti.salary=20
print(shreya.company)
print(sanskriti.company)
print(shreya.salary)
print(sanskriti.salary)