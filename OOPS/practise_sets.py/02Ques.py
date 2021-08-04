class Calculator:
    def __init__(self,num):
        self.number=num
    def square(self):
        print(f"The square of {self.number} is {self.number**2}")
    def squareroot(self):
        print(f"the Squareroot of {self.number} is {self.number**0.5}")
    def cube(self):
        print(f"the cube of {self.number} is {self.number**3}")
    @staticmethod
    def greet():
        print(f"hello! , hope you are doing well")
a=Calculator(30)
a.square()
a.squareroot()
a.cube()
a.greet()
