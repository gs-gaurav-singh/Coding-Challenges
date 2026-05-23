class Solution:
    def lengthOfLongestSubstring(self, s):
        seen = set()
        slow = 0
        result = 0

        for fast in range(len(s)):
            # shrink window until no duplicate
            while s[fast] in seen:
                seen.remove(s[slow])
                slow += 1
            
            seen.add(s[fast])
            result = max(result, fast - slow + 1)

        return result
