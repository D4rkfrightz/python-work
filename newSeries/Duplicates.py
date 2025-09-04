array = [3 ,4 , 5 , 5 , 2 , 1 , 1 , 3]
extra = []
for i in range(0 , len(array)):
    if array[i] not in extra:
        extra.append(array[i])
print("the array without duplicates is ",sorted(extra))
