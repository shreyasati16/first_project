#WAP to convert celcius to farehenhite
#Formula	
#(0°C × 9/5) + 32 = 32°F 
def farah(cel):
    return cel*(9/5) + 32
c=37
f=farah(c)
print("the temperature in farahite is", str(f))
