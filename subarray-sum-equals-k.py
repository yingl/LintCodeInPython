class Solution:
    """
    @param nums: a list of integer
    @param k: an integer
    @return: return an integer, denote the number of continuous subarrays whose sum equals to k
    """
    def subarraySumEqualsK(self, nums, k):
        # write your code here
        # 遍历数组nums，计算从第0个元素到当前元素的和，用哈希表保存出现过的累积和sum的次数。
        # 如果sum - k在哈希表中出现过，则代表从当前下标i往前有连续的子数组的和为k！！！
        ret = 0
        di = {0:1}
        _sum = 0
        for i in nums:
            _sum += i
            if (_sum - k) in di:
                ret += di[_sum - k]
            if _sum in di:
                di[_sum] += 1
            else:
                di[_sum] = 1
        return ret

# easy: https://www.lintcode.com/problem/subarray-sum-equals-k/
