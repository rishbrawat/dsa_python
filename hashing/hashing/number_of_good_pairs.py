def numIdenticalPairs(nums: list[int]):
    # totalPairs = 0
    # n = len(nums)
# 
    # for i in range(n):
        # for j in range(i+1, n):
            # if nums[i] == nums[j]:
                # totalPairs += 1
# 
    # return totalPairs



    # freq = {}
    # for num in nums:
    #     freq[num] = freq.get(num, 0) + 1

    # totalPairs = 0

    # for count in freq.values():
    #     totalPairs += count * (count - 1) // 2

    # return totalPairs


    freq = {}
    totalPairs = 0

    for num in nums:
        previous = freq.get(num, 0)

        totalPairs += previous

        freq[num] = previous + 1

    return totalPairs

print(numIdenticalPairs(nums = [1,1,1,1]))