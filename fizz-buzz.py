# coding: utf-8

class Solution:
    """
    @param n: An integer as description
    @return: A list of strings.
    For example, if n = 7, your code should return
        ["1", "2", "fizz", "4", "buzz", "fizz", "7"]
    """
    def fizzBuzz(self, n):
        ret = []
        for i in range(1, n+1):
            if i % 15 == 0:
                ret.append("fizz buzz")
            elif i % 5 == 0:
                ret.append("buzz")
            elif i % 3 == 0:
                ret.append("fizz")
            else:
                ret.append(str(i))
        return ret

# easy: http://lintcode.com/zh-cn/problem/fizz-buzz/
