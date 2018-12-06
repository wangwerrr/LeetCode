class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def sink( i, j):
            # if a[i][j] is water or hits the border, return 0
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0":
                return 0

            # if a[i][j] is land, sink it and keep sinking its neighbors, return 1 in the end
            grid[i][j] = "0" # sink
            map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)) # side results
            return 1

        return sum(sink(i , j) for i in range(len(grid)) for j in range(len(grid[0])))

"""
if a[i][j] is water at the very beginning, sink() will return 0 immediately;
if a[i][j] is land at the very beginning, 0s and 1s will be returned as side results, but eventually sink() will return 1
"""
