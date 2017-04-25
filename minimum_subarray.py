# coding: utf-8

class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        # write your code here
        plus_min = 2147483647
        i, sum_min, sub_sum_min = 0, 1, 0
        while i < len(nums):
            sub_sum_min += nums[i]
            if sub_sum_min < 0:
                if sub_sum_min < sum_min:
                    sum_min = sub_sum_min
            else:
                sub_sum_min = 0
            if (nums[i] >= 0) and (nums[i] < plus_min):
                plus_min = nums[i]
            i += 1
        if sum_min < 0:
            return sum_min
        return plus_min

# easy: http://lintcode.com/zh-cn/problem/minimum-subarray/
