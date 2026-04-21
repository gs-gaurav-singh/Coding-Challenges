class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        i = 0
        j = 0
        count = 0
        while count < len(s) and j != len(t):
            if s[i] != t[j] and j != len(t):
                j += 1
            elif s[i] == t[j]:
                i += 1
                j += 1
                count += 1
        
        if count == len(s):
            return True
        else:
            return False
