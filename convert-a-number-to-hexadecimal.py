class Solution:
    """
    @param num: an integer
    @return: convert the integer to hexadecimal
    """
    def toHex(self, num):
        # Write your code here
        ret = []
        digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', \
                  'a', 'b', 'c', 'd', 'e', 'f']
        if num < 0:
            num += (1 << 32)
        while num > 0:
            v = num % 16
            ret.append(digits[v])
            num = int(num / 16)
        return ''.join(ret[::-1])

# easy: https://www.lintcode.com/problem/convert-a-number-to-hexadecimal/
