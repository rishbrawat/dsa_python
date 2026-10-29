def remove_duplicates(nums:list[int]):
    write = 0
    for read in range(1, len(nums)):
        if nums[read-1] != nums[read]:
            write += 1
            nums[write] = nums[read]

    return (write + 1)