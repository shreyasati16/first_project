#WAP for report card
sub1 = int(input("enter your subject1 marks:"))
sub2 = int(input("enter your subject2 marks:"))
sub3 = int(input("enter your subject3 marks:"))
sub4 = int(input("enter your subject4 marks:"))
# if(sub1<33):
#     print("you are failed! in sub1")
# else:
#     print("congratualtions!you passed the examination in subject1")
# if(sub2<33):
#     print("you are failed! in sub2")
# else:
#     print("congratualtions!you passed the examination in subject2")
# if(sub3<33):
#     print("you failed in sub3")
# else:
#     print("congratualtions!you passed the examination in subject3")
# if(sub4<33):
#     print("you failed in sub4")
# else:
#     print("congratualtions!you passed the examination in subject4")
# total=((sub1+sub2+sub3+sub4)/4)
# print("your percentage is",total)
# if(total<40):
#     print("overall failed in END-SEM!")
# else:
#     print("congratulations!you passed the overall END-SEM")
 

 #method2

if(sub1>33 or sub2<33 or sub3<33 or sub4<33):
    print("you failed in any one of the subject")
elif(sub1+sub2+sub3+sub4/4)<40:
    print("you are overall failed")
else:
    print("you passed the all four exam")


