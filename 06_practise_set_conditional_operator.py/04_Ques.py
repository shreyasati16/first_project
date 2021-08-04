#WAP to find out wheater the username contains less than 10 characteres or not
a=str(input("enter username: "))
print(len(a))
if(len(a)<10):
    print("less than 10 character")
else:
    print("greater than 10 cahracter")
