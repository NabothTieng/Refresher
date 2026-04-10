class Solution:
    def modifyString(self, s: str) -> str:
        # Convert string to list so we can modify characters in place
        result = list(s)
        
        for i in range(len(result)):
            if result[i] == '?':
                # Try 'a', 'b', 'c' — one of them is guaranteed to work
                for ch in 'abc':
                    # Check if this character would be same as left or right neighbor
                    left_same = (i > 0 and result[i-1] == ch)
                    right_same = (i < len(result)-1 and result[i+1] == ch)
                    
                    if not left_same and not right_same:
                        result[i] = ch
                        break
        
        return ''.join(result)