def removeDuplicates(nums: list[int]):
    write = 1
    occured = 1

    for read in range(1, len(nums)):
        if nums[read-1] == nums[read]:
            occured += 1
        else:
            occured = 1

        if occured <= 2:
            nums[write] = nums[read]
            write += 1

    return write + 1

print(removeDuplicates(nums=[1,1,1,1,2,2,2,3,3,1,0,1,1]))