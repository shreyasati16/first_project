with open('sample.txt','r') as f:
    if "twinkle" in f.read: 
        print("twinkle")
    else:
        print("not present")
