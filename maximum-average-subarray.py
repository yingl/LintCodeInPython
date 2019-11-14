class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the maximum average value
    """
    def findMaxAverage(self, nums, k):
        # Write your code here
        ret = sum(nums[:k])
        avg = ret
        i = 1
        while i < len(nums) - k + 1:
            avg = avg - nums[i - 1] + nums[i + k - 1]
            if avg > ret:
                ret = avg
            i += 1
        return ret / k
        
# easy: https://www.lintcode.com/problem/maximum-average-subarray/
