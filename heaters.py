class Solution:
    """
    @param houses: positions of houses
    @param heaters: positions of heaters
    @return: the minimum radius standard of heaters
    """
    def findRadius(self, houses, heaters):
        # Write your code here
        # 按照顺序找到每个屋子距离最近的加热器，记录其位置差。
        # 所有的位置差里面最长的那一个就是最小的加热器半径了
        ret = 0
        houses.sort()
        heaters.sort()
        j = 0
        for i in range(len(houses)):
            while j < (len(heaters) - 1):
                diff_1 = abs(heaters[j] - houses[i])
                diff_2 = abs(heaters[j + 1] - houses[i])
                if diff_1 >= diff_2:
                    j += 1
                else:
                    break
            ret = max(ret, abs(heaters[j] - houses[i]))
        return ret

# easy: https://www.lintcode.com/problem/heaters/
