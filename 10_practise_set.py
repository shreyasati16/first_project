#name=input("enter a name: ")
#greeting="good morning"
#print(name + greeting)
letter = '''dear <|name|>
congratulations! 
your selected in ABC code company!
date:<|date|>'''
a = input("enter name\n ")
b = input("enter date\n")
letter= letter.replace("<|name|>",a)
letter =letter.replace("<|date|>",b)
print(letter)


