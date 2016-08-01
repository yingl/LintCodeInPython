# -*- coding: utf-8 -*-

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        # write your code here
        # 偷个懒，直接用sort。把sort_integers_ii.py搬过来就OK了。
        colors.sort()