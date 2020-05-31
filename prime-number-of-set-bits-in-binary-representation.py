class Solution:
    """
    @param L: an integer
    @param R: an integer
    @return: the count of numbers in the range [L, R] having a prime number of set bits in their binary representation
    """
    def countPrimeSetBits(self, L, R):
        # Write your code here
        ret = 0
        for i in range(L, R + 1):
            c = self.count_1(i)
            if self.is_prime(c):
                ret += 1
        return ret
        
    def count_1(self, n):
        ret = 0
        while (n > 0):
            if (n % 2) == 1:
                ret += 1
            n = int(n / 2)
        return ret

    def is_prime(self, n):
        if n == 1:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if (i * i) <= n:
                    if (n % i) == 0:
                        return False
            return True
            
# easy: https://www.lintcode.com/problem/prime-number-of-set-bits-in-binary-representation/
