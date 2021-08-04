class Programmer:
    company="microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product      
    def getInfo(self):
        print(f"the name of the Employee working in {self.company} is {self.name} under the product name of {self.product}")
shreya=Programmer("shreya","git") 
ishita=Programmer("ishita","microsoft")
shreya.getInfo() 
ishita.getInfo()



