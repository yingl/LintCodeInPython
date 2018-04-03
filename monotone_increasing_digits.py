from functools import reduce

class Solution:
    """
    @param num: a non-negative integer N
    @return: the largest number that is less than or equal to N with monotone increasing digits.
    """
    def monotoneDigits(self, num):
        # write your code here
        digits = list(map(int, list(str(num))))
        digits_len = len(digits)
        j = digits_len
        for i in range(digits_len - 1, 0, -1):
            if digits[i] > digits[i - 1]:
                continue
            digits[i - 1] -= 1
            j = i
        for i in range(j, digits_len):
            digits[i] = 9
        return reduce(lambda x, y: x * 10 + y, digits)
