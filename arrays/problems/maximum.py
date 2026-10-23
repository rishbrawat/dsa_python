def find_maximum(nums: list[int]) -> int:
    maximum = 0
    for num in nums:
        if num > maximum:
            maximum = num

    return maximum

nums = [20,-0, 201, -232,-11,22]
maximum = find_maximum(nums)

print(maximum)