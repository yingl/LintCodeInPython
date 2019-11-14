# coding: utf-8

class Solution:
    """
    @param A: An integer array.
    @param k: A positive integer (k <= length(A))
    @param target: Integer
    @return a list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        self.ret = []
        self.dfs(A, k, target, 0, [])
        return self.ret

    def dfs(self, A, k, target, index, candidates):
        if (target == 0) and (k == 0):
            self.ret.append(candidates)
            return None
        if (len(A) == index) or (target < 0) or (k < 0):
            return None
        # 跳过A[index]
        self.dfs(A, k, target, index + 1, candidates)
        # 保留A[index]
        new_candidates = []
        new_candidates.extend(candidates)
        new_candidates.append(A[index])
        self.dfs(A, k - 1, target - A[index], index + 1, new_candidates)

# medium: http://lintcode.com/zh-cn/problem/k-sum-ii/
