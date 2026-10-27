def sortedSquares(nums: list[int]):
    for i in range(len(nums)):
        nums[i] *= nums[i]

    result = []
    left = 0
    
    right = (len(nums)-1)//2
    for i in range(right, len(nums)):
        result.append(nums[i])

    return result



print(sortedSquares(nums=[-4,-1,0,3,10]))