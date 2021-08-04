class employee: #class name
    company="google" #class attribute name
    salary = 100   
shreya= employee()
sanskriti= employee()
#class attribute gets printed beacuse instance attribute is not defined.
# print(shreya.salary)
shreya.salary=25
print(shreya.salary)#here attribute is linked with object and create a instance attribute
print(sanskriti.salary) 