# coding: utf-8

class Solution:
    # @param s, a string
    # @return an integer
    def minCut(self, s):
        # write your code here
        '''
        这里多加一个虚拟元素，表示第i之后的元素最多可以分割几次。
        这个思路类似于在list头部加一个节点。
        statuses则是空间换时间，记录s[i:j + 1]是否回文。
        '''
        ret = [(len(s) - i) for i in xrange(len(s) + 1)]
        statuses = [[False] * len(s) for i in xrange(len(s))]
        for i in xrange(len(s) - 1, -1, -1):
            for j in xrange(i, len(s)):
                '''
                如果以下条件满足，则s[i:j + 1]为回文：
                - s[i] == s[j]
                - ij相邻或者s[i + 1:j]是回文
                '''
                if (s[i] == s[j]) and (((j - i) <= 1) or statuses[i + 1][j - 1]):
                    statuses[i][j] = True
                    '''
                    因为s[i:j + 1是回文]，所以在j这里切一刀可能会是更好的选择。
                    在j这里切下后，因为s[i:j + 1]是回文，所以分割次数是cuts[j + 1] + 1，
                    1是在j这里做的一次切割。
                    '''
                    ret[i] = min(ret[i], ret[j + 1] + 1)
        return ret[0] - 1   # 因为第0个是虚拟元素，所以要扣除一次。

# medium: http://lintcode.com/zh-cn/problem/palindrome-partitioning-ii/
