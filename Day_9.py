class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s is "":
            return True
        
        index = 0
        for i in range(len(t)):
            if t[i] == s[index]:
                index = index + 1
            if index >= len(s):
                return True
            
        return False