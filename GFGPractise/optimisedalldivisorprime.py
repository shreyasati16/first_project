n=int(input("enter a number: "))
x=1
while x*x<n:
    if n%x==0:
        print(x)
        print(n/x)
    x=x+1
if x*x==n:
    print(x) 