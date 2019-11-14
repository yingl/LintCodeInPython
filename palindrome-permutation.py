class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # write your code here
        counting = {}
        for c in s:
            if c not in counting:
                counting[c] = 1
            else:
                counting[c] += 1
        not_2 = 0
        for k, v in counting.items():
            if (v % 2) != 0:
                not_2 += 1
        if (len(s) % 2) == 0:
            return not_2 == 0
        else:
            return not_2 == 1
            
# easy: https://www.lintcode.com/problem/palindrome-permutation/
