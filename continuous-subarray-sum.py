# coding: utf-8

class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        # Write your code here
        _max = A[0]
        _sum = 0
        start, end = 0, 0
        curr_start = 0  # 记录子数组开始位置
        for i in xrange(len(A)):
            _sum += A[i]
            if _sum > _max:
                _max = _sum
                start, end = curr_start, i
            if _sum < 0:
                curr_start = i + 1
                _sum = 0
        return [start, end]

# medium: http://lintcode.com/zh-cn/problem/continuous-subarray-sum/
