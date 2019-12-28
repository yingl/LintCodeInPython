class Solution:
    """
    @param rowIndex: a non-negative index
    @return: the kth index row of the Pascal's triangle
    """
    def getRow(self, rowIndex):
        # write your code here
        rows = [[1, 1], []]
        idx = 0
        for i in range(1, rowIndex):
            idx_next = 1 - idx
            rows[idx_next] = [1] * (i + 2)
            for j in range(1, i + 1):
                rows[idx_next][j] = rows[idx][j - 1] + rows[idx][j]
            idx, idx_next = idx_next, idx
        return rows[idx]

# easy: https://www.lintcode.com/problem/pascals-triangle-ii/
