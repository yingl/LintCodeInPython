class Solution:
    """
    @param str: the string
    @return: the number of substrings 
    """
    def stringCount(self, str):
        # Write your code here.
        r = 0
        zeros = 0
        prev = 'x'
        for c in str:
            if (prev == '0') and (c != '0'):
                zeros = 0
            elif c == '0':
                if prev != '0':
                    zeros = 1
                else:
                    zeros += 1
                r += zeros
            prev = c
        return r
        
# medium: https://www.lintcode.com/problem/1870
