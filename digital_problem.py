class Solution:
    """
    @param n: the number n 
    @return: the times n convert to 1
    """
    def digitConvert(self, n):
        # Write your code here 
        i = 0
        while n != 1:
            if (n % 2) == 0:
                n = n / 2
            else:
                n = n * 3 + 1
            i += 1
        return i

# easy: http://lintcode.com/zh-cn/problem/digital-problem/
