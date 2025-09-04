# student add details name, father name , class
# student delete 
# student update data


array = [1,2,34,4] # 4
result=[]
# print(array)
saad = int(input("Enter a value you want to delete "))
for i in range(0,4):
    if (array[i] != saad):
        result.append(array[i])
    else:
        print("value", array[i], "removed from the list")
print(result)
    # if(i==34):
    #     print(i)
# array.pop(2)
# print(array)
# make function of this only to kick out the student data
# in the list at loops.py who has the percentage less than 50 percent
