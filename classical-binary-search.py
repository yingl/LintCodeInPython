# coding: utf-8

class Solution:
    # @param {int[]} A an integer array sorted in ascending order
    # @param {int} target an integer
    # @return {int} an integer
    def findPosition(self, A, target):
        # Write your code here
        start, end = 0, len(A) - 1
        while start <= end:
            mid = (start + end) / 2
            if A[mid] == target:
                return mid
            elif A[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return -1

# easy: http://lintcode.com/zh-cn/problem/classical-binary-search/
