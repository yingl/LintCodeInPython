# coding: utf-8

class Solution:
    # @param {string[]} tokens The Reverse Polish Notation
    # @return {int} the value
    def evalRPN(self, tokens):
        # Write your code here
        ret = []
        for item in tokens:
            if self.isOperator(item):
                right_val = ret.pop()
                left_val = ret.pop()
                if item == '*':
                    ret.append(left_val * right_val)
                elif item == '/':
                    # Python对于正负数相除有问题，需要单独处理
                    hack = ((left_val > 0) and (right_val < 0)) or ((left_val < 0) and (right_val > 0))
                    div = abs(left_val) / abs(right_val)
                    if hack:
                        div = -1 * int(div)
                    ret.append(div)
                elif item == '+':
                    ret.append(left_val + right_val)
                else:
                    ret.append(left_val - right_val)
            else:
                ret.append(int(item))
        return 0 if not ret else ret[0]

    def isOperator(self, item):
        return (item == '+') or (item == '-') or (item == '*') or (item == '/')

# medium: http://lintcode.com/zh-cn/problem/evaluate-reverse-polish-notation/
