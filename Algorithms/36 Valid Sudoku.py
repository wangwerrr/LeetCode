from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        dR = defaultdict(list)
        dC = defaultdict(list)
        dB = defaultdict(list)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                elif board[i][j] in dR[i] or board[i][j] in dC[j] or board[i][j] in dB[(i//3)*3+j//3]:
                    return False
                else:
                    dR[i].append(board[i][j])
                    dC[j].append(board[i][j]) 
                    dB[(i//3)*3+j//3].append(board[i][j])
        return True

# hash tables for Row, Column, Box;
# see how to calculate index of Box: (i//3)*3+j//3
