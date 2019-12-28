class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def reverseString(self, s):
        # write your code here
        s = list(s)
        start, end = 0, len(s) - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        return ''.join(s)
        
# easy: https://www.lintcode.com/problem/reverse-string/
