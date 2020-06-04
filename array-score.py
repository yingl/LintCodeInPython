class Solution:
    """
    @param nums: the array to be scored.
    @param k: the requirement of subarray length.
    @param u: if the sum is less than u, get 1 score.
    @param l: if the sum is greater than l, lose 1 score.
    @return: return the sum of scores for every subarray whose length is k.
    """
    def arrayScore(self, nums, k, u, l):
        # write your code here.
        ret = 0
        s = 0
        for i in range(0, k):
            s += nums[i]
        if s < u:
            ret += 1
        if s > l:
            ret -= 1
        for i in range(k, len(nums)):
            s += nums[i] - nums[i - k]
            if s < u:
                ret += 1
            if s > l:
                ret -= 1
        return ret
        
# easy: https://www.lintcode.com/problem/array-score/
