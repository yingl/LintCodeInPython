# coding: utf-8

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        ret = 0
        buy_price = -1
        for i in xrange(len(prices) - 1): # 最后一天只能卖
            if buy_price == -1: # 寻找买点
                if prices[i] < prices[i + 1]:
                    buy_price = prices[i]
                else:
                    continue
            else: # 寻找卖点，这里sell_price肯定大于buy_price。
                if prices[i] > prices[i + 1]:
                    ret += prices[i] - buy_price
                    buy_price = -1
        if buy_price != -1:
            ret += prices[-1] - buy_price
        return ret

# medium: http://lintcode.com/zh-cn/problem/best-time-to-buy-and-sell-stock-ii/
