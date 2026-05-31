class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        output = []
        s_word_count = {}
        p_word_count = {}

        if len(p) > len(s):
            return output

        for i in range(len(p)):
            s_word_count[s[i]] = s_word_count.get(s[i], 0) + 1
            p_word_count[p[i]] = p_word_count.get(p[i], 0) + 1

        if s_word_count == p_word_count:
            output.append(len(p)-len(p))

        for i in range(len(p), len(s)):
            s_word_count[s[i]] = s_word_count.get(s[i], 0) + 1

            out = s[i - len(p)]
            s_word_count[out] -= 1
            if s_word_count[out] == 0:
                del s_word_count[out]

            if s_word_count == p_word_count:
                output.append(i - len(p) + 1)

        return output
