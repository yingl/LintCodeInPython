class Solution:
    def diStringMatch(self, S):
        #
        '''
        测试几例子可以发现：I序列从0开始递增，D序列从len(S)开始递减。
        IDID
        - I 0
        - D 4
        - I 1
        - D 3
        - 2
        '''
        ret = []
        start, end = 0, len(S)
        for c in S:
            if c == 'I':
                ret.append(start)
                start += 1
            else:
                ret.append(end)
                end -= 1
        if S[-1] == 'I':
            ret.append(start)
        else:
            ret.append(end)
        return ret
        
# easy: https://www.lintcode.com/problem/di-string-match/
