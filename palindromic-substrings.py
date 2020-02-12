def count_alindromic(s, begin, end, count):
    while (begin >= 0) and (end < len(s)):
        if s[begin] == s[end]:
            count[0] += 1
            begin -= 1
            end += 1
        else:
            break
    
class Solution:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    def countPalindromicSubstrings(self, _str):
        # write your code here
        # 回文可以是奇数，也可以是偶数。
        # 如果xy...yx是回文，那么y...y一定也是回文。
        ret = [0]
        for i in range(len(_str)):
            count_alindromic(_str, i, i, ret)
            count_alindromic(_str, i, i + 1, ret)
        return ret[0]

##########

class Solution:
    """
    @param str: s string
    @return: return an integer, denote the number of the palindromic substrings
    """
    def countPalindromicSubstrings(self, _str):
        # write your code here
        # dp[i][j]表示str[i:j + 1]是否为回文串。
        # 如果dp[i][j]是回文串，那么dp[i + 1][j - 1]一定也是。
        ret = 0
        dp = [[False] * len(_str) for i in range(len(_str))]
        for i in range(len(_str) - 1, -1, -1):
            for j in range(i, len(_str)):
                if _str[i] == _str[j]:
                    # 相邻或中间段为回文，不用担心数组越界，想一下为什么？
                    if ((j - i) <= 2) or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        ret += 1
        return ret

# easy: https://www.lintcode.com/problem/palindromic-substrings/
