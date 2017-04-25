# coding: utf-8

class Solution:
    # @param s, a string
    # @return a list of lists of string
    def partition(self, s):
        # write your code here
        self.ret = []
        self.statuses = [[False] * len(s) for i in xrange(len(s))]
        self.buildStatuses(s)
        self._partition(s, 0, [])
        return self.ret

    def _partition(self, s, start, palindromes):
        if start < len(s):
            for i in xrange(start, len(s)):
                if self.statuses[start][i]:
                    palindromes.append(s[start:i + 1])
                    self._partition(s, i + 1, palindromes)
                    palindromes.pop()
        else:
            self.ret.append(palindromes[:]) # 这里一定要复制！！！

    def buildStatuses(self, s):
        for i in xrange(len(s)):  # ...x...的情况
            self.statuses[i][i] = True
            j = 1
            while True:
              if ((i - j) >= 0) and ((i + j) < len(s)):
                  if s[i - j] == s[i + j]:
                      self.statuses[i - j][i + j] = True
                      j += 1
                  else:
                      break
              else:
                  break
        for i in xrange(0, len(s)): # ...xx...的情况
            if (i + 1) == len(s):
                break
            if s[i] != s[i + 1]:
                continue
            self.statuses[i][i + 1] = True
            j = 1
            while True:
                if ((i - j) >= 0) and ((i + 1 + j) < len(s)):
                    if s[i - j] == s[i + 1 + j]:
                        self.statuses[i - j][i + 1 + j] = True
                        j += 1
                    else:
                        break
                else:
                    break

# medium: http://lintcode.com/problem/palindrome-partitioning
