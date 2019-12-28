class Solution:
    """
    @param numRows: num of rows
    @return: generate Pascal's triangle
    """
    def generate(self, numRows):
        # write your code here
        ret = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = ret[-1][j - 1] + ret[-1][j]
            ret.append(row)
        return ret
            
# easy: https://www.lintcode.com/problem/pascals-triangle/
