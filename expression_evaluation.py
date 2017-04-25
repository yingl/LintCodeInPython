# coding: utf-8

class Solution:
    # @param expression: a list of strings;
    # @return: an integer
    def evaluateExpression(self, expression):
        # write your code here
        '''
        先转换成后缀表达式，然后再计算后缀表达式的值。
        后缀表达式转换步骤：
        1. 定义两个堆栈，表达式栈ex和运算符栈op。
        2. 从左到右扫描中缀表达式
        3. 遇到操作数，直接进ex。
        4. 遇到运算符，与op栈顶元素比较优先级
          - 4.1. 如果op为空，或者栈顶运算符为'('，入栈。
          - 4.2. 若优先级高于op栈顶运算符，入站。
          - 4.3. 弹出op栈顶元素压入ex，再次转到4.1。
        5. 如果运算符是'('或'))'
          - 5.1. '('直接入栈
          - 5.2. 如果是')'，一次将op栈操作符弹出并入压ex栈，直到遇到'('，抛弃匹配括号。
        6. 重复2到5
        7. 将op栈内剩余元素依次弹出并压入ex栈。
        关于后缀表达式的计算自己google去。
        '''
        op_rank = {'+': 1, '-':1, '*':2, '/': 2, '(': 3, ')': 3}
        post_expr = []
        op_stack = []
        for item in expression:
            if self.isOperand(item):  # #1
                post_expr.append(item)
            elif item == ')':   # step #5
                while op_stack and op_stack[-1] != '(': # #5.2
                    post_expr.append(op_stack.pop())
                op_stack.pop()
            else:
                # #4.1 and #4.2
                while op_stack and (op_stack[-1] != '(') and (op_rank[item] <= op_rank[op_stack[-1]]):
                    post_expr.append(op_stack.pop())
                op_stack.append(item)   # #4.1 and #5.1
        while op_stack:
            post_expr.append(op_stack.pop())    # #7
        ret = []
        for item in post_expr:
            if self.isOperand(item):
                ret.append(int(item))
            else:
                right_val = ret.pop()
                left_val = ret.pop()
                if item == '*':
                    ret.append(left_val * right_val)
                elif item == '/':
                    ret.append(left_val / right_val)
                elif item == '+':
                    ret.append(left_val + right_val)
                else:
                    ret.append(left_val - right_val)
        return 0 if not ret else ret[0] # 小心全括号的场景

    def isOperand(self, item):  # 这里偷个懒，测试数据没有负数！
        return (item[0] >= '0') and (item[0] <= '9')

# hard: http://lintcode.com/problem/expression-evaluation
