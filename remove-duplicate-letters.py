class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def removeDuplicateLetters(self, s):
        # write your code here
        '''
        因为要求字典序最小，当一个字符出现的时候，必须进行如下判断：
        1. 如果ret没有内容直接加入
        2. 判断ret最后一个字符
           - 如果还有出现机会：如果比当前字符大，删掉，继续比ret的最后一个字符，因为字典序要求最小。
           - 将当前字符插入
        '''
        ret = []
        counting = {}
        visited = {}
        for c in s:
            if c not in counting:
                counting[c] = 1
            else:
                counting[c] += 1
            visited[c] = False # 先初始化为False
        for c in s:
            counting[c] -= 1
            if visited[c]:
                continue
            while (len(ret) > 0) and (counting[ret[-1]] > 0) and (ret[-1] > c):
                visited[ret[-1]] = False
                ret.pop()
            ret.append(c)
            visited[c] = True
        return ''.join(ret)
