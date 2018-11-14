"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""

class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        # Write your code here
        candidate = 0
        for i in range(n):                  # if a knows b, then del a; else del b. At last we only get one candidate.
            if Celebrity.knows(candidate, i):     
                candidate = i
                
        # still we have to test if the candidate is a celebrity or not           
        for i in range(n):
            if candidate != i:
                if Celebrity.knows(candidate, i):
                    return -1
                if not Celebrity.knows(i, candidate):
                    return -1
            
        return candidate
        
        """
        for i in xrange(candidate):
            if Celebrity.knows(candidate, i) or not Celebrity.knows(i, candidate):
                return -1
        
        # we don't need to judge knows(candidate, i) for range(candidate + 1, n), since we've already done than during the first loop
        
        for i in xrange(candidate + 1, n):
            if not Celebrity.knows(i, candidate):
                return -1
                
        """
