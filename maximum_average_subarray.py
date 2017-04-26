# coding: utf-8

class Solution:
    # @param {int[]} nums an array with positive and negative numbers
    # @param {int} k an integer
    # @return {double} the maximum average
    def maxAverage(self, nums, k):
        # Write your code here
        # 智商不足，网上搜的答案想了很久才想明白。希望后面的注释有用！
        self.min = sys.maxsize # 平均数的下限，不可能比最小的小。
        self.max = -self.min # 平均数的上限，不可能比最大的大。
        for i in nums:
            if i > self.max:
                self.max = i
            if i < self.min:
                self.min = i
        while (self.max - self.min) > 0.0001:
            mid = float(self.max + self.min) / 2
            if self._search(nums, k, mid): # 调整平均值的上下限
                self.min = mid
            else:
                self.max = mid
        return self.max

    def _search(self, nums, k, mid):
        bar = 0
        sums = [0] * (len(nums) + 1)
        for i in range(1, len(sums)):
            # sums[i] = (nums[0] + ... + nums[i - 1]) - (mid * i)
            sums[i] = sums[i - 1] + nums[i - 1] - mid
            if i >= k:
                '''
                这里首先看sums[i] < 0的情况（因为bar的初始值为0）。
                - 如果sums[i]小于bar，第一次意味着前k个数的平均数都小于mid。
                - 和sums[i - k + 1]比较有什么用？如果比bar小的话，说明在计算连续
                  k个子数组时可以把前面的结果扔掉，完全副作用啊。在程序里体现就
                  是通过min函数调整bar。
                那么后面就容易理解了，如果大于bar，就说明有平均值大于mid。这里的
                精妙之处在于不去试图计算平均值，而是不断收敛平均值上下限的范围。
                '''
                if sums[i] >= bar:
                    return True
                bar = min(bar, sums[i - k + 1])
        return False

# medium: http://lintcode.com/zh-cn/problem/maximum-average-subarray/
