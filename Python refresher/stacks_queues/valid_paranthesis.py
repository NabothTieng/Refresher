class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        
        valid_comb = {")":"(","]":"[","}":"{"}
        stack = []
        
        for char in s:
            if char in valid_comb:

                if stack and stack[-1] == valid_comb[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack 
        