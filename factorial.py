# coding: utf-8

class Solution:
    """
    @param: : an integer
    @return:  the factorial of n
    """

    def factorial(self, n):
        # write your code here
        # 偷懒做法，实际就是做竖式乘法，Python内部实现了。
        f = 1
        for i in range(2, n + 1):
            f *= i
        return str(f)
        
# hard: http://lintcode.com/zh-cn/problem/factorial/
