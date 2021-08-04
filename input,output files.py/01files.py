from os import close


#this will read the .txt files
f = open('shreya.txt','r') #here 'r' modes means read mode.
data = f.read()
print(data)
f.close()
