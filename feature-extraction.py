class Solution:
    """
    @param frames: A series of frames
    @return: Find the longest feature movement
    """
    def FeatureExtraction(self, frames):
        # write your code here
        r = 0
        di = {}
        for i in range(len(frames)):
            f = frames[i]
            n = f[0]
            for j in range(n):
                v = str(f[2 * j + 1]) + '-' + str(f[2 * j + 2])
                if v not in di:
                    di[v] = [i]
                else:
                    if i != di[v][-1]:
                        di[v].append(i)
        for v in di.values():
            l = 0
            prev = -1
            for i in v:
                if prev == -1:
                    l = 1
                else:
                    if (prev + 1) == i:
                        l += 1
                    else:
                        l = 1
                prev = i
                if l > r:
                    r = l
        return r

# easy: https://www.lintcode.com/problem/1135/
