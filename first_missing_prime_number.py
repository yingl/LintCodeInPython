class Solution:
    """
    @param nums: an array of integer
    @return: the first missing prime number
    """
    def firstMissingPrime(self, nums):
        # write your code here
        '''
        先排序，然后分3种情况：
        1. 缺少第1个素数2
        2. 缺少的数在当中
        3. 缺少的数正好是当前最大素数的下一个
        '''
        if 2 not in nums:
            return 2
        nums.sort()
        for i in range(3, nums[-1] + 1):
            not_prime = False
            for k in nums: # 用除法验证是否素数，虽然2重循环，但是有k <= i的限制，效率问题不大。
                if (k <= i) and (i % k == 0):
                    not_prime = True
                    break
            if not not_prime:
                return i
        i = nums[-1] + 2 # 没找到，找下一个最大素数，循环知道满足条件。
        while True:
            not_prime = False
            for k in nums:
                if (k <= i) and (i % k == 0):
                    not_prime = True
                    break
            if not not_prime:
                return i
            else:
                i += 2

# medium: https://www.lintcode.com/problem/first-missing-prime-number
