Array = [9,1,2,2,9,3,3,4]
Array.sort()
i = 0
while i < len(Array) - 1:
    if Array[i] == Array[i+1]:
        Array.pop(i+1)
    else:
        i =i+1

print(Array)