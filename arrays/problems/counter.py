# count the total number of values greater than 'key' 

def counter(nums: list[int], key:int) -> int:

    # initially we initialize counter value at 0
    total_count = 0
    for num in nums:
        if num > key: # increase when there is new larger value
            total_count += 1

    return total_count

key = 10
nums = [11,1,-2,33,25]

total_count = counter(nums, key)
print(total_count)