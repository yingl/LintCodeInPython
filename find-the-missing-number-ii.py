# coding: utf-8

class Solution:
    # @param {int} n an integer
    # @param {string} str a string with number from 1-n
    #                     in random order and miss one number
    # @return {int} an integer
    def findMissing2(self, n, str):
        # Write your code here
        self.ret = 0
        self.done = False
        self.mark = [False] * (1 + n)
        self._search(0, n, str)
        return self.ret

    def _search(self, i, n, str):
        if (i >= len(str)) or self.done:
            if not self.done:
                for i in xrange(1, n + 1):
                    if not self.mark[i]:
                        self.ret = i
                        break
                self.done = True
            return
        s = int(str[i])
        if s == 0: # [1, n]
            return
        j = i
        while s <= n: # 不断尝试多取一位
            if not self.mark[s]:
                self.mark[s] = True
                self._search(j + 1, n, str)
                self.mark[s] = False
            j += 1
            if j >= len(str):
                break
            s = s * 10 + int(str[j])

# medium: http://www.lintcode.com/zh-cn/problem/find-the-missing-number-ii/
