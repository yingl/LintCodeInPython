class Solution:
    """
    @param s: string s
    @param t: string t
    @return: Given two strings s and t, write a function to determine if t is an anagram of s.
    """
    def isAnagram(self, s, t):
        # write your code here
        if len(s) != len(t):
            return False
        di = {}
        for i in range(len(s)):
            if s[i] in di:
                di[s[i]] += 1
            else:
                di[s[i]] = 1
            if t[i] in di:
                di[t[i]] -= 1
            else:
                di[t[i]] = -1
        for k, v in di.items():
            if v != 0:
                return False
        return True

# easy: https://www.lintcode.com/problem/vlid-anagram/
