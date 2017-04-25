# coding: utf-8

class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        # write your code here
        if nums[0] < nums[-1]:
            return
        shift = 0
        for i in xrange(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                shift = i + 1
                break
        self.reverse(nums, 0, shift - 1)
        self.reverse(nums, shift, len(nums) - 1)
        self.reverse(nums, 0, len(nums) - 1)

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

# easy: http://lintcode.com/zh-cn/problem/recover-rotated-sorted-array/
