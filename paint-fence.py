# coding: utf-8

class Solution:
    # @param {int} n non-negative integer, n posts
    # @param {int} k non-negative integer, k colors
    # @return {int} an integer, the total number of ways
    def numWays(self, n, k):
        # Write your code here
        # The question is wrong, please google the correct one.
        '''
        题目描述有错，真实意思是必须保证最多只有两个相邻的柱子颜色相同！！！
        初始条件为[k, k ^ 2]
        如果第i个柱子的颜色和第i - 1个一样，就必需和第i - 2个不一样。
        如果第i个柱子的颜色和第i - 1个不一样，颜色的取值和第i个就没关系了。
        '''
        if (n == 0) or (k == 0):
            return 0
        plans = [k, k * k]
        if n == 1:
            return plans[0]
        else:
            i = 2
            while i < n:
                tmp = plans[-1] * (k - 1) + plans[-2] * (k - 1)
                plans[0] = plans[1]
                plans[1] = tmp
                i += 1
            return plans[1]

# easy: http://lintcode.com/zh-cn/problem/paint-fence/
