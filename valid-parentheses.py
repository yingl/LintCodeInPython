# coding: utf-8

class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        # Write your code here
        par_list = []
        for ch in s:
            if (ch == '(') or (ch == '[') or (ch == '{'):
                par_list.append(ch) # 插入左括号
            else:
                if not self.check(ch, par_list):
                    return False
        return True if not par_list else False

    def check(self, right, par_list):
        if not par_list:
            return False
        left = par_list[-1]
        if ((left == '(') and (right == ')')) or \
                ((left == '[') and (right == ']')) or \
                ((left == '{') and (right == '}')):
            par_list.pop()  # 括号匹配成功后弹出
        else:
            par_list.append(right)
        return True

# easy: http://lintcode.com/zh-cn/problem/valid-parentheses/
