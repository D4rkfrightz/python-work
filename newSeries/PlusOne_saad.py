digits = [9 , 8 , 7 , 9]
saad_length =len(digits)
for i in range(0, saad_length):
    temp = i+1
    if (digits[saad_length-temp]!=9):
        digits[saad_length-temp]=digits[saad_length-temp]+1
        break
    elif(digits[saad_length-temp] == 9 and saad_length-temp!=0):
        digits[saad_length-temp] = 0
    else:
        digits[saad_length-temp] = 0
        digits.insert(0, 1)
        
print(digits)