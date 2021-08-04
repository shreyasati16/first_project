#WAP for spam detector
text = input("enter you text: ")
spam = False
if("make money" in text):
    spam = True
if("subscribe it" in text):
    spam = True
if("click it" in text):
    spam = True
if("buy now" in text):
    spam = True
else:
    spam = False
if(spam):
    print("this is spam")
else:
    print(text)