# coding: utf-8

class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        ret = 0
        if prices:
            max_profit_1, max_profit_2 = 0, 0
            min_price, max_price = prices[0], prices[-1]
            profits = [0] * len(prices)
            # 顺序找一次
            for i in xrange(1, len(prices)):
                profit = prices[i] - min_price
                if profit < 0:
                    min_price = prices[i]
                else:
                    if profit > max_profit_1:
                        max_profit_1 = profit
                profits[i] = max_profit_1 # 记录当前位置最大利润
            # 从后往前再找一次，利用第一次profits的结果。
            for i in xrange(len(prices) -2 , -1, -1):
                profit = max_price - prices[i]
                if profit < 0:
                    max_price = prices[i]
                else:
                    if profit > max_profit_2:
                        max_profit_2 = profit
                    if (max_profit_2 + profits[i]) > ret: # 有先买后卖的限制
                        ret = max_profit_2 + profits[i]
        return ret

# medium: http://lintcode.com/zh-cn/problem/best-time-to-buy-and-sell-stock-iii/
