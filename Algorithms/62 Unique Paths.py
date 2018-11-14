class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        grid = [[1 for j in range(m)] for i in range(n)]

        for i in range(1, n):
            for j in range(1, m):
                grid[i][j] = grid[i-1][j] + grid[i][j-1]
        
        return grid[-1][-1]
    
# n: row, m: col
# Dynamic Programming
