# first check which digit is the last one. After finding it, increment one in it.
# And check if the last digit is 9 then just pop the number and put 1 against its place 
# and 0 in the next index. Find a way to increment the index when the number comes to 9.
# Find if there is a digit before the 9. If it is then increment it to 1 and put 0 instead
# of 9.
digits = [9 , 9]
for i in range(0,len(digits)):
    if i == len(digits) - 1 and digits[i] != 9 :
        digits[i] = digits[i] + 1
    elif digits[i] == 9 and i == len(digits) - 1 and i == 0  :
        digits.pop()
        digits.append(1)
        digits.append(0)
    elif i == len(digits) - 1 and i > 0 and digits[i] == 9:
        if digits[i-1] != 9:
            digits[i-1] = digits[i-1] + 1
            digits[i-1].pop()
            digits[i-1].append(0)
        else: 
            digits[i-2] == 0  
            digits.pop(i-3)
            digits.append(i-3== 1)

print(digits) 