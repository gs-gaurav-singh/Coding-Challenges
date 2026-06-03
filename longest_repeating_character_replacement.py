class Solution:
    def characterReplacement(self, s, k):
        slow = 0
        window = {}
        max_freq = 0
        result = 0

        for fast in range(len(s)):
            # expand
            window[s[fast]] = window.get(s[fast], 0) + 1
            max_freq = max(max_freq, window[s[fast]])

            # shrink when replacements needed > k
            while (fast - slow + 1) - max_freq > k:
                window[s[slow]] -= 1
                slow += 1

            result = max(result, fast - slow + 1)

        return result
