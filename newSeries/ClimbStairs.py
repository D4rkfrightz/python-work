Major = [2 , 2 , 2 , 3 , 1]
lenMajor =  len(Major)
dictionary ={}
for i in range(0 , lenMajor):
    if Major[i] not in dictionary:
        # print(Major[i])
        dictionary[Major[i]] = 1
    else:
        # print(Major[i], "saad")
        dictionary[Major[i]] = dictionary[Major[i]]+1

for i in dictionary:
    if (dictionary[i]>= lenMajor/2):
        print(i)