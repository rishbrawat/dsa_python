def sortedSquares(nums: list[int]):
    left = 0
    right = len(nums)-1
    result = []
    for i in range(len(nums)):
        nums[i] *= nums[i]
        result.append(nums[i])

    while left < right:
        if nums[left] < nums[right]:
            result.append(nums)

print(sortedSquares(nums=[-4,-1,0,3,10]))