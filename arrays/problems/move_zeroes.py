def move_zeroes(nums: list[int]):
    for i in range(len(nums)):
        for j in range( len(nums)-1):
            if nums[j] == 0 and nums[j+1] != 0:
                temp = nums[j+1]
                nums[j+1] = nums[j]
                nums[j] = temp

    return nums

print(move_zeroes(nums=[1,0,0,1,1,0,-2,1,1,1,1,1,9,9,9,9,1,0,0,0,0,-0]))