class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def countPrimes(self, n):
        # write your code here
        nums = [0] * n
        for i in range(2, int(math.sqrt(n)) + 1):
            if nums[i] == 0:
                j = 2
                while (i * j) < n:
                    nums[i * j] = 1
                    j += 1
        return n - sum(nums) - 2 # 0和1扣除
        
# easy: https://www.lintcode.com/problem/count-primes/
