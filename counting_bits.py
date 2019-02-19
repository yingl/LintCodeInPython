class Solution:
    """
    @param num: a non negative integer number
    @return: an array represent the number of 1's in their binary
    """
    def countBits(self, num):
        # write your code here
        # 这实际是个数学题。
        # 1. 如果是偶数，和除2后的数的1一样多。
        # 2. 如果是奇数，就是前一个偶数的1的数量再加1。
        if num <= 0:
            return [0]
        ret = [0] * (num + 1)
        for i in range(1, num + 1):
            if (i % 2) != 0:
                ret[i] = ret[i - 1] + 1
            else:
                ret[i] = ret[int(i / 2)]
        return ret

# medium: https://www.lintcode.com/problem/counting-bits
