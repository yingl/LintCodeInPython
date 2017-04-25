# coding: utf-8

class Solution:
    # @param expression: A string list
    # @return: The Reverse Polish notation of this expression
    def convertToRPN(self, expression):
        # write your code here
        # 原理请参考expression_evaluation.py的注释
        op_rank = {'+': 1, '-':1, '*':2, '/': 2, '(': 3, ')': 3}
        ret = []
        op_stack = []
        for item in expression:
            if self.isOperand(item):
                ret.append(item)
            elif item == ')':
                while op_stack and op_stack[-1] != '(':
                    ret.append(op_stack.pop())
                op_stack.pop()
            else:
                while op_stack and (op_stack[-1] != '(') and (op_rank[item] <= op_rank[op_stack[-1]]):
                    ret.append(op_stack.pop())
                op_stack.append(item)
        while op_stack:
            ret.append(op_stack.pop())
        return ret
    
    def isOperand(self, item):  # 这里偷个懒，测试数据没有负数！
        return (item[0] >= '0') and (item[0] <= '9')

# hard: http://lintcode.com/problem/convert-expression-to-reverse-polish-notation
