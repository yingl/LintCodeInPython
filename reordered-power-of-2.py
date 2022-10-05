class Solution:
    """
    @param n: int
    @return: return true or false
    """
    def reordered_power_of2(self, n: int) -> bool:
        # write your code here
        digits = self.get_digits(n)
        p2s = []
        self.build_p2s(p2s, digits)
        for p in p2s:
            if self.compare(p, n):
                return True
        return False

    def get_digits(self, n):
        r = 0
        while n > 0:
            r += 1
            n = n // 10
        return r

    def build_p2s(self, p2s, digits):
        i = 1
        while True:
            d = self.get_digits(i)
            if d < digits:
                i *= 2
            elif d == digits:
                p2s.append(i)
                i *= 2
            else:
                break

    def compare(self, v1, v2):
        v1 = ''.join(sorted(str(v1)))
        v2 = ''.join(sorted(str(v2)))
        return v1 == v2
      
# medium: https://www.lintcode.com/problem/1499
