# coding: utf-8

class Solution:
    # @param {string} s the string that represents a number
    # @return {boolean} whether the string is a valid number
    def isNumber(self, s):
        # Write your code here
        INIT = 0  # 初始化状态表
        INT = 10  # 整数
        SIGN = 20 # 正负号
        DOT = 30  # 小数点
        FLOAT = 40  # 浮点数
        EXP = 50  # e
        EXP_INT = 60  # e的整数次方
        EXP_SIGN = 70 # e^(+...)或e^(-...)
        ENDING_SPACES = 80
        state = 0
        for ch in s:
            if state == INIT:
                if (ch >= '0') and (ch <= '9'):
                    state = INT
                elif (ch == '+') or (ch == '-'):
                    state = SIGN
                elif ch == '.':
                    state = DOT
                elif ch != ' ':
                    return False
            elif state == INT:
                if (ch < '0') or (ch > '9'):
                    if ch == '.':
                        state = FLOAT
                    elif ch == 'e':
                        state = EXP
                    elif ch == ' ':
                        state = ENDING_SPACES
                    else:
                        return False
            elif state == SIGN:
                if (ch >= '0') and (ch <= '9'):
                    state = INT
                elif ch == '.':
                    state = DOT
                else:
                    return False
            elif state == DOT:
                if (ch >= '0') and (ch <= '9'):
                    state = FLOAT
                else:
                    return False
            elif state == FLOAT:
                if (ch < '0') or (ch > '9'):
                    if ch == 'e':
                        state = EXP
                    elif ch == ' ':
                        state = ENDING_SPACES
                    else:
                        return False
            elif state == EXP:
                if (ch >= '0') and (ch <= '9'):
                    state = EXP_INT
                elif (ch == '+') or (ch == '-'):
                    state = EXP_SIGN
                else:
                    return False
            elif state == EXP_INT:
                if (ch < '0') or (ch > '9'):
                    if ch == ' ':
                        state = ENDING_SPACES
                    else:
                        return False
            elif state == EXP_SIGN:
                if (ch >= '0') and (ch <= '9'):
                    state = EXP_INT
                else:
                    return False
            elif state == ENDING_SPACES:
                if ch != ' ':
                    return False
        return (state == INT) \
                or (state == FLOAT) \
                or (state == EXP_INT) \
                or (state == ENDING_SPACES)

# hard: http://lintcode.com/zh-cn/problem/valid-number/
