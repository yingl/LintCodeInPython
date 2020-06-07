class Solution:
    """
    @param N: a number
    @return: the number of prime numbers.
    """
    def Count_PrimeNum(self, N):
        #
        dp = [1] * (N + 1) # 技巧在这里，对于dp[2]及之后元素，本来就至少有一个质因数。
        for num in range(3, N + 1):
            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    d = int(num / i)
                    dp[num] = dp[i] + dp[d]
                    break
        return sum(dp[2:])
