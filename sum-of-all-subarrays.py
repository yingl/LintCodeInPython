def do_sum(nums, idx, ret, _sum): # _sum记录子数组的和
    if idx >= len(nums):
        return
    _sum += nums[idx]
    ret[0] += _sum
    do_sum(nums, idx + 1, ret, _sum)

class Solution:
    """
    @param nums: a Integer list
    @return: return the sum of subarrays
    """
    def SubArraySum(self, nums):
        # write your code here
        ret = [0]
        for i in range(len(nums)):
            do_sum(nums, i, ret, 0)
        return ret[0]

# easy: https://www.lintcode.com/problem/sum-of-all-subarrays/
