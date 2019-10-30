class Solution:
    """
    @param num: an integer
    @return: whether the integer is a power of 4
    """
    def isPowerOfFour(self, num):
        # Write your code here
        s = set([1,
                 4,
                 16,
                 64,
                 256,
                 1024,
                 4096,
                 16384,
                 65536,
                 262144,
                 1048576,
                 4194304,
                 16777216,
                 67108864,
                 268435456,
                 1073741824])
        return num in s

# easy: https://www.lintcode.com/problem/power-of-four/
