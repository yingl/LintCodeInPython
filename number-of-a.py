class Solution:
    """
    @param s: the given string
    @return: the number of A
    """
    def countA(self, s):
        # Write your code here
        return self._countA(s, 0, len(s) - 1)

    def _countA(self, s, start, end):
      if start <= end:
        mid = (start + end) // 2
        c = s[mid]
        if c == 'B':
          return self._countA(s, mid + 1, end)
        else:
          ret = self._countA(s, start, mid - 1)
          if c == 'A':
            ret += 1 + self._countA(s, mid + 1, end)
          return ret
      else:
        return 0

# easy: https://www.lintcode.com/problem/number-of-a/
