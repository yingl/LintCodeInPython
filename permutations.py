# coding: utf-8

class Solution:
    """
    @param nums: A list of Integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        # write your code here
        # 非递归实现请参考next_permutation.py
        self.ret = []
        if nums:
            self._permute(nums, 0)
        return self.ret

    def _permute(self, nums, start):
        if start == len(nums):
            self.ret.append(nums[:])  # 这里一定要复制对象！
        else:
            for i in xrange(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                self._permute(nums, start + 1)
                nums[i], nums[start] = nums[start], nums[i]

# medium: http://lintcode.com/zh-cn/problem/permutations/
