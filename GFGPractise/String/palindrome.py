# def isPalindrome(s):
#     return s==s[::-1]
# s='malayalam'
# isPalindrome(s)
# if s:
#     print("yes")
# else:
#     print("No")
s=input("enter: ")
low=0
high=len(s)-1
while low<high:
    if s[low]!=s[high]:
        print("NO")
        break
    low=low+1
    high=high-1
else:
    print("yes")


    
