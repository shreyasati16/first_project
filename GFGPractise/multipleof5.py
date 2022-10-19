#print the numbers which are not the multiple of 5
l=[10,23,33,20,13,14,16,7]
# res=[]
# for i in range(len(l)):
#     if l[i]%5 != 0:
#         res.append(l[i])
#         continue
# print(res)
for x in l:
    if x%5==0:
        continue
    print(x)

    
    
