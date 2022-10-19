#You are given a number n, you need to print its multiplication table in a single line.
n=int(input("enter a number: "))
for i in range(1,11):
    print(n*i,end=" ")
