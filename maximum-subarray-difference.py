# coding: utf-8

class Solution:
    """
    @param nums: A list of integers
    @return: An integer indicate the value of maximum difference between two
             Subarrays
    """
    def maxDiffSubArrays(self, nums):
        # write your code here
        '''
        记录从0到i的最大值和从n - 1到i的最小值，计算最大差。
        因为比较大的部分可能出现在前半段，也有可能出现在后半段，
        所以反转数组再计算一遍。
        '''
        ret = self._maxDiffSubArrays(nums)
        nums.reverse()
        return max(ret, self._maxDiffSubArrays(nums))

    def _maxDiffSubArrays(self, nums):
        left, right = [0] * len(nums), [0] * len(nums)
        _sum = 0
        max_sum, min_sum = -2147483648, 2147483647
        for i in xrange(len(nums)):
            _sum += nums[i]
            max_sum = max(_sum, max_sum)
            if _sum < 0:
                _sum = 0
            left[i] = max_sum
        _sum = 0
        for i in xrange(len(nums) - 1, -1, -1):
            _sum += nums[i]
            min_sum = min(_sum, min_sum)
            if _sum > 0:
                _sum = 0
            right[i] = min_sum
        ret = 0
        for i in xrange(1, len(nums)):
            ret = max(ret, abs(left[i - 1] - right[i]))
        return ret

# medium: http://lintcode.com/zh-cn/problem/maximum-subarray-difference/
