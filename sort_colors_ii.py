# coding: utf-8

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        # 偷个懒，直接用sort。把sort_integers_ii.py搬过来就OK了。
        # 已知条件包括：包括k种不同的颜色，并按照1到k进行编号。
        # 所以pivot的选取就比较简单了，从1开始往上加。
        colors.sort()

# medium: http://lintcode.com/zh-cn/problem/sort-colors-ii/
