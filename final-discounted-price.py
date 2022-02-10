class Solution:
    """
    @param prices: a list of integer
    @return: return the actual prices
    """
    def FinalDiscountedPrice(self, prices):
        # write your code here
        r = [p for p in prices]
        stack = []
        for i in range(len(prices)):
            while stack and (prices[stack[-1]] >= prices[i]):
                idx = stack.pop()
                r[idx] = prices[idx] - prices[i]
            stack.append(i)
        return r
      
# medium: https://www.lintcode.com/problem/1852/
