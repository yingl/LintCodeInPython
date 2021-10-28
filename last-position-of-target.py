class Solution:
    """
    @param nums: An integer array sorted in ascending order
    @param target: An integer
    @return: An integer
    """
    def lastPosition(self, nums, target):
        # write your code here
        i, j = 0, len(nums) - 1
        while i < (j - 1):
            m = int((i + j) / 2)
            if nums[m] <= target:
                i = m
            else:
                j = m
        if j >= i:
            if nums[j] == target:
                return j
            elif nums[i] == target:
                return i
        return -1

# easy: https://www.lintcode.com/problem/458
