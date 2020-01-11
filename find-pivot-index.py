class Solution:
    """
    @param nums: an array
    @return: the "pivot" index of this array
    """
    def pivotIndex(self, nums):
        # Write your code here
        nums_sum = sum(nums)
        left_sum, right_sum = 0, 0
        for i in range(len(nums)):
            if i == 0:
                left_sum = 0
            else:
                left_sum += nums[i - 1]
            right_sum = nums_sum - nums[i] - left_sum
            if left_sum == right_sum:
                return i
        return -1

# easy: https://www.lintcode.com/problem/find-pivot-index/
