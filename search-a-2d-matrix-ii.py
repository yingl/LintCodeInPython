# coding: utf-8

class Solution:
    """
    @param matrix: An list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicates the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if not matrix:
            return 0
        rows = len(matrix)
        cols = len(matrix[0])
        ret = 0
        i, j = 0, cols - 1  # 从右上角开始搜索
        while (i < rows) and (j >= 0):
            '''
            因为是从右上角开始搜索，所以当前元素如果等于target，
            那么它下面的元素一定大于target，左面的元素一定小于target，
            所以只能向左下方移动一步。同理推出其它两种情况。
            '''
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                ret += 1
                i += 1
                j -= 1
        return ret

# medium: http://lintcode.com/zh-cn/problem/search-a-2d-matrix-ii/
