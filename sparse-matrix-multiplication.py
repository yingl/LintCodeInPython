class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        # write your code here
        ret = []
        rows_a, cols_a = len(A), len(A[0])
        rows_b, cols_b = len(B), len(B[0])
        for i in range(rows_a):
            di = {}
            row = [0] * cols_b
            for j in range(cols_a):
                if A[i][j] != 0:
                    di[j] = A[i][j]
            for j in range(cols_b):
                for k, v in di.items():
                    row[j] += v * B[k][j]
            ret.append(row)
        return ret

# medium: https://www.lintcode.com/problem/sparse-matrix-multiplication/
