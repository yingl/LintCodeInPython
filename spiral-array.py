class Solution:
    """
    @param n: a Integer
    @return: a spiral array
    """
    def spiralArray(self, n):
        # write your code here
        ret = [[0] * n for i in range(n)]
        row_up, row_down = 0, n
        col_left, col_right = 0, n
        i, size = 1, n * n
        while i <= size:
            for c in range(col_left, col_right): # right
                if i > size:
                    break
                ret[row_up][c] = i
                i += 1
            for r in range(row_up + 1, row_down): # down
                if i > size:
                    break
                ret[r][col_right - 1] = i
                i += 1
            for c in range(col_right - 2, col_left - 1, -1): # left
                if i > size:
                    break
                ret[row_down - 1][c] = i
                i += 1
            for r in range(row_down - 2, row_up, -1): # up
                if i > size:
                    break
                ret[r][col_left] = i
                i += 1
            row_up += 1
            row_down -= 1
            col_left += 1
            col_right -= 1
        return ret

# easy: https://www.lintcode.com/problem/spiral-array/
