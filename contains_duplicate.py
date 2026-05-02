class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        self.nums = nums
        return (len(nums) != len(set(nums)))
