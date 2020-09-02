class Solution:
    """
    @param X: a integer
    @param Y: a integer
    @param nums: a list of integer
    @return: return the maximum index of largest prefix
    """
    def LongestPrefix(self, X, Y, nums):
        # write your code here
        ret = -1
        cx = 0
        cy = 0
        for i in range(len(nums)):
            v = nums[i]
            if v == X:
                cx += 1
            if v == Y:
                cy += 1
            if (cx > 0) and (cx == cy):
                ret = i
        return ret

# easy: https://www.lintcode.com/problem/longest-prefix-of-array/
