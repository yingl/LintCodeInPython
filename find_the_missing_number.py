# -*- coding: utf-8 -*-

class Solution:
    # @param nums: a list of integers
    # @return: an integer
    def findMissing(self, nums):
        # write your code here
        ret = len(nums) * (len(nums) + 1) / 2
        for num in nums:
            ret -= num
        return ret