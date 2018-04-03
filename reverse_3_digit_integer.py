class Solution:
    """
    @param number: A 3-digit number.
    @return: Reversed number.
    """
    def reverseInteger(self, number):
        # write your code here
        ret = 0
        while number != 0:
            ret = ret * 10 + (number % 10)
            number /= 10
        return ret

# entry: http://www.lintcode.com/zh-cn/problem/reverse-3-digit-integer/
