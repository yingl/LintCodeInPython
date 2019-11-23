# coding: utf-8

class Solution:
    # @param nums: a list of integer
    # @return: return nothing (void), do not return anything, modify nums in-place instead
    def nextPermutation(self, nums):  # 不要被题目内容忽悠了，其实和next-permutation一模一样。
        # write your code here
        i = len(nums) - 2
        while i >= 0:
            if nums[i] < nums[i + 1]:
                break
            i -= 1
        if i < 0:
            nums.reverse()
            return nums
        min_val = nums[i + 1]
        min_pos = i + 1
        for j in xrange(i + 2, len(nums)):
            if (nums[j] < min_val) and (nums[j] > nums[i]):
                min_val, min_pos = nums[j], j
        nums[i], nums[min_pos] = nums[min_pos], nums[i]
        partial_list = nums[i + 1:]
        partial_list.sort()
        nums[i + 1:] = partial_list
        return nums

# medium: http://lintcode.com/zh-cn/problem/next-permutation-ii/
