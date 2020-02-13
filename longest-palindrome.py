class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        ret = 0
        odd = False
        di = {}
        for c in s:
            if c in di:
                di[c] += 1
            else:
                di[c] = 1
        for k, v in di.items():
            if v % 2 == 0:
                ret += v
            else:
                odd = True
                if v > 1:
                    ret += (v - 1)
        if odd:
            ret += 1
        return ret

# easy: https://www.lintcode.com/problem/longest-palindrome/
