class Solution:
    """
    @param S: a string
    @param K: a integer
    @return: return a string
    """
    def licenseKeyFormatting(self, S, K):
        # write your code here
        ret = []
        count = 0
        for i in range(len(S) - 1, -1, -1):
            if S[i] != '-':
                count += 1
                ret.append(S[i].upper())
                if (count % K) == 0:
                    ret.append('-')
        if ret[-1] == '-':
            ret.pop()
        ret.reverse()
        return ''.join(ret)
        
# easy: https://www.lintcode.com/problem/license-key-formatting/
