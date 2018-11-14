class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        n = len(A)
        m = len(A[0])
        k = len(B[0])

        C = [[0 for _ in xrange(k)] for i in xrange(n)]
        
        non_zero_col_B = [[l for l in range(k) if B[j][l] != 0 ] for j in range(m)]
        print non_zero_col_B
        
        for i in xrange(n):
            for j in xrange(m):
                if A[i][j] != 0:
                    for l in non_zero_col_B[j]:
                        C[i][l] += A[i][j] * B[j][l]
        return C
