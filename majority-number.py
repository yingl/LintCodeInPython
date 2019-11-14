# coding: utf-8

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        # write your code here
        # 借鉴majority_number_ii.py的算法，复杂度降低到O(n)。
        ret, count = 0, 0
        for i in xrange(len(nums)):
            if count == 0:
                ret = nums[i]
                count = 1
            else:
                count = (count + 1) if ret == nums[i] else (count - 1)
        return ret

# easy: http://lintcode.com/zh-cn/problem/majority-number/
