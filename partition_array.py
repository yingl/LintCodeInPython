# coding: utf-8

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: As description
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        # write your code here
        # you should partition the nums by k
        # and return the partition index as description
        if not nums:
            return 0
        start, end = 0, len(nums) - 1
        while start < end:
            if nums[start] < k:
                start += 1
            elif nums[end] >= k:
                end -= 1
            else:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        return start + 1 if nums[start] < k else start

# medium: http://lintcode.com/zh-cn/problem/partition-array/
