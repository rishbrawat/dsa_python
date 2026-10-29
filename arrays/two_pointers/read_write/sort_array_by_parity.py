def sort_array_by_parity(nums: list[int]):
    write = 0
    for read in range(len(nums)):
        if nums[read] % 2 == 0:
            nums[write],nums[read] = nums[read], nums[write]
            write += 1

    return nums


print(sort_array_by_parity(nums=[0]))
