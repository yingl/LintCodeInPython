# coding: utf-8

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        # write your code here
        ret = []
        intervals.sort(key = lambda x: x.start)
        tmp = None
        for interval in intervals:
            if not tmp:
                tmp = interval
            else:
                if (interval.start >= tmp.start) and (interval.start <= tmp.end):
                    if interval.end > tmp.end:
                        tmp.end = interval.end
                else:
                    ret.append(tmp)
                    tmp = interval
        if tmp:
            ret.append(tmp)
        return ret

# easy: http://lintcode.com/zh-cn/problem/merge-intervals/
