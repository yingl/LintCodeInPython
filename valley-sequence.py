class Solution:
    """
    @param num: sequence
    @return: The longest valley sequence
    """
    def valley(self, num):
        # write your code here
        ret = 0
        di = {} # key is the value in the number, value is the coresponding position.
        n = len(num)
        dpl, dpr = [0] * n, [0] * n # l descending, r ascending... important!!!
        for i in range(n):
            if num[i] not in di:
                di[num[i]] = []
            di[num[i]].append(i)
            dpl[i] = 1
            for j in range(i - 1, -1, -1):
                if num[j] > num[i]:
                    dpl[i] = max(dpl[i], dpl[j] + 1)
        for i in range(n - 1, -1, -1):
            dpr[i] = 1
            for j in range(i + 1, n):
                if num[j] > num[i]:
                    dpr[i] = max(dpr[i], dpr[j] + 1)
        for i in num:
            l = di[i]
            if len(l) < 2:
                continue
            for j in range(len(l)):
                for k in range(j + 1, len(l)):
                    ret = max(ret, min(dpl[l[j]], dpr[l[k]]) * 2)
            di[i] = []
        return ret
      
# medium: https://www.lintcode.com/problem/342/
