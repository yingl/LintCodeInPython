class Solution:
    """
    @param num: a array
    @param target: a num
    @return: return all combinations
    """
    def combinationSet(self, num, target):
        # write your code here
        ret = []
        self.dfs(ret, num, target, 0)
        return ret
        
    def dfs(self, ret, num, target, cur):
        for i in num:
            tmp = cur
            cur = cur * 10 + i
            if cur < target:
                ret.append(cur)
                if cur > 0:
                    self.dfs(ret, num, target, cur)
            cur = tmp
            
# easy: https://www.lintcode.com/problem/combination-set/
