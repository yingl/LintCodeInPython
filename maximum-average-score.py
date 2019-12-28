class Solution:
    """
    @param names: the name
    @param grades: the grade
    @return: the maximum average score
    """
    def maximumAverageScore(self, names, grades):
        # Write your code here
        ret = 0
        di = {}
        for i in range(len(names)):
            if names[i] not in di:
                di[names[i]] = [grades[i], 1]
            else:
                di[names[i]][0] += grades[i]
                di[names[i]][1] += 1
        for k, v in di.items():
            if (v[0] / v[1]) > ret:
                ret = v[0] / v[1]
        return float('%.2f' % (ret))

# easy: https://www.lintcode.com/problem/maximum-average-score/
