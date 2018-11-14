class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        lo, hi = 1, x
        
        while True:
            mid = lo + (hi - lo)/2
            if mid > x / mid:
                hi = mid -1
            else:
                if mid + 1 > x / (mid + 1):
                    return mid
                lo = mid + 1

 # binary search
