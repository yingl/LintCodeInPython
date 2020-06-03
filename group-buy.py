class Solution:
    """
    @param x: the number of people who plan to buy goods A.
    @param y: the number of people who plan to buy goods B.
    @param z: the number of people who plan to buy goods C.
    @return: return the maximum times they can group buy.
    """
    def groupBuyTimes(self, x, y, z):
        # write your code here
        '''
        其题目并不要求买到x + y + z件商品，然后满足团购条件下购买尽可能多的商品。
        1. 如果z大于等于x，那么返回x与y之间较小的。
        2. 如果z大于等于y，同上。
        3. 如果x和y都大于z,那么z一定能满足。x和y剩下的部分最多可团购(x + y) / 3次，但是要看一下是否满足限制。
        '''
        if z >= x:
            return y if x >= y else x
        if z >= y:
            return y if x >= y else x
        x -= z
        y -= z
        r = int((x + y) / 3)
        if r > min(x, y):
            r = min(x, y)
        return r + z
        
# easy: https://www.lintcode.com/problem/group-buy/my-submissions
