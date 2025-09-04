palin = 1221
stringpalin = str(palin)
bool=False
for i in range(0 , len(stringpalin)):
    if stringpalin[i] != stringpalin[len(stringpalin)-i-1]:
        bool=False
        break
    else:
        bool=True

print(bool)
if bool==True:
    print("Yousaf")