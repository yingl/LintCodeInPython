class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """
    def kthPrime(self, n):
        # write your code here
        ret = 0
        judge = [0 for i in range(n + 1)] # [0, n]
        for i in range(2, n + 1):
            if judge[i] ==  0: # 质数
                ret += 1
            j = 2
            while (i * j) < n:
                judge[i * j] = 1
                j += 1
        return ret

# easy: https://www.lintcode.com/problem/kth-prime-number/
