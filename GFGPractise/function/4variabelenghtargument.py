# def sum(*elements):
#     res=0
#     for x in elements:
#         res=res+x
#     return res
# print(sum(10,20))
# d=sum(20,220,100,400)
# print(d)
def sum(**elements):
    for d,v in elements.items():
        print(f"{d} is {v}")
sum(id= 101,name='abc',price=100)
print()
sum(id=102,name="xyz")
print()


