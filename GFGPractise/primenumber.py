n=int(input("enter a number:"))
if (n<=1):
    print("no")
else:
    for i in range(2,n):
        if(n%i==0):
            print("NO")
            break
    else:
        print("yes")
