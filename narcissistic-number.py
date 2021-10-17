class Solution:
    """
    @param n: The number of digits
    @return: All narcissistic numbers with n digits
    """
    def getNarcissisticNumbers(self, n):
        # write your code here
        ret = []
        if n == 1:
            ret.append(0)
        for i in range(pow(10, n - 1), pow(10, n)):
            _i = i
            s = 0
            while i > 0:
                s += pow(i % 10, n)
                i = int(i / 10)
            if s == _i:
                ret.append(s)
        return ret
      
# easy: https://www.lintcode.com/problem/147/description
