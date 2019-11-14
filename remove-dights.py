class Solution:
    """
    @param num: a number
    @param k: the k digits
    @return: the smallest number
    """
    def removeKdigits(self, num, k):
        # write your code here.
        if k <= 0:
            return num
        if k >= len(num):
            return '0'
        new_len = len(num) - k
        stack = []
        for i in range(len(num)):
            while stack and (k > 0) and (stack[-1] > num[i]):
                # 当前元素比栈顶元素小，且还有数字可以删除。
                stack.pop()
                k = k - 1
            stack.append(num[i])
        start = 0
        while stack[start] == '0':
            start += 1
            if start >= new_len:
                break
        if start >= new_len:
            return '0'
        return ''.join(stack[start:new_len])

# easy: https://www.lintcode.com/problem/remove-dights/
