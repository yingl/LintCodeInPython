class Solution:
    """
    @param cost: The cost of each interviewer
    @return: The total cost of all the interviewers.
    """
    def TotalCost(self, cost):
        # write your code here
        # 因为AB人数相等，N一定是偶数。
        ret = 0
        diff = []
        for c in cost:
            ret += c[1]
            diff.append(c[0] - c[1])
        diff.sort()
        for i in range(int(len(diff) / 2)):
            ret += diff[i]
        return ret

# easy: https://www.lintcode.com/problem/arrange-interview-city/
