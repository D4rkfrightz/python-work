array = [33,55,77,99,98,39,70]
temp = 0
def find_highest_number(array):
    for i in range(0,len(array)) :
      if array[i] < array[i + 1] :
         temp = array[i]
         array[i] = array[i + 1]
         array[i + 1] = temp

find_highest_number(array)
print("the list answer is from highest to lowest is" , array)