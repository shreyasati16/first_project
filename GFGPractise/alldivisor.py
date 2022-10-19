n=int(input("enter a number: "))
#12=2,4,6,8,10,12
res=[]
for i in range(1,n+1):
    if n%i==0:
        res.append(i)
print(res)
    

