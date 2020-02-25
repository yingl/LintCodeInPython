class Solution:
    """
    @param nums: an array
    @return: the sum of min(ai, bi) for all i from 1 to n
    """
    def arrayPairSum(self, nums):
        # Write your code here
        ret = 0
        nums.sort()
        for i in range(0, len(nums), 2):
            ret += nums[i]
        return ret

# easy: https://www.lintcode.com/problem/array-partition-i/
