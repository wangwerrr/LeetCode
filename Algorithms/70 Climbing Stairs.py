class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
    #   return self.dpMemo(n, {})
        return self.dpTable(n)  
    
    # S1: Memorization; res is a dictionary
    def dpMemo(self, n, res):
        if n == 0 or n == 1:
            res[n] = 1
        if n not in res:
            res[n] = self.dpMemo(n-1, res) + self.dpMemo(n-2, res)
        return res[n]
    
    # S2: Tabulation; res is an array
    def dpTable(self, n):
        res = [0] * (n+1)
        res[0] = 1
        res[1] = 1
        
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2] # i, not n!!
        return res[n]
