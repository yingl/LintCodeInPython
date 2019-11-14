# coding: utf-8

class Solution:
    """
    @param s: A string 
    @param p: A string includes "." and "*"
    @return: A boolean
    """
    def isMatch(self, s, p):
        # write your code here
        m, n = len(s), len(p)
        dp = [[False for _ in xrange(n + 1)] for _ in xrange(m + 1)]
        dp[0][0] = True # 两个长度为0的字符串一定匹配
        # 处理s长度为0的可能出现匹配情况
        for j in xrange(1, n + 1):  # j索引p
            dp[0][j] = (j > 1) and (p[j - 1] == '*') and dp[0][j - 2]
        for j in xrange(1, n + 1):  # j索引p
            for i in xrange(1, m + 1): # i索引s
                if (j > 1) and (p[j - 1] == '*'):
                    '''
                    在两种情况下匹配。
                    条件1：dp[i][j - 2] = True
                    条件2：以下两个条件同时满足
                      - dp[i - 1][j] = True
                      - s[i - 1] == p[j - 2]或者p[j - 2] == '.'
                    '''
                    dp[i][j] = (dp[i][j - 2]) or (dp[i - 1][j] and ((s[i - 1] == p[j - 2]) or (p[j - 2] == '.')))
                else:
                    # 只有当dp[i - 1][j - 1] = True时，判断两个字符是否匹配。
                    dp[i][j] = dp[i - 1][j - 1] and ((s[i - 1] == p[j - 1]) or (p[j - 1] == '.'))
        return dp[m][n]

# hard: http://lintcode.com/zh-cn/problem/regular-expression-matching/
