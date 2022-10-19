#You are given a String S, you need to print its characters at even indices(index starts at 0).
str=input("Enter a name: ")
res=[]
for i in range(0,len(str)):
    if i%2==0:
        res.append(str[i])
print(res)
    

