class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        output = 0
        starting_seq_num = 0
        nums = set(nums)

        if len(nums) == 0:
            return 0

        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                output = max(output, length)

        return output
