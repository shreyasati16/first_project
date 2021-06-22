#WAP to find out grade of a student in the following list(given)
marks =int(input("enter your marks: "))
if(marks<50):
    print(" F GRADE")
elif(50<marks<60):
    print("D grade")
elif(60<marks<70):
    print("C GRADE")
elif(70<marks<80):
    print("B GRADE")
elif(80<marks<90):
    print("A GRADE")
elif(90<marks<100):
    print("A+ GRADE")
else:
    print("type grade less than 100")
