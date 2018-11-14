class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        
        s = "".join(c for c in s if c.isalnum()).lower()
        if len(s) == 0:
            return True
        
        i, j = 0, len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            i, j = i+1, j-1
        
        return True

    # instead of delete the unwanted ones, keep the num
