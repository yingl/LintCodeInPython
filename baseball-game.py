class Solution:
    """
    @param ops: the list of operations
    @return:  the sum of the points you could get in all the rounds
    """
    def calPoints(self, ops):
        # Write your code here
        stack = []
        for i in ops:
            if i == '+':
                stack.append(stack[-1] + stack[-2])
            elif i == 'C':
                stack.pop()
            elif i == 'D':
                stack.append(stack[-1] * 2)
            else:
                stack.append(int(i))
        return sum(stack)

# easy: https://www.lintcode.com/problem/baseball-game/
