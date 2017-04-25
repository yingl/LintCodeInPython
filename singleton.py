# coding: utf-8

class Solution:
    # @return: The same instance of this class every time
    @classmethod
    def getInstance(cls):
        # write your code here
        if not Solution.obj:
            Solution.obj = cls()
        return Solution.obj

    obj = None

# easy: http://lintcode.com/zh-cn/problem/sort-integers-ii/
