def find_largest(nums: list[int]):
    if len(nums) <= 0:
        return -1

    largest = nums[0]
    for num in nums:
        if num > largest:
            largest = num

    return largest


print(find_largest(nums=[3,1,2,2,1,0,-4]))