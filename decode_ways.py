# coding: utf-8

class Solution:
    # @param {string} s a string,  encoded message
    # @return {int} an integer, the number of ways decoding
    def numDecodings(self, s):
        # Write your code here
        '''
        从后往前找，对于第i位的情况：
        1. 等于第i + 1位的组合。
        2. 如果s[i][i + 1]在10到26的范围内，再加上第i + 2位的组合。
        '''
        if not s:
            return 0
        cached_nums = [1 for i in xrange(len(s) + 1)] # 多一格方便处理倒数第二位的情况
        for i in xrange(len(s) - 1, -1, -1):
            if s[i] == '0':
                cached_nums[i] = 0
            else:
                cached_nums[i] = cached_nums[i + 1]
            if i < len(s) - 1:
                if (s[i] == '1') or ((s[i] == '2') and (s[i + 1] <= '6')):
                    cached_nums[i] += cached_nums[i + 2]
        return cached_nums[0]

# medium: http://lintcode.com/zh-cn/problem/decode-ways/
