class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        # write your code here
        ret = 1
        facts = [1]
        for i in range(1, len(A)):
            facts.append(facts[-1] * i)
        for i in range(len(A)):
            rc = 0 # 逆序数
            for j in range(i + 1, len(A)):
                if A[i] > A[j]:
                    rc += 1
            ret += rc * facts[len(A) - i - 1]
        return ret

# medium: http://lintcode.com/zh-cn/problem/permutation-index/
