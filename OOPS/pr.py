class RailwayForm:
    formtype="railwayform"
    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Name is {self.train}")
        print(f"Name is {self.PNR}")
shreyaApplication= RailwayForm()  
shreyaApplication.name="shreya"
shreyaApplication.train="Rajdhani Express"
shreyaApplication.PNR="180147"
shreyaApplication.printdata()