class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        # Write your code here
        # 7步的情况：1的话走1步到2，走6步到7，丢1次足够了...
        ret = 1
        if length <= 7:
            return 1
        sc = [0] # 短路表，因为从1开始，所以都额外加个元素。
        dp = [0]
        for i in range(1, length + 1):
            sc.append(i) # 自己和自己一定短路
            dp.append(length + 1)
        dp[1] = 0 # 一开始就在位置0
        for i in range(len(connections)):
            sc[connections[i][0]] = connections[i][1] # 短路表内容
        for i in range(2, length + 1):
            x = ''
            if (i - 6) <= 1:
                x = 1
                dp[i] = 1 # 丢一次肯定能到
            else:
                x = 2
                for j in range(i - 1, i - 7, -1): # 往前看6步
                    dp[i] = min(dp[j] + 1, dp[i]) # j丢1次肯定能到i
            dp[sc[i]] = min(dp[i], dp[sc[i]]) # 更新第i个点对应的短路位置
        return dp[-1]

# easy: https://www.lintcode.com/problem/modern-ludo-i/
