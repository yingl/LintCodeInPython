class Solution:
    """
    @param str: the pattern 
    @return: the minimum number
    """
    def formMinimumNumber(self, str):
        # Write your code here.
        n = len(str)
        ret = [0] * (n + 1)
        i, idx = 0, 0
        while i <= n:
            if (i == n) or (str[i] == 'I'):
                for j in range(i, idx - 1, -1):
                    ret[j] = (1 + idx + i - j).__str__() # The first value for I must be 1!
                idx = i + 1
            i += 1
        return ''.join(ret)
      
# medium: https://www.lintcode.com/problem/1890
