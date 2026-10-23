def is_array_sorted(nums: list[int]):
    if len(nums) < 1:
        return

    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            return False

    return True



# is_array_sorted(nums=[1,2,3])

print(is_array_sorted(nums=[121,1,121,-12,1,0]))