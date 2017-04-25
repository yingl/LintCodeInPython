# coding: utf-8

class Solution:
    def strStr(self, source, target):
        if (source is None) or (target is None):
            return -1
        for i in xrange(len(source) - len(target) + 1):
            if source[i:i + len(target)] == target:
                return i
        return -1

# easy: http://lintcode.com/zh-cn/problem/strstr/
