# ugly but easy to understand version (Jun 29th)

import copy 

class Solution(object):
    
    # Recurse columnly, from left to right. So columns & right rows/diagnals are good. Just check the left rows & left diagnals.
    def isSafe(self, n, board, row, col):
        # left row
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        # left upper diagonal
        for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
            if board[i][j] == 'Q':
                return False
        # left lower diagonal
        for i,j in zip(range(row,n,1), range(col,-1,-1)):
            if board[i][j] == 'Q':
                return False
        return True   

    # solveNQUtil() places queen for each column
    def solveNQUtil(self, n, board, col, res):
        # base case: If all queens are placed, append to res & return
        if col >= n:
            # res.append(board) is wrong. board will change afterwards
            board_copy = copy.deepcopy(board)
            res.append(board_copy)
            return 

        # Consider every row(i) of this col: only when isSafe(), place the queen at this row
        for i in range(n):
            if self.isSafe(n, board, i, col):
                board[i][col] = 'Q'
                self.solveNQUtil(n, board, col+1, res) 
                board[i][col] = '.' # backtracking
                
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = [['.' for i in range(n)] for j in range(n)]
        # board = [['.'] * n] * n is WRONG. '* n' is not deep copy. shoud not use it to initialize board.
        res = []
        self.solveNQUtil(n, board, 0, res)
        res = [[''.join(row) for row in board] for board in res]
        return res
        
    
