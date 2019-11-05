class Solution:
    """
    @param nums: a integer array
    @return: the index of the largest element
    """
    def dominantIndex(self, nums):
        # Write your code here
        if len(nums) == 1:
            return 0
        t_1, t_2 = nums[0], nums[1]
        p_1, p_2 = 0, 1
        if t_1 < t_2:
            t_1, t_2 = t_2, t_1
            p_1, p_2 = p_2, p_1
        for i in range(2, len(nums)):
            if nums[i] > t_2:
                t_2 = nums[i]
                p_2 = i
                if t_1 < t_2:
                    t_1, t_2 = t_2, t_1
                    p_1, p_2 = p_2, p_1
        if t_1 >= (t_2 * 2):
            return p_1
        else:
            return -1

# easy: https://www.lintcode.com/problem/largest-number-at-least-twice-of-others/
