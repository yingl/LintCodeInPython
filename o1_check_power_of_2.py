# -*- coding: utf-8 -*-

class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        # write your code here
        if n == 0:
            return False
        return (n & (n - 1)) == 0