class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.cache = [0]
        for i in nums:
            self.cache.append(i + self.cache[-1])
        
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.cache[j + 1] - self.cache[i]
        
# easy: https://www.lintcode.com/problem/range-sum-query-immutable/
