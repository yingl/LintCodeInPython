import math

class Solution:
    """
    @param nums: an array of integers
    @param threshold: an integer
    @return: return the smallest divisor
    """
    def smallestDivisor(self, nums, threshold):
        # write your code here
        ret = 0
        min_value = sum(nums)
        l, r = 1, max(nums)
        while l <= r:
            mid = int((l + r) / 2)
            if self.check(nums, mid, threshold):
                r = mid - 1
                ret = mid
            else:
                l = mid + 1
        return ret

    def check(self, nums, div, threshold):
        s = 0
        for i in nums:
            s += math.ceil(i / div)
            if s > threshold:
                return False
        return True
      
# medium: https://www.lintcode.com/problem/1816/
