# coding: utf-8

class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        # write your code here
        ret = []
        i = 0
        while i < len(intervals):
            if intervals[i].start > newInterval.start:
                break
            i += 1
        if i > 0:
            ret[0:i] = intervals[0:i]
            intervals[i - 1] = newInterval
            start = i - 1
        else:
            ret.append(newInterval)
            start = 0
        for i in xrange(start, len(intervals)):
            if (intervals[i].start >= ret[-1].start) and \
                    (intervals[i].start <= ret[-1].end):
                if intervals[i].end > ret[-1].end:
                    ret[-1].end = intervals[i].end
            else:
                ret.append(intervals[i])
        return ret

# easy: http://lintcode.com/problem/insert-interval
