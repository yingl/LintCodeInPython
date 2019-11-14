class Solution:
    """
    @param x: an integer
    @param y: an integer
    @return: return an integer, denote the Hamming Distance between two integers
    """
    def hammingDistance(self, x, y):
        # write your code here
        # 转成2进制字符串后比较，记得长度不同前面补0。
        r = 0
        bx = bin(x)[2:]
        by = bin(y)[2:]
        diff = abs(len(bx) - len(by))
        if len(bx) > len(by):
            by = '0' * diff + by
        else:
            bx = '0' * diff + bx
        for i in range(len(bx)):
            if bx[i] != by[i]:
                r += 1
        return r

# easy: https://www.lintcode.com/problem/hamming-distance
