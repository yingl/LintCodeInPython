class Solution:
    """
    @param nums: an array
    @return: the shortest subarray's length
    """
    def findUnsortedSubarray(self, nums):
        # Write your code here
        # 有个有趣的做法，排序都可以省了。。。
        # 1. 找到最右边的比之前max小的元素
        # 2. 找到最左边的比之后min大的元素
        _max, _min = nums[0], nums[-1]
        l, r = -1, -2
        for i in range(1, len(nums)):
            _max = max(_max, nums[i])
            _min = min(_min, nums[len(nums) - i - 1])
            if _max != nums[i]:
                r = i
            if _min != nums[len(nums) - i - 1]:
                l = len(nums) - i - 1
        return r - l + 1
        
# easy: https://www.lintcode.com/problem/shortest-unsorted-continuous-subarray/
