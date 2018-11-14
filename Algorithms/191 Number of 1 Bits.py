class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        bits = 0
        mask = 1
        
        for i in range(32):
            if mask & n != 0:       # if the current position of n is 0, then mask & 0 == 0, but if not , it is not equal to 1!
                bits = bits + 1
            mask = mask << 1
        
        return bits
        
