nums = [1 , 3 , 5 , 6]
target = 2
lenum = len(nums)
for i in range(0 , lenum):
    if (nums[i] >= target):
        print(i)
        break
    elif target > nums[i] and i == lenum-1:
        print(lenum)
        break

