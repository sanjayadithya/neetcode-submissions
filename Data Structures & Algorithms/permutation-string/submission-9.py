from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False
        
        s1_counts = Counter(s1)

        n = len(s1)

        i,j = 0,n

        while j <= len(s2):
                
            substring = s2[i:j]

            if Counter(substring) == s1_counts:
                return True
            else:
                i += 1 
                j += 1

        return False