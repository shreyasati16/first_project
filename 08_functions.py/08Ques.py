
# def star(n):
#     for i in range(n):
#         return("*"*(n-i))

# f=star()
# print(f)
def func1(n):
    for i in range(n):
        print(" " * (2*n-i),end="")
        print("*" * (2*i+1),end=" ")
        print(" " * (2*n-i))
        
print(func1(10))
