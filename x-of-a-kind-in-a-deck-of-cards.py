class Solution:
    """
    @param deck: a integer array
    @return: return a value of bool
    """
    def hasGroupsSizeX(self, deck):
        # write your code here
        # 分组统计后只要找到找到大于1的最大公约数即可
        if len(deck) < 2:
            return False
        di = {}
        for d in deck:
            if d not in di:
                di[d] = 1
            else:
                di[d] += 1
        m = min(di.values())
        for i in range(2, m + 1):
            match = True
            for v in di.values():
                if v % i != 0:
                    match = False
                    break
            if match:
                return match
        return False
        
# easy: https://www.lintcode.com/problem/x-of-a-kind-in-a-deck-of-cards/
