# coding: utf-8

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        # write your code here
        self.ret = []
        self.target = target
        candidates.sort()
        self._combinationSum(candidates, [], 0, 0)
        return self.ret
        
    def _combinationSum(self, candidates, comb, i, _sum):
        if _sum == self.target:
            self.ret.append(comb[:])
        elif _sum > self.target:
            return
        else:
            if i <= len(candidates):
                comb.append(candidates[i])
                self._combinationSum(candidates, comb, i, _sum + candidates[i])
                comb.pop()
                prev = candidates[i]
                j = i
                while j < len(candidates):
                    if candidates[j] != prev:
                        prev = candidates[j]
                        comb.append(candidates[j])
                        self._combinationSum(candidates, comb, j, _sum + prev)
                        comb.pop()
                    j += 1

# medium: http://lintcode.com/zh-cn/problem/combination-sum/
