n=int(input("enter a number: "))
for i in range(0,n):
    for j in range(n-i):
        print("*",end=" ")
    print()