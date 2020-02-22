class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """
    def canPlaceFlowers(self, flowerbed, n):
        # Write your code here
        # 连续偶数个0的情况分为以下几种：
        # - 空（开始） 0000 满 -> X0X0
        # - 空（起始位置） 0000 空（结束） -> X0X0
        # - 满 0000 满 -> 0X00, 00X0
        # 连续奇数个0的情况分为以下几种：
        # - 空（开始） 000 满 -> X00, 0X0
        # - 空（开始） 000 空（结束） -> X0X
        # - 满 000 满 -> 0X0
        # - 满 000 空（结束） -> 0X0, 00X
        # 在头尾各补一个0，然后判断连续0：
        # - 偶数：int((n - 1) / 2)
        # - 奇数：(n - 1) / 2
        if not flowerbed:
            return False
        ext_bed = []
        if flowerbed[0] == 0:
            ext_bed.append(0)
        ext_bed.extend(flowerbed)
        if flowerbed[-1] == 0:
            ext_bed.append(0)
        total, c_z = 0, 0
        for i in range(len(ext_bed) + 1): # 扩展一位，方便处理最后的0。
            if (i < len(ext_bed)) and (ext_bed[i] == 0):
                c_z += 1
            else:
                total += int((c_z - 1) / 2)
                c_z = 0
        return total >= n

# easy: https://www.lintcode.com/problem/can-place-flowers/
