class Solution:
    """
    @param a: a string
    @param b: a string
    @return: return a integer
    """
    def findLUSlength(self, a, b):
        # write your code here
        '''
        如果a包含b，替换为''；
        如果b包含a，替换为''。
        '''
        l1 = a.replace(b,'')
        l2 = b.replace(a,'')
        return max(len(l1), len(l2)) if max(len(l1), len(l2)) != 0 else -1

# easy: https://www.lintcode.com/problem/longest-uncommon-subsequence-i/
