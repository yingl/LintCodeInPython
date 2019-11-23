# coding: utf-8

class Solution:
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        # write your code here
        if (not matrix) or (target < matrix[0][0]) or (target > matrix[-1][-1]):
            return False
        start, end = 0, len(matrix)
        while start < end:
            mid = (start + end) / 2
            if matrix[mid][0] < target:
                start = mid + 1
            elif matrix[mid][0] > target:
                end = mid # end是开区间，所以不用减1。
            else:
                break
        if matrix[mid][0] > target: # 确保所有A[mid][0]小于等于target
            mid -= 1
        i = mid
        start, end = 0, len(matrix[0])
        while start < end:
            mid = (start + end) / 2
            if matrix[i][mid] < target:
                start = mid + 1
            elif matrix[i][mid] > target:
                end = mid
            else:
                return True
        return False

# easy: http://lintcode.com/zh-cn/problem/search-a-2d-matrix/
