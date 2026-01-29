class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        
        if nums:
            temp_num = nums[0]
        else:
            return []
          
        results = []
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]+1:
                if temp_num == nums[i-1]:
                    results.append(str(temp_num))
                else:
                    results.append(f"{temp_num}->{nums[i-1]}")

                temp_num = nums[i]

        if temp_num == nums[-1]:
            results.append(str(temp_num))
        else:
            results.append(f"{temp_num}->{nums[-1]}")

        return results
