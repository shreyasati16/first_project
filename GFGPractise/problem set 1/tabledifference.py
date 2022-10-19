a=int(input("enter a: "))
b=int(input("enter b: "))
res=[]
for i in range(1,10):
    c=(b*i)-(a*i)
    res.append(c)
print(res)