class Solution:
    def isPalindrome(self, s: str) -> bool:
        #lets remove the punctuation marks
        cleaned = []
        for char in s:
            if char.isalnum():
                cleaned.append(char.lower())
        x = "".join(cleaned)
        return x == x[::-1]