class Solution:
    def longestOnes(self, nums, k):
        slow = 0
        zero_count = 0
        result = 0

        for fast in range(len(nums)):
            if nums[fast] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[slow] == 0:
                    zero_count -= 1
                slow += 1

            result = max(result, fast - slow + 1)

        return result
