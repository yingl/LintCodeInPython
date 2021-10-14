class Solution:
    """
    @param scores: two dimensional array
    @param K: a integer
    @return: return a integer
    """
    def FindTheRank(self, scores, K):
        # write your code here
        m = {} # 偷懒，直接排序然后查表！
        total = [sum(scores[i]) for i in range(len(scores))]
        for i in range(len(total)):
            if total[i] not in m:
                m[total[i]] = [i]
            else:
                m[total[i]].append(i)
        total.sort(reverse=True)
        return m[total[K - 1]][0]
      
# easy: https://www.lintcode.com/problem/1804/
