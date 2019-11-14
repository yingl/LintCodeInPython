# coding: utf-8

class Solution:
    # @param values: a list of integers
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, values):
        # write your code here
        # score[i]表示从i开始到end能获取的最大值。
        if len(values) <= 2:
            return True
        score = [0] * (len(values) + 1)
        score[-1] = 0
        score[-2] = values[-1]
        score[-3] = values[-2] + values[-1]
        score[-4] = values[-3] + values[-2]
        for i in xrange(len(values) - 4, -1, -1):
            # 拿1个后，对方取1个或2个的情况。
            score[i] = values[i] + min(score[i + 2], score[i + 3])
            # 拿2个后，对方取1个或2个的情况。
            score[i] = max(score[i], values[i] + values[i + 1] + min(score[i + 3], score[i + 4]))
        return True if score[0] > (sum(values) - score[0]) else False

# medium: http://lintcode.com/zh-cn/problem/coins-in-a-line-ii/
