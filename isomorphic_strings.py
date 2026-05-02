class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        letters = {}
        reverse = {}

        for letter_s, letter_t in zip(s,t):
            if letter_s in letters and letters[letter_s] != letter_t:
                return False
            if letter_t in reverse and reverse[letter_t] != letter_s:
                return False
            letters[letter_s] = letter_t
            reverse[letter_t] = letter_s

        return True
