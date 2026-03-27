class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       
       #Check if they are the same lenght
        if len(s) != len(t):
            return False
        
        ledger = {}
        for char in s:
            if char in ledger:
                ledger[char] += 1
            else:
                ledger[char] = 1
        
        for char in t:
            if char in ledger:
                ledger[char]-=1
            else:
                return False
        
        return all(v==0 for v in ledger.values())
        