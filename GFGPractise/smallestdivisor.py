n=int(input("enter a number: "))
# for i in range(2,n+1):
#     if n%i==0:
#         print(i)
#         break
x=2
while x<=n:
    if n%x==0:
        print("the smallest divisor is :",x)
        break
    x=x+1

