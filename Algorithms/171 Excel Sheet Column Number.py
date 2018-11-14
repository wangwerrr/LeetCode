class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        col_dict = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = list(s)
        n = len(s)
        output = 0
        
        if n == 0:
            return None
        
        for char in s:
            output = output + (col_dict.index(char)+1) * 26 ** (n-1)
            n = n - 1
            
        return output
