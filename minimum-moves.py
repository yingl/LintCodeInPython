class Solution:
    """
    @param S: a string
    @return:  return the minimum number of moves
    """
    def MinimumMoves(self, S):
        # write your code here
        ret = 0
        if S:
            n = 1
            c = S[0]
            S += ' ' # 因为最后一个字符也要判断，所以额外加个空格。
            for i in range(1, len(S)):
                if c == S[i]:
                    n += 1
                else:
                    ret += int(n / 3) # 根据之前连续的数目决定要移动几次
                    c = S[i]
                    n = 1
        return ret

# easy: https://www.lintcode.com/problem/minimum-moves/
