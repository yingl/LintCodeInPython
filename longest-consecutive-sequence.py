# coding: utf-8

class Solution:
    """
    @param num, a list of integer
    @return an integer
    """
    def longestConsecutive(self, num):
        # write your code here
        ret = 0
        if num:
            neighbors = {}  # 记录每个数的相邻数字，+-1。
            for i in num:
                if i not in neighbors:
                    neighbors[i] = 1
            for i in num:
                if neighbors[i]: # 一个数不会出现在2个序列中
                    count = 1
                    # 向上找
                    target = i + 1
                    while target in neighbors:
                        neighbors[target] = None  # 标记该数字已被使用
                        target += 1
                        count += 1
                    # 向下找
                    target = i - 1
                    while target in neighbors:
                        neighbors[target] = None
                        target -= 1
                        count += 1
                    neighbors[i] = None
                    ret = max(count, ret)
        return ret

# medium: http://lintcode.com/zh-cn/problem/longest-consecutive-sequence/
