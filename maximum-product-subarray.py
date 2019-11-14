# coding: utf-8

class Solution:
    # @param nums: an integer[]
    # @return: an integer
    def maxProduct(self, nums):
        # write your code here
        # 用两个数组保存到当前的最大最小值，方便负数处理。
        ret = nums[0]
        max_products, min_products = [0] * len(nums), [0] * len(nums)
        max_products[0], min_products[0] = nums[0], nums[0]
        for i in xrange(1, len(nums)):
            max_products[i] = max(max_products[i - 1] * nums[i], \
                                min_products[i - 1] * nums[i], nums[i])
            min_products[i] = min(max_products[i - 1] * nums[i], \
                                min_products[i - 1] * nums[i], nums[i])
            if max_products[i] > ret:
                ret = max_products[i]
        return ret

# medium: http://lintcode.com/zh-cn/problem/maximum-product-subarray/
