class Solution:
    """
    @param n: N
    @return: return the number of distinct numbers can you dial in this manner mod 1e9+7
    """
    def knight_dialer(self, n: int) -> int:
        # 
        '''
        可以缓存前序位置
        1. 到位置0，前一个位置可以是4或6；
        2. 到位置1，前一个位置可以是6或8；
        ...
        '''
        moves = [[4, 6],
                 [6, 8],
                 [7, 9],
                 [4, 8],
                 [0, 3, 9],
                 [],
                 [0, 1, 7],
                 [2, 6],
                 [1, 3],
                 [2, 4]]
        dp = [1] * 10
        for i in range(n - 1):
            new_dp = [0] * 10
            for num, count in enumerate(dp):
                for m in moves[num]:
                    new_dp[m] += count
            dp = new_dp
        return sum(dp) % (10 ** 9 + 7)

# medium: https://www.lintcode.com/problem/1707
