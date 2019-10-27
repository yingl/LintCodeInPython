class Solution:
    """
    @param num: the given number
    @return: The base 7 string representation
    """
    def convertToBase7(self, num):
        # Write your code here
        minus = False
        if num < 0:
            num = -num;
            minus = True
        digits = []
        while num >= 7:
            digits.append(num % 7)
            num = int(num / 7)
        digits.append(num)
        k = 1
        ret = 0
        for d in digits:
            ret += d * k
            k *= 10
        if minus:
            return str(-ret)
        return str(ret)
        
# easy: https://www.lintcode.com/problem/base-7/
