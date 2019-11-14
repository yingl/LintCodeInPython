# coding: utf-8

class Solution:
    """
  @param A : An integer array
  @return : An integer
    """
    def singleNumberII(self, A):
        # write your code here
        ret = 0
        tmp = 0
        for num in A:
            ret = (ret ^ num) & (~tmp)
            tmp = (tmp ^ num) & (~ret)
        return ret

# medium: http://lintcode.com/zh-cn/problem/single-number-ii/
