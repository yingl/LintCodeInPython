# coding: utf-8

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permuteUnique(self, nums):
        # write your code here
        # 非递归实现请参考next_permutation_ii.py
        nums.sort()
        self.ret = []
        if nums:
            self._permuteUnique(nums, 0)
        return self.ret

    def _permuteUnique(self, nums, start):
        if start == len(nums):
            self.ret.append(nums[:])  # 这里一定要复制对象！
        else:
            for i in xrange(start, len(nums)):
                # 比如[1, 1, 2, 3, 3]，第2个1和3都不用参与交换。
                if (i == start) or ((nums[i] != nums[i - 1]) and (nums[i] != nums[start])):
                    nums[i], nums[start] = nums[start], nums[i]
                    self._permuteUnique(nums, start + 1)
                    nums[i], nums[start] = nums[start], nums[i]

# medium: http://lintcode.com/zh-cn/problem/permutations-ii/
