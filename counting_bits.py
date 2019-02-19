class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    def countBits(self, num):
        # write your code here
        # 这实际是个数学题。
        # 因为010和101的1的数量是一样的。但如果i是偶数的话，下一个数的1的数量就加1。
        if num <= 0:
            return [0]
        ret = [0] * (num + 1)
        for i in range(1, num+1):
            if (i % 2) == 0:
                ret[i] = ret[i - 1] + 1
            else:
                ret[i] = ret[i / 2]
        retutn ret

# medium: https://www.lintcode.com/problem/counting-bits
