class Solution:
    """
    @param amount: The amount you should pay.
    @return: Return the minimum number of coins for change.
    """
    def giveChange(self, amount):
        # write you code here.
        ret = 0
        coins = [64, 16, 4, 1]
        c = 0
        amount = 1024 - amount
        while amount > 0:
            ret += int(amount / coins[c])
            amount -= int(amount / coins[c]) * coins[c]
            c += 1
        return ret
        
# easy: https://www.lintcode.com/problem/give-change/
