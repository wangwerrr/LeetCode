class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        return 0 if n == 0 else n/5 + self.trailingZeroes(n/5)
    
# Because all trailing 0 is from factors 5 * 2. In the n! operation, factors 2 is always ample. So we just count how many 5 factors in all number from 1 to n.
