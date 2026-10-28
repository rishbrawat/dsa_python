def move_zeroes(nums: list[int]):
    write = 0

    for read in range(len(nums)):

        # this will swap non zero elements and it still does not place zeroes at the end
        if nums[read] != 0:
            nums[write] = nums[read]
            write += 1 # this is the index we need, it originally stops at the last swap

    for i in range(write, len(nums)): 
        # fill the remaining array with zeroes
        nums[i] = 0

    return nums


print(move_zeroes(nums=[1,0,2,0,0,3]))