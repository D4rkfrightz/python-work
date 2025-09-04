Sent = "luffy is still joyboy"
length_of_Sen= len(Sent)
# print(length_of_Sen)
# output= 5
saad =''
for i in range(1, length_of_Sen+2):
    if (Sent[length_of_Sen-i]!=' ' and i<=length_of_Sen):
        saad = saad+Sent[length_of_Sen-i]
    elif(len(saad)>0):
        print(len(saad))
        break
    # elif(i==length_of_Sen):
    #     print(len(saad))
    #     break