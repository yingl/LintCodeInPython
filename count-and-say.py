# coding: utf-8

class Solution:
    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        # Write your code here
        return self._countAndSay(n)

    def _countAndSay(self, n):
        if n == 1:
            return '1'
        ret = ''
        prev_str = self._countAndSay(n - 1)
        i = 0
        while i < len(prev_str):
            ch = prev_str[i]
            sum = 1
            j = i + 1
            while j < len(prev_str):
                if prev_str[i] == prev_str[j]:
                    sum += 1
                    j += 1
                else:
                    break
            ret += str(sum)
            ret += ch
            i = j
        return ret

# easy: http://lintcode.com/zh-cn/problem/count-and-say/
