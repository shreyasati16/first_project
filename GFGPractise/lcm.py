#LCM in python
import math
a=int(input("enter a number: "))
b=int(input("enter another number: "))
gcd=math.gcd(a,b)
lcm=(a*b)/gcd
print("lcm is",lcm)
