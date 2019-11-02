class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        # Write your code here
        if not matrix:
            return True
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            col = 0
            while row < (rows - 1) and col < (cols - 1):
                if matrix[row][col] != matrix[row + 1][col + 1]:
                    return False
                row += 1
                col += 1
        return True

# easy: https://www.lintcode.com/problem/toeplitz-matrix/
