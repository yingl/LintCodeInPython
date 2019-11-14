# coding: utf-8

class Solution:
    #@param n: Given a decimal number that is passed in as a string
    #@return: A string
    def binaryRepresentation(self, n):
        # write you code here
        bin_val = []
        int_digits = 0
        for i in xrange(len(n)):
            if n[i] != '.':
                int_digits += 1
            else:
                break
        int_part = self.int(n, 0, int_digits)
        float_part = self.int(n, int_digits + 1, len(n))
        if int_part == 0:
            bin_val.append('0')
        else:
            while int_part != 0:
                bin_val.append('1' if (int_part % 2) == 1 else '0')
                int_part /= 2
            bin_val.reverse()
        if float_part > 0:
            bin_val.append('.')
            bin_float_digits = 0
            adjust = 0
            while ((int_digits + 1+ adjust) < len(n)) and (n[int_digits + 1 + adjust] == '0'):
                adjust += 1
            round_up = self.roundUp(float_part, adjust)
            while float_part > 0:
                float_part_2 = float_part * 2
                bin_val.append('1' if float_part_2 >= round_up else '0')
                bin_float_digits += 1
                if bin_float_digits > 32:
                    return 'ERROR'
                float_part = (float_part_2 - round_up) if float_part_2 >= round_up else float_part_2
        return ''.join(bin_val)

    def int(self, number, start, end):  # 字符串转整数
        ret = 0
        while start < end:
            ret = ret * 10 + int(number[start])
            start += 1
        return ret

    def roundUp(self, val, adjust): # 向上取整
        ret = 1
        while val > 0:
            ret *= 10
            val /= 10
        i = 0
        while i < adjust:
            ret *= 10
            i += 1
        return ret

# hard: http://lintcode.com/zh-cn/problem/binary-representation/
