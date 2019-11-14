# coding: utf-8

class Solution:
    """
    @param nums: The integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    def longestIncreasingSubsequence(self, nums):
        # write your code here
        ret = 0
        if nums:
            caches = [0] * len(nums)  # 到当前位置最长子序列长度
            caches[0] = 1
            for i in xrange(1, len(nums)):
                _len = 0
                for j in xrange(i):
                    if nums[j] < nums[i]:
                        _len = max(caches[j], _len)
                caches[i] = _len + 1
                ret = max(caches[i], ret)
        return ret

# medium: http://lintcode.com/zh-cn/problem/longest-increasing-subsequence/
