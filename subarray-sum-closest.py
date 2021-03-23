class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySumClosest(self, nums):
        # write your code here
        if not nums:
            return []
        sums = []
        tmp = 0
        for i in range(len(nums)):
            tmp += nums[i]
            sums.append([tmp, i])
        sums.sort()
        diff = abs(sums[0][0])
        ret = [0, sums[0][1]]
        for i in range(1, len(sums)):
            if abs(sums[i][0] - sums[i - 1][0]) < diff:
                diff = abs(sums[i][0] - sums[i - 1][0])
                ret[0] = min(sums[i][1], sums[i - 1][1]) + 1
                ret[1] = max(sums[i][1], sums[i - 1][1])
        return ret

# medium: http://lintcode.com/problem/subarray-sum-closest
