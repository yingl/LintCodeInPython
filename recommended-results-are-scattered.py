class Solution:
    """
    @param elements: A list of recommended elements.
    @param n: [picture P] can appear at most 1 in every n
    @return: Return the scattered result.
    """
    def scatter(self, elements, n):
        # write your code here
        ret = []
        start = 0
        while start < len(elements):
            if elements[start].startswith('P'):
                ret.extend(elements[:start + 1])
                break
            start += 1
        plist, vlist = [], []
        for i in range(start + 1, len(elements)):
            e = elements[i]
            if e.startswith('P'):
                plist.append(e)
            else:
                vlist.append(e)
        v_start, p_start = 0, 0
        while True:
            if v_start == len(vlist):
                break
            elif (len(vlist) - v_start) < (n - 1):
                ret.extend(vlist[v_start:])
            else:
                ret.extend(vlist[v_start : v_start + n - 1])
            if p_start >= len(plist):
                break
            v_start += (n - 1)
            if v_start > len(vlist):
                break
            ret.append(plist[p_start])
            p_start += 1
        return ret
        
# easy: https://www.lintcode.com/problem/recommended-results-are-scattered/
