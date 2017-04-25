# coding: utf-8

class Solution:
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        # write your code here
        if not nums:
            return -1
        return self._median(nums, 0, len(nums) - 1, (len(nums) + 1) / 2)

    def _median(self, nums, begin, end, pos):
        if begin >= end:
            return nums[begin]
        index = begin
        for i in xrange(begin + 1, end + 1):
            if nums[i] < nums[begin]:
                index += 1
                nums[i], nums[index] = nums[index], nums[i]
        nums[begin], nums[index] = nums[index], nums[begin]
        if index - begin + 1 == pos:
            return nums[index]
        elif index - begin + 1 > pos:
            return self._median(nums, begin, index - 1, pos)
        else:
            return self._median(nums, index + 1, end, pos - (index - begin + 1))

# easy: http://lintcode.com/zh-cn/problem/median/
