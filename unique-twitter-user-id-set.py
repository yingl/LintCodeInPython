class Solution:
    """
    @param arr: a integer array
    @return: return ids sum is minimum.
    """
    def UniqueIDSum(self, arr):
        # write your code here
        ret = 0
        di = {}
        a = arr.copy()
        a.sort()
        prev = a[0] - 1
        for i in a:
            if i != prev:
                if prev in di:
                    if i <= di[prev][-1]:
                        di[i] = [di[prev][-1] + 1]
                    else:
                        di[i] = [i]
                else:
                    di[i] = [i]
                prev = i
            else:
                v = di[i][-1] + 1
                di[i].append(v)
        for v in di.values():
            ret += sum(v)
        return ret
      
# easy: https://www.lintcode.com/problem/1521/
