class Solution:
    """
    @param musics: the musics
    @return: calc the number of pair of music
    """
    def musicPairs(self, musics):
        # write your code here
        ret = 0
        di = {}
        musics.sort()
        for m in musics:
            if m not in di:
                di[m] = 0
            di[m] += 1
        for i in range(len(musics)):
            m = musics[i]
            di[m] -= 1
            r = self.round(m)
            while r <= musics[-1]:
                if (r in di) and (di[r] > 0):
                    ret += di[r]
                    r += 60
                else:
                    break
        return ret

    def round(self, n):
        return 60 * (int(n / 60) + 1) - n
        
# easy: https://www.lintcode.com/problem/music-pairs/
