class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        clean_text = "".join(char for char in s if char.isalnum()).lower()

        clean_text_list = list(clean_text)
        start = 0
        last = len(clean_text_list) - 1
        while start < last:
            if clean_text_list[start] != clean_text_list[last]:
                return False
                break
            start += 1
            last -= 1
        return True
