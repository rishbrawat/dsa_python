def reverse_list(nums: list[int]):
    left = 0
    right = len(nums)-1

    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums

print(reverse_list(nums = [1,2,3,4]))
