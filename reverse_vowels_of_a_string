class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]
        s_list = list("".join(s))
        start = 0
        last = len(s_list) - 1

        while start < last:
            if s_list[start] not in vowels:
                start += 1
            elif s_list[last] not in vowels:
                last -= 1
            elif s_list[start] in vowels and s_list[last] in vowels:
                s_list[start], s_list[last] = s_list[last], s_list[start]

                start += 1
                last -= 1

        return ''.join(map(str, s_list))
