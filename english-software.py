class Solution:
    """
    @param score: Each student's grades
    @param ask: A series of inquiries
    @return: Find the percentage of each question asked
    """
    def englishSoftware(self, score, ask):
        # write your code here
        ret = []
        di = {}
        for i in range(len(score)):
            di[i + 1] = score[i]
        score.sort()
        for i in ask:
            bar = di[i]
            i, j = 0, len(score) - 1
            m = 0
            while i <= j:
                mid = int((i + j) / 2)
                if score[mid] == bar:
                    k = mid
                    while k < len(score):
                        if score[k] != bar:
                            break
                        k += 1
                    m = k - 1
                    break
                elif score[mid] < bar:
                    i = mid + 1
                else:
                    j = mid - 1
            ret.append(int(m * 100 / len(score)))
        return ret
# easy: https://www.lintcode.com/problem/super-lollipop/description
