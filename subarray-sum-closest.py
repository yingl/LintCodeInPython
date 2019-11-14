# coding: utf-8

class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        # 序列a[i + 1]到a[j]的和等于a[0]到a[j]的和减去a[0]到a[i]的和。
        if not nums:
            return []
        sums = []
        tmp = 0
        for i in xrange(len(nums)):
            tmp += nums[i]
            sums.append([tmp, i])
        sums.sort()
        ret = [0, 0]
        diff = 2147483647
        for i in xrange(1, len(sums)):
            if abs(sums[i][0] - sums[i - 1][0]) < diff:
                diff = abs(sums[i][0] - sums[i - 1][0])
                ret = []
                ret.append(min(sums[i][1], sums[i - 1][1]) + 1)
                ret.append(max(sums[i][1], sums[i - 1][1]))
        return ret

# medium: http://lintcode.com/problem/subarray-sum-closest
