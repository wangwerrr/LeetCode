from collections import deque

class Solution:
    """
    @param rooms: m x n 2D grid
    @return: nothing
    """
    def wallsAndGates(self, rooms):
        
        INF = 2147483647
        que = deque([(i, j) for i, row in enumerate(rooms) for j, r in enumerate(row) if not r])
        while que:
            i, j = que.popleft()
            for x, y in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= x < len(rooms) and 0 <= y < len(rooms[0]) and rooms[x][y] == INF:
                    rooms[x][y] = rooms[i][j] + 1
                    que.append((x, y))
