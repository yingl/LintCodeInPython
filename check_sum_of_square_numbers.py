# coding: utf-8

class Solution:
    """
    @param: : the given number
    @return: whether whether there're two integers
    """
    def checkSumOfSquareNumbers(self, num):
        # write your code here
        if num < 0:
            return False
        import math
        upper = int(math.sqrt(num))
        for i in range(upper + 1):
            start, end = i, upper # 二分法的干活
            while start <= end:
                j = int((start + end) / 2)
                s = i * i + j * j
                if s == num:
                    return True
                elif s > num:
                    end = j - 1
                else:
                    start = j + 1
        return False
        
# easy: http://lintcode.com/zh-cn/problem/check-sum-of-square-numbers/
