# coding: utf-8

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the sum of max two non-overlapping subarrays
    """
    def maxTwoSubArrays(self, nums):
        # write your code here    
        if not nums:
            return 0
        nums_len = len(nums)
        # 从左边开始到当前位置的连续最大和
        max_sums_from_left = [0] * nums_len
        # 从右边开始到当前位置的连续最大和
        max_sums_from_right = [0] * nums_len
        _sum, _min, _max = 0, 0, nums[0]
        for i in xrange(nums_len):
            _sum += nums[i]
            _max = max(_max, _sum - _min)   # - _min很重要！！！
            _min = min(_min, _sum)
            max_sums_from_left[i] = _max
        _sum, _min, _max = 0, 0, nums[-1]   # _max取右边第一个元素
        for i in xrange(nums_len - 1, -1, -1):
            _sum += nums[i]
            _max = max(_max, _sum - _min)
            _min = min(_min, _sum)
            max_sums_from_right[i] = _max
        _max = max_sums_from_left[0] + max_sums_from_right[-1]
        for i in xrange(nums_len - 1):
            _max = max(_max, max_sums_from_left[i] + max_sums_from_right[i + 1])
        return _max

# medium: http://lintcode.com/zh-cn/problem/maximum-subarray-ii/
