class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s) - 1
        
        while i < j:
            if i < j:
                temp = s[j]
                s[j] = s[i]
                s[i] = temp
                i = i + 1
                j = j - 1
                
        
        