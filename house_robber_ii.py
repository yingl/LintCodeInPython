# coding: utf-8

class Solution:
    # @param nums: A list of non-negative integers.
    # return: an integer
    def houseRobber2(self, nums):
        # write your code here
        '''
        与打劫房屋相比：
        1. 如果我抢了第1间，最后一间就不能抢。
        2. 如果第一间不抢，就可以抢最后一间。
        '''
        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        else:
            ret_1, ret_2 = 0, 0
            # 场景1
            caches = nums[:]
            caches[1] = max(caches[0], caches[1])
            for i in xrange(2, len(nums) - 1):
                caches[i] = max(caches[i] + caches[i - 2], caches[i - 1])
            ret_1 = caches[-2]
            caches = nums[:]
            caches[0] = 0
            for i in xrange(2, len(nums)):
                caches[i] = max(caches[i] + caches[i - 2], caches[i - 1])
            ret_2 = caches[-1]
            return max(ret_1, ret_2)

# medium: http://lintcode.com/zh-cn/problem/house-robber-ii/
