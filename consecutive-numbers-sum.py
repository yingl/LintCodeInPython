class Solution:
    """
    @param n: an integer
    @return: how many ways can we write it as a sum of consecutive positive integers
    """
    def consecutive_numbers_sum(self, n: int) -> int:
        # Write your code here
        '''
        There is a math tricky:
        1. K = N
        2. K + K + 1 = N -> 2K = N - 1
        3. K + K + 1 + K + 2 = N -> 3K = N - 1 - 2
        '''
        r = 0
        i = 1
        while n > 0:
            if (n % i) == 0:
                r += 1
            n -= i
            i += 1
        return r
      
# medium: https://www.lintcode.com/problem/1439/
