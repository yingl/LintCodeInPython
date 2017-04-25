# coding: utf-8

class Solution(object):
    """
    @param {int[]} nums a list of integer
    @return nothing, modify nums in-place instead
    """
    def wiggleSort(self, nums):
        # Write your code here
        '''
        根据排序条件的出nums[i * 2 + 1]大于nums[i * 2]和nums[i * 2 + 2]，
        所以对于以下任意一种情况必须交换位置：
        1. i为奇数且nums[i]小于nums[i - 1]
        2. i为偶数且nums[i - 1]小于nums[i]
        因为循环从1开始，所以当第2种情况出现时，一定nums[i - 1]大于等于nums[i - 2]。
        '''
        for i in xrange(1, len(nums)):
            if ((i % 2 == 1) and (nums[i] < nums[i - 1])) or \
                ((i % 2 == 0) and (nums[i] > nums[i - 1])):
                nums[i], nums[i - 1] = nums[i- 1], nums[i]

# medium: http://lintcode.com/zh-cn/problem/wiggle-sort/
