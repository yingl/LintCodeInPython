"""
Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
"""

class Solution:
    """
    @param l1: top-left coordinate of first rectangle
    @param r1: bottom-right coordinate of first rectangle
    @param l2: top-left coordinate of second rectangle
    @param r2: bottom-right coordinate of second rectangle
    @return: true if they are overlap or false
    """
    def doOverlap(self, l1, r1, l2, r2):
        # write your code here
        # 不重叠的规则比较好写，xy轴同时不交叉即可。
        if (((l2.x > r1.x) or (r2.x < l1.x)) \
            or ((r2.y > l1.y) or (l2.y < r1.y))):
            return False
        return True

# https://www.lintcode.com/problem/rectangle-overlap/
