# coding: utf-8

class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        # write your code here
        x = 0
        for i in xrange(len(key)):
            x += ord(key[i]) * self.fastPower(33, HASH_SIZE, len(key) - 1 - i)
        return x % HASH_SIZE
        
    def fastPower(self, a, b, n): # 参考fast_power.py实现快速取模
        # write your code here
        if n == 0:
            return 1 % b
        if 1 == n:
            return a % b
        x = self.fastPower(a, b, n / 2)
        if n % 2 == 1:
            return (((x * x) % b) * a) % b
        else:
            return (x * x) % b

# easy: http://lintcode.com/problem/hash-function
