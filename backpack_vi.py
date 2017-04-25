# coding: utf-8

class Solution:
    # @param {int[]} nums an integer array and all positive numbers, no duplicates
    # @param {int} target an integer
    # @return {int} an integer
    def backPackVI(self, nums, target):
        # Write your code here
        '''
        1. 先对nums排序
        2. 利用result[0]到result[i - 1]的结果迭代出result[i]
        '''
        result = [0] * (target + 1)
        result[0] = 1
        nums.sort()
        for i in xrange(1, target + 1):
            for j in xrange(len(nums)):
                if i >= nums[j]:
                    result[i] += result[i - nums[j]]
        return result[-1]

# medium: http://lintcode.com/zh-cn/problem/backpack-vi/
