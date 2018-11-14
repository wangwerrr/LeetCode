class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
       
        def backtrack(s="", left=0, right=0):
            if len(s) == 2 * n:
                output.append(s)
                return
            
            if left < n:
                backtrack(s + '(', left+1, right)
            if right < left:
                backtrack(s + ')', left, right+1)
        
        output = [] 
        
        backtrack()
        
        return output

# func inside func
# recursion
