class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        num = 0
        sign = 1
        
        if x < -(2**31) or x > 2**31 - 1:     # original number limit
            return 0
        
        x = str(x)
        if x[0] == '-':
            sign = -1
            x = x[1:]
        
        for i in range(len(x)-1, -1, -1):
            num = num*10 + int(x[i])
            
        if num < -(2**31) or num > 2**31 - 1:     # reversed limit
            return 0 
        else:
            return sign * num
        
