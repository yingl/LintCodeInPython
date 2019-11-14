# coding: utf-8

class Solution:
    # @param {int[]} nums an integer array
    # @return nothing, do this in-place
    def moveZeroes(self, nums):
        # Write your code here
        zeros = 0
        for i in xrange(0, len(nums)):
            nums[i - zeros] = nums[i]
            if nums[i] == 0:
                zeros += 1
        for i in xrange(zeros):
            nums[len(nums) - i - 1] = 0

# easy: http://lintcode.com/zh-cn/problem/move-zeroes/
