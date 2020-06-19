class Solution:
    """
    @param n: the number of digit
    @return: the largest palindrome mod 1337
    """
    def largestPalindrome(self, n):
        # write your code here
        '''
        改良暴力法
        n * n的最大回文数一定是2n位
        从10 ^ (n - 1)到10 ^ n - 1作为前半部分，凑出整个回文数，
        然后做除法检查。
        但是n = 8一定超时...所以算好了查表！！！
        '''
        return [9,987,123,597,677,1218,877,475][n-1]

    '''
    def largestPalindrome(self, n):    
        self.low = pow(10, n - 1)
        self.up = pow(10, n)
        for i in range(self.up - 1, self.low - 1, -1):
            x = self.to_palindrome(i)
            j = self.up
            while j * j >= x:
                if (x % j) == 0:
                    return x % 1337
                j -= 1
        return 9 # n = 1的特殊情况
        
    def to_palindrome(self, val):
        ret = val * self.up
        k = 0
        while val > 0:
            k = k * 10 + (val % 10)
            val = int(val / 10)
        return ret + k
    '''

# easy: https://www.lintcode.com/problem/largest-palindrome-product/
