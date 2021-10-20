class Solution:
    """
    @param k: The k
    @param a: The A
    @param b: The B
    @return: The answer
    """
    def addition(self, k, a, b):
        # Write your code here
        r = []
        flag = 0
        a = a[::-1]
        b = b[::-1]
        i = 0
        while i < min(len(a), len(b)):
            v = int(a[i]) + int(b[i]) + flag
            r.append(str(int(v % k)))
            flag = 1 if v >= k else 0
            i += 1
        arr = a if len(a) > i else b
        while i < len(arr):
            v = int(arr[i]) + flag
            r.append(str(int(v % k)))
            flag = 1 if v >= k else 0
            i += 1
        if flag > 0:
            r.append('1')
        while r and (r[-1] == '0'):
            r.pop()
        return ''.join(r[::-1])

# easy: https://www.lintcode.com/problem/1398/
