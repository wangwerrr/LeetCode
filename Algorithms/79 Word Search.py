# ugly and slow version July, 3rd
import numpy as np

class Solution(object):

    def util(self, board, used, word, l, i, j):
        # base case: If all characters are placed, return true
        if l >= len(word):
            return True
        # same letter cell may not be used more than once.
        # consider edges
        if j - 1 >= 0 and board[i][j - 1] == word[l] and used[i][j - 1] == 0:
            used[i][j - 1] = 1
            if self.util(board, used, word, l + 1, i, j - 1) == True:
                return True
            used[i][j - 1] = 0
        # shouldn't use elif!!! or if one is False, it will not enter another condition
        if j + 1 < len(board[0]) and board[i][j + 1] == word[l] and used[i][j + 1] == 0:
            used[i][j + 1] = 1
            if self.util(board, used, word, l + 1, i, j + 1) == True:
                return True
            used[i][j + 1] = 0

        if i - 1 >= 0 and board[i - 1][j] == word[l] and used[i - 1][j] == 0:
            used[i - 1][j] = 1
            if self.util(board, used, word, l + 1, i - 1, j) == True:
                return True
            used[i - 1][j] = 0

        if i + 1 < len(board) and board[i + 1][j] == word[l] and used[i + 1][j] == 0:
            used[i + 1][j] = 1
            if self.util(board, used, word, l + 1, i + 1, j) == True:
                return True
            used[i + 1][j] = 0
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        start = np.where(
            np.array(board) == word[0])  # 2D array, start[0] contains the row idxs, start[1] contains col idxs

        if len(start[0]) == 0 or len(board)*len(board[0])< len(word):
            return False
        
        res = []
        for i, j in zip(start[0], start[1]):
            used = np.zeros((len(board), len(board[0])))
            used[i][j] = 1
            a = self.util(board, used, word, 1, i, j)
            res.append(a)
        return True if True in res else False


            
