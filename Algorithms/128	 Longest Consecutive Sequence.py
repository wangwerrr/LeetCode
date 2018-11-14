# O(n)
class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
        dict={}
        
        for x in num:
            dict[x] = 1
            
        ans = 0
        
        for x in num:
            if x in dict:
                len = 1
                del dict[x]
                l = x - 1
                r = x + 1
                while l in dict:
                    del dict[l]
                    l -= 1 
                    len += 1
                while r in dict:
                    del dict[r]
                    r += 1
                    len += 1
                if ans < len:
                    ans = len
                    
        return ans
# look at the l,r of each elements, decide if it is part of the longest seq
# need to create a dict to record it
