class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        slow = 0
        window_sum = 0
        result = float('inf')

        for fast in range(len(nums)):
            window_sum += nums[fast]

            while window_sum >= target:
                result = min(result, fast-slow+1)
                window_sum -= nums[slow]
                slow += 1

        return 0 if result == float('inf') else result
