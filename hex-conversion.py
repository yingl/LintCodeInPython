class Solution:
    """
    @param n: a decimal number
    @param k: a Integer represent base-k
    @return: a base-k number
    """
    def hexConversion(self, n, k):
        # write your code here
        chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
        digits = []
        while n >= k:
            digits.append(chars[n % k])
            n = int(n / k)
        digits.append(chars[n])
        return ''.join(digits[::-1])

# easy: https://www.lintcode.com/problem/hex-conversion/
