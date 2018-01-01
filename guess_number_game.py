# coding: utf-8

class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        # Write your code here
        start, end = 1, n
        while True:
            val = int((start + end) / 2)
            r = Guess.guess(val)
            if r == 0:
                return val
            if r < 0: # 期望数字比你猜得小
                end = val - 1
            else:
                start = val + 1
            
# easy: http://lintcode.com/zh-cn/problem/guess-number-game/
