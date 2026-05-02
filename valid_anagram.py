class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(t) != len(s):
            return False

        anagram_s = {}
        anagram_t = {}
        for letter_s, letter_t in zip(s, t):
            anagram_s[letter_s] = anagram_s.get(letter_s, 0) + 1
            anagram_t[letter_t] = anagram_t.get(letter_t, 0) + 1
            
        if sorted(anagram_t.items()) != sorted(anagram_s.items()):
            return False
        
        return True
