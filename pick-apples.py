from typing import (
    List,
)

class Solution:
    """
    @param a: a list of integer
    @param k: a integer
    @param l: a integer
    @return: return the maximum number of apples that they can collect.
    """
    def pick_apples(self, a: List[int], k: int, l: int) -> int:
        # write your code here
        r = -1
        n = len(a)
        if (k + l) > n:
            return r
        alice, bob = [0] * n, [0] * n
        # 构造alice选k颗树的可能结果，可以写两重循环，但是当k非常大时，这样效率高。
        for i in range(k):
            alice[k - 1] += a[i]
        for i in range(k, n):            
            alice[i] = alice[i - 1] + a[i] - a[i - k]
        for i in range(l):
            bob[l - 1] += a[i]
        for i in range(l, n):            
            bob[i] = bob[i - 1] + a[i] - a[i - l]
        for i in range(k - 1, n):
            for j in range(l - 1, n):
                if ((i - j) >= k) or ((j -i) >= l):
                    r = max(r, alice[i] + bob[j])
        return r

# medium: https://www.lintcode.com/problem/1850
