def target_sum(nums: list[int], target: int) :

    for i in range(len(nums)):
        for j in range(1, len(nums)-i-1):
            if nums[i] + nums[j] == target:
                return (i, j)


print(target_sum(nums=[3, 6, 1, 8, 4], target=9))
            