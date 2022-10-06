class Solution:
    """
    @param n: int
    @param k: int
    @param w: int
    @return: the probability
    """
    def new21_game(self, n: int, k: int, w: int) -> float:
        # Write your code here.
        '''
        使用DP，dpi表示当前值为i的概率。每次可选牌的范围是1到w，所以如果当前值为i，
        那么上一次的取值范围为i - w到i - 1。
        我们要求的结果是大于k的数，所以最终i的范围落在k到k + w - 1。如果n >= k + w，
        那么就跟就说100%.如果n < k + w，那么累加概率值即可。
        '''
        if (k == 0) or (n >= (k + w)):
            return 1
        r = 0
        s = 0
        dp = [0] * (n + 1) # [0, n]
        for i in range(1, n + 1):
            dp[i] = (s / w + 1 / w) if (i <= w) else (s / w)
            if i < k:
                s += dp[i]
            if i > w:
                s -= dp[i - w]
            if i >= k:
                r += dp[i]
        return r
      
# medium: https://www.lintcode.com/problem/1432
