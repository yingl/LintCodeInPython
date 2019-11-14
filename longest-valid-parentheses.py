class Solution:
    """
    @param s: a string
    @return: return a integer
    """
    def longestValidParentheses(self, s):
        # write your code here
        ret = 0
        start = 0
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if not stack:
                    start = i + 1 # 重要，因为必须从'('开始。
                else:
                    stack.pop()
                    if not stack:
                        # 必须与上一次结果合并
                        ret = max(ret, i - start + 1)
                    else:
                        # 因为pop了，不需要再加1。
                        ret = max(ret, i - stack[-1])
        return ret
        
# easy: https://www.lintcode.com/problem/longest-valid-parentheses/
