# coding: utf-8

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        # write your code here
        i, _sum, sum_max = 0, 0, -2147483648
        while i < len(nums):
            _sum += nums[i]
            if _sum > sum_max:
                sum_max = _sum
            if _sum < 0:
                _sum = 0
            i += 1
        return sum_max

# easy: http://lintcode.com/zh-cn/problem/maximum-subarray/
