class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # 上下翻转
        for r in range(n/2):
            for c in range(n):
                matrix[r][c], matrix[n-1-r][c] =  matrix[n-1-r][c], matrix[r][c]
                
        # x,y 交换
        for r in range(n):    
            for c in range(r, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
  
        # notice the num range(): if n, then swap twice, back to original
        # note that the direction of coordinators are down,right.
