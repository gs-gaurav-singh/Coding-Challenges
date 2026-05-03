class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram = {}

        for i in strs:
            sorted_words = tuple(sorted(i))
            # print(sorted_words)
            if sorted_words not in anagram:
                anagram[sorted_words] = []
            anagram[sorted_words].append(i)
        
        return list(anagram.values())
