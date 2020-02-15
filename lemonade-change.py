class Solution:
    """
    @param bills: the Bill
    @return: Return true if and only if you can provide every customer with correct change.
    """
    def lemonadeChange(self, bills):
        # Write your code here.
        # 对于20，优先用10 + 5，不行再用5 * 3。
        count_5, count_10 = 0, 0
        for b in bills:
            if b == 5:
                count_5 += 1
            elif b == 10:
                count_10 += 1 # 收进一张10元
                count_5 -= 1 # 找出一张5元
            else: # 20，另外20不能用于找零
                if count_10:
                    count_10 -= 1
                    count_5 -= 1
                else:
                    count_5 -= 3
            if count_5 < 0: # 5元不够用
                return False
        return True

# easy: https://www.lintcode.com/problem/lemonade-change/
