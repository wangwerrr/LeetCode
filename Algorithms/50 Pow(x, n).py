class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        # n -> binary , o(n) = logn
        
        if n < 0:
            x = 1/x
            n = -n
        
        ans, tmp = 1, x
        while n!=0:
            if n % 2 == 1:
                ans = ans * tmp
            tmp, n = tmp * tmp, n/2
        
        return ans
            
