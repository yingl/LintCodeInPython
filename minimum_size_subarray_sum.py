# coding: utf-8

class Solution:
     # @param nums: a list of integers
     # @param s: an integer
     # @return: an integer representing the minimum size of subarray
    def minimumSize(self, nums, s):
        # write your code here
        # 两个指针一前一后，先找到大于s，在移动后面使得小于s，再移动前面。。。
        ret = 2147483647
        if nums:
            slow, fast = 0, 0
            _sum = 0
            while fast < len(nums):
                while (fast < len(nums)) and (_sum < s):
                    _sum += nums[fast]
                    fast += 1
                while _sum >= s:
                    ret = min(fast - slow, ret)
                    _sum -= nums[slow]
                    slow += 1
        return -1 if ret == 2147483647 else ret

    # TODO: nLog(n)复杂度的算法

# medium: http://lintcode.com/zh-cn/problem/minimum-size-subarray-sum/
