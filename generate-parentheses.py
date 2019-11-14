# coding: utf-8

class Solution:
    # @param {int} n n pairs
    # @return {string[]} All combinations of well-formed parentheses
    def generateParenthesis(self, n):
        # Write your code here
        self.limit = n
        self.ret = []
        self._generateParenthesis('', 0, 0)
        return self.ret

    def _generateParenthesis(self, comb, left_pars, right_pars):
        if (left_pars == self.limit) and (right_pars == self.limit):
            if self.limit > 0:  # 处理n等于0的特殊情况
                self.ret.append(comb)
            return
        if left_pars < self.limit:  # 左括号数目必须小于等于n
            self._generateParenthesis(comb + '(', left_pars + 1, right_pars)
        if right_pars < left_pars:  # 未完成的组合，右括号数目必须小于等于左括号。
            self._generateParenthesis(comb + ')', left_pars, right_pars + 1)

# medium: http://lintcode.com/zh-cn/problem/generate-parentheses/
