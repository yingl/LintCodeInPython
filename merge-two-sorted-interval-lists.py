"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # write your code here
        ret = []
        li = list1 + list2
        li.sort(key=lambda x: x.start) # 偷个懒，正常做法是利用已排序特性。
        for r in li:
            if not ret:
                ret.append(r)
            else:
                if (r.start >= ret[-1].start) and (r.start <= ret[-1].end):
                    ret[-1].end = max(r.end, ret[-1].end)
                else:
                    ret.append(r)
        return ret

# easy: https://www.lintcode.com/problem/merge-two-sorted-interval-lists/
