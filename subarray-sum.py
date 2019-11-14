# coding: utf-8

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        # write your code here
        for i in xrange(0, len(nums)):
            sum = nums[i]
            if sum == 0:
                return [i, i]
            for j in xrange(i + 1, len(nums)):
                sum += nums[j]
                if sum == 0:
                    return [i, j]

# easy: http://lintcode.com/zh-cn/problem/subarray-sum/
