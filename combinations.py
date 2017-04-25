# coding: utf-8

class Solution:
    """    
    @param n: Given the range of numbers
    @param k: Given the numbers of combinations
    @return: All the combinations of k numbers out of 1..n   
    """
    def combine(self, n, k):      
        # write your code here
        # TODO: 添加注释
        list = [x + 1 for x in xrange(n)]
        return self.dfs(list, 0, k)
        
    def dfs(self, list, pos, k):
        n = len(list) - pos
        if (not list) or (n < k):
            return None
        ret = []
        if k == 0:
            return [[]]
        elif k == 1:
            for i in xrange(pos, len(list), 1):
                ret.append([list[i]])
            return ret
        else:
            for i in xrange(pos, len(list), 1):
                combs = self.dfs(list, i + 1, k - 1)
                if combs:
                    for comb in combs:
                        new_comb = [list[i]]
                        new_comb.extend(comb)
                        ret.append(new_comb)
            return ret

# medium: http://lintcode.com/zh-cn/problem/combinations/
