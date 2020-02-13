class Solution:
    """
    @param n: a positive integer
    @return: the nth digit of the infinite integer sequence
    """
    def findNthDigit(self, n):
        # write your code here
        # 首先明确以下知识：9个一位数，90个两位数，900个三位数，依次类推。
        count = 1 # 数字从1开始
        digits = 1 # 位数
        while n > (9 * digits * count):
            n -= 9 * digits * count
            count *= 10
            digits += 1
        count += ((n - 1) / digits) # 计算出现在那个数
        pos = (n - 1) % digits # 这个数里的具体位置
        return int(str(count)[pos])

# easy: https://www.lintcode.com/problem/nth-digit/
