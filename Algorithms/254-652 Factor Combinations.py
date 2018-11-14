from math import sqrt
class Solution:
    """
    @param n: An integer
    @return: a list of combination
    """
    def getFactors(self, n):
        # write your code here
        ans = []

        self.dfs(2, n, [], ans)
        return ans
    
    def dfs(self, start, n, item, ans):
        if n <= 1:
            if len(item) > 1:
                ans.append(item)
            return

        for i in range(start, int(sqrt(n))+1):
            if n % i == 0:
                self.dfs(i, n/i, item + [i], ans)
        
        if n>= start:
            self.dfs(n, 1, item + [n], ans)  

# the last two lines. why??????
