class Solution:
    """
    @param M: a 2D integer matrix
    @return: a 2D integer matrix
    """
    def imageSmoother(self, M):
        # Write your code here
        ret = []
        for row in range(len(M)):
            ret.append([])
            for col in range(len(M[0])):
                ret[-1].append(self.smoother(M, row, col))
        return ret

    def smoother(self, M, row, col):
        val = M[row][col]
        count = 1
        if ((row - 1) >= 0) and ((col - 1) >= 0): # left-upper
            val += M[row - 1][col - 1]
            count += 1
        if ((row - 1) >= 0): # upper
            val += M[row - 1][col]
            count += 1
        if ((row - 1) >= 0) and ((col + 1) < len(M[0])): # right-upper
            val += M[row - 1][col + 1]
            count += 1
        if ((col - 1) >= 0): # left
            val += M[row][col - 1]
            count += 1
        if ((col + 1) < len(M[0])): # right
            val += M[row][col + 1]
            count += 1
        if ((row + 1) < len(M)) and ((col - 1) >= 0): # left-down
            val += M[row + 1][col - 1]
            count += 1
        if ((row + 1) < len(M)): # down
            val += M[row + 1][col]
            count += 1
        if ((row + 1) < len(M)) and ((col + 1) < len(M[0])): # right-down
            val += M[row + 1][col + 1]
            count += 1
        return int(val / count)
        
# easy: https://www.lintcode.com/problem/image-smoother/
