class Solution:
    """
    @param x: the wall's height
    @return: YES or NO
    """
    def isBuild(self, x):
        # write you code here
        # 这题容易被题目吓着，其实就是3和7能不能堆成某个高度。
        # 理论上只要高度满足3 * n + 7 * m就行，但是很难凑。
        # 反向思考，高度除7的余数：
        # 1. 余数属于[0, 3, 6]正好都是3的倍数。
        # 2. 如果高度大于7，但是余数等于2，那么可以把7拿出来凑9。
        # 3. 如果高度大于7，但是余数等于5，那么可以把7拿出来凑12。
        # 4. 其它情况就没办法了。
        m = x % 7
        if m in [0, 3, 6]:
            return "YES"
        elif (x > 7) and ((m == 5) or (m==2)):
            return "YES"
        else:
            return "NO"

# easy: https://www.lintcode.com/problem/johns-backyard-garden
