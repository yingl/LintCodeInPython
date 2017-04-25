# coding: utf-8

class Solution:
    """
    @param S: The set of numbers.
    @return: A list of lists. See example.
    """
    def subsets(self, S):
        # write your code here
        ret = []
        S.sort()
        for i in xrange(len(S) + 1):
            combs = self._subsets(S, 0, i) # 计算包含i个元素的子集
            for comb in combs:
                ret.append(comb)
        return ret
        
    def _subsets(self, numbers, pos, k):
        n = len(numbers) - pos
        if (not numbers) or (n < k):
            return None
        ret = []
        if k == 0:  # 0/1特殊情况处理
            return [[]]
        for i in xrange(pos, len(numbers), 1):
            combs = self._subsets(numbers, i + 1, k - 1)  # 计算i + 1开始位置，包含k - 1个元素的子集
            if combs:
                if combs != [[]]:
                    for comb in combs:
                        new_comb = [numbers[i]]
                        new_comb.extend(comb)
                        ret.append(new_comb)
                else:
                    ret.append([numbers[i]])
        return ret

# medium: http://lintcode.com/zh-cn/problem/subsets/
