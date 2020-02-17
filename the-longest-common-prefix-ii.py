class Solution:
    """
    @param dic: the n strings
    @param target: the target string
    @return: The ans
    """
    def the_longest_common_prefix(self, dic, target):
        # write your code here
        ret = 0
        for word in dic:
            tmp = 0
            for i in range(min(len(word), len(target))):
                if word[i] == target[i]:
                    tmp += 1
                else:
                    break
            if tmp > ret:
                ret = tmp
        return ret

# easy: https://www.lintcode.com/problem/the-longest-common-prefix-ii/
