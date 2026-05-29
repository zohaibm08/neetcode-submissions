class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = {}
        if len(s) != len(t):
            return False

        for i in s:
            counts[i] = counts.get(i,0) + 1
        
        for j in t:
            if j in counts and counts[j] > 0:
                counts[j] = counts.get(j, 0) - 1
            else:
                return False

        return True