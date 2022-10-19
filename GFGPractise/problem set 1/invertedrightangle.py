n=int(input("enter a number: "))
for i in range(n):
    for j in range(n):
        print((n-i)*"*")
        n-=1
    break
print()
