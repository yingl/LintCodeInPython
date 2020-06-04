class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def findLHS(self, nums):
        # write your code here
        # 先排序，最大/最小值之差为1，所以第一个元素定了，后面的值也就限制了。
        ret = 0
        nums.sort()
        start, new_start = 0, 0
        for i in range(1, len(nums)):
            if (nums[i] - nums[start]) > 1: # 判断是否在约束范围
                start = new_start
            if nums[i] != nums[i - 1]:
                new_start = i # 有机会作为新的开始，因为如果相等就不可能有更长的子序列。
            if (nums[i] - nums[start]) == 1: # [start, i]满足和谐子序列要求
                ret = max(ret, i - start + 1)
        return ret
        
# easy: https://www.lintcode.com/problem/longest-harmonious-subsequence/
