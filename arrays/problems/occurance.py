def find_occurance(nums: list[int], target: int):
    occured = 0
    for num in nums:
        if num == target:
            occured += 1


    return occured


print(find_occurance(nums=[1,2,3,3,3,4,-3], target=4))