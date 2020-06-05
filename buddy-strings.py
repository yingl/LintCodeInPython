class Solution:
    """
    @param A: string A
    @param B: string B
    @return: bool
    """
    def buddyStrings(self, A, B):
        # Write your code here
        if len(A) != len(B):
            return False
        di = {}
        for i in range(len(A)):
            if not A[i] in di:
                di[A[i]] = 1
            else:
                di[A[i]] += 1
        if A == B:
            for k, v in di.items():
                if v >= 2:
                    return True
            return False
        for i in range(len(A)):
            if not B[i] in di:
                di[B[i]] = -1
            else:
                di[B[i]] -= 1
        for k, v in di.items():
            if v != 0:
                return False
        cnt = 0
        for i in range(len(A)):
            if A[i] != B[i]:
                cnt += 1
        return cnt == 2
        
# easy: https://www.lintcode.com/problem/buddy-strings/
