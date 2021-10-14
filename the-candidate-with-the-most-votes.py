class Solution:
    """
    @param votes: The array of names of candidates in the election.
    @return: The name of the candidate who has the most votes.
    """
    def candidateWithTheMostVotes(self, votes):
        # Write your code here
        ret = ''
        mv = 0
        di = {}
        for v in votes:
            if v not in di:
                di[v] = 1
            else:
                di[v] += 1
        for k, v in di.items(): # 不对字典排序，遍历！
            if v > mv:
                mv = v
                ret = k
            elif (v == mv) and (k < ret):
                ret = k
        return ret

# easy: https://www.lintcode.com/problem/1780/
