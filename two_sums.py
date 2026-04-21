class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        subs = {}
        for i, num in enumerate(nums):
            complement = target - num

            if complement in subs:
                return [subs[complement], i]

            subs[num] = i
