# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        
        while low <= high:
            mid = low + (high - low) // 2
            re = guess(mid)
            if re == 0:
                return mid
            elif re == -1:
                high = mid - 1
            else:
                low = mid + 1
        return -1
        
# classy
