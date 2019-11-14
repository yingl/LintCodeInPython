# coding: utf-8

class Solution:
    # @param {int[]} nums n non-negative integer array
    # @return {str} a string
    def minNumber(self, nums):
        # Write your code here
        # 修改一下排序规则就可以了
        nums.sort(lambda x, y: cmp(str(x) + str(y), str(y) + str(x)))
        return str(int(''.join(str(i) for i in nums)))  # 把前面的0都去掉

# medium: http://lintcode.com/zh-cn/problem/reorder-array-to-construct-the-minimum-number/
