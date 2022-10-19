#GCD{greatest common divisor} in python.
from cgitb import small
from math import gcd
from re import I


a=int(input("enter a number:"))
b=int(input("enter a number:"))
small=min(a,b)
for i in range(1,small+1):
    if(a%i==0 & b%i==0):
        gcd=i
print("gcd is ",gcd)