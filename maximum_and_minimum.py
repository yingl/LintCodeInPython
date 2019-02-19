class Solution:
    """
    @param matrix: an input matrix 
    @return: nums[0]: the maximum,nums[1]: the minimum
    """
    def maxAndMin(self, matrix):
        # write your code here
        if not matrix:
            return []
        r = [matrix[0][0], matrix[0][0]]
        for row in matrix:
            for i in row:
                if i > r[0]: # 确保max在前min在后
                    r[0] = i
                elif i < r[1]:
                    r[1] = i
        return r

# easy: https://www.lintcode.com/problem/maximum-and-minimum
