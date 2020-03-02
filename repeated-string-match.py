class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return an integer
    """
    def repeatedStringMatch(self, A, B):
        # write your code here
        # 因为存在不匹配的可能性，要确定一个次数上限。
        # 如果A的长度是5，B的长度是15/16,那么最多循环4次一定就能匹配，否则无解。
        # 具体解释（能匹配的情况）：
        # A的格式：ABCDE
        # B的格式：EABCD-EABCD-EABCD-E
        # A循环4次：ABCD-[EABCD-EABCD-EABCD-E]
        # 但是如果B的长度是17，那么最多循环5次一定就能匹配，否则无解。
        # B的格式：EABCD-EABCD-EABCD-EA
        # A循环4次：ABCD-[EABCD-EABCD-EABCD-EA]-BCDE
        # 可以试着证明一下，然后用下面的公式计算limit。
        if A:
            limit = int(len(B) / len(A))
            if (len(B) % len(A)) <= 1:
                limit += 1
            else:
                limit += 2
            _str = list(A)
            ret = 1
            while limit >= 0:
                if len(_str) >= len(B):
                    for i in range(len(_str) - len(B) + 1):
                        j = 0
                        while j < len(B):
                            if _str[i + j] != B[j]:
                                break
                            else:
                                j += 1
                        if j == len(B):
                            return ret
                _str += list(A)
                ret += 1
                limit -= 1
        return -1

# easy: https://www.lintcode.com/problem/repeated-string-match/
