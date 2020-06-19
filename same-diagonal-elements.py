class Solution:
    """
    @param matrix: a matrix
    @return: return true if same.
    """
    def judgeSame(self, matrix):
        # write your code here.
        # 1st row, then 1st column.
        n = len(matrix)
        for i in range(n):
            r, c = 1, i + 1
            while (r < n) and (c < n):
                if matrix[r][c] != matrix[0][i]:
                    return False
                r += 1
                c += 1
        for i in range(1, n):
            r, c = i + 1, 1
            while (r < n) and (c < n):
                if matrix[r][c] != matrix[i][0]:
                    return False
                r += 1
                c += 1
        return True
        
# easy: https://www.lintcode.com/problem/same-diagonal-elements/
