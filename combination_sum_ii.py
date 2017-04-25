# coding: utf-8

class Solution:    
    """
    @param candidates: Given the candidate numbers
    @param target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, candidates, target): 
        # write your code here
        self.ret = []
        self.target = target
        candidates.sort()
        self._combinationSum2(candidates, [], 0, 0)
        return self.ret
        
    def _combinationSum2(self, candidates, comb, i, _sum):
        if _sum == self.target:
            self.ret.append(comb[:])
        elif _sum > self.target:
            return
        else:
            if i <= len(candidates):
                prev = None
                j = i
                while j < len(candidates):
                    if candidates[j] != prev:
                        prev = candidates[j]
                        comb.append(candidates[j])
                        self._combinationSum2(candidates, comb, j + 1, _sum + prev)
                        comb.pop()
                    j += 1

# medium: http://lintcode.com/zh-cn/problem/combination-sum-ii/
