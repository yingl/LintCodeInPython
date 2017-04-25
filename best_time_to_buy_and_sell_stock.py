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
            buy_price = prices[0] # 必须先买后卖，假设先在第一天买进。
            for i in xrange(1, len(prices)):
                ret = max(ret, prices[i] - buy_price)
                buy_price = min(prices[i], buy_price) # 更新买入价格
        return ret

# medium: http://lintcode.com/zh-cn/problem/best-time-to-buy-and-sell-stock/
