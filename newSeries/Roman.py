Roman = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000}
s = "III"  
LenVal = len(s)
Sum = 0

for i in range(1, LenVal+1):
    # IV and IX
    if((s[LenVal-i] == "I" and LenVal-i+1<LenVal) and ( s[LenVal-i+1]=="V" or s[LenVal-i+1]=="X")):
        Sum = Sum - Roman[s[LenVal-i]]
        # XL and XC
    elif((s[LenVal-i] == "X" and LenVal-i+1<LenVal) and ( s[LenVal-i+1]=="L" or s[LenVal-i+1]=="C")):
        Sum = Sum - Roman[s[LenVal-i]]
    # CD and CM
    elif((s[LenVal-i] == "C" and LenVal-i+1<LenVal) and ( s[LenVal-i+1]=="D" or s[LenVal-i+1]=="M")):
        Sum = Sum - Roman[s[LenVal-i]]        
    else:
        Sum = Sum + Roman[s[LenVal-i]]
print(Sum)