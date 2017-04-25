# coding: utf-8

class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.
        import ctypes
        a = ctypes.c_int32(a).value
        b = ctypes.c_int32(b).value
        while b != 0:
            carry = ctypes.c_int32(a & b).value
            a = ctypes.c_int32(a ^ b).value
            b = ctypes.c_int32(carry << 1).value
        return a

# easy: http://lintcode.com/zh-cn/problem/a-b-problem/
