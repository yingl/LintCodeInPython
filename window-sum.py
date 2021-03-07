class Solution:
    """
    @param nums: a list of integers.
    @param k: length of window.
    @return: the sum of the element inside the window at each moving.
    """
    def winSum(self, nums, k):
        # write your code here
        ret = []
        if nums:
            ret.append(0)
            for i in range(k):
                ret[0] += nums[i]
            for i in range(1, len(nums) - k + 1):
                ret.append(ret[i - 1] - nums[i - 1] + nums[i + k - 1])
        return ret;

# easy: https://www.lintcode.com/problem/window-sum/
