def second_largest(nums: list[int]):
    if len(nums) <= 1:
        return None
    
    sorted_nums = sorted(nums, reverse=True)

    for i in range(0, len(sorted_nums) - 1):
        if sorted_nums[i] != sorted_nums[i + 1]:
            return sorted_nums[i + 1]
            
    return None


print(second_largest(nums=[13, 12, 11, 10, 12, 12]))