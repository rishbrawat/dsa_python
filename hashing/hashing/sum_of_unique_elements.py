def sumOfUnique(nums: list[int]) -> int:
        freq = {}
        totalSum = 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1


        for value, count in freq.items():
              if count == 1:
                    totalSum += value

        return totalSum

print(sumOfUnique(nums = [1,2,3,2]))