# coding: utf-8

class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        # write your code here
        for i in xrange(len(nums)):
            j = i
            while (nums[j] < len(nums)) and (nums[j] != j):
                k = nums[j]
                nums[j], nums[k] = nums[k], nums[j]
        ret = 0
        for i in xrange(len(nums)):
            if nums[i] != i:
                break
            ret += 1
        return ret

# medium: http://lintcode.com/zh-cn/problem/find-the-missing-number/
