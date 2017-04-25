# coding: utf-8

class Solution:
    def __init__(self):
      self.cache = {}

    # @param n: an integer
    # @return: a boolean which equals to True if the first player will win
    def firstWillWin(self, n):
        # write your code here
        if n == 0:
            return False
        elif n <= 2:
            return True
        if n not in self.cache:
            '''
            如果n - 3被第一个玩家拿走，
            那么不管第二个玩家拿1个或2个，
            第n个一定被第一个玩家拿走。
            '''
            self.cache[n] = self.firstWillWin(n - 3)
        return self.cache[n]

# medium: http://lintcode.com/zh-cn/problem/coins-in-a-line/
