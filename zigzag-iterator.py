class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        # do intialization if necessary
        self.v1 = v1
        self.v2 = v2
        self.i1 = 0
        self.i2 = 0
        self.curr = 1
        if not v1:
            self.curr = 2

    """
    @return: An integer
    """
    def _next(self):
        # write your code here
        if self.curr == 1:
            if self.i1 < len(self.v1):
                i = self.i1
                self.i1 += 1
                if self.i2 < len(self.v2):
                    self.curr = 2
                return self.v1[i]
        else:
            if self.i2 < len(self.v2):
                i = self.i2
                self.i2 += 1
                if self.i1 < len(self.v1):
                    self.curr = 1
                return self.v2[i]

    """
    @return: True if has next
    """
    def hasNext(self):
        # write your code here
        return (self.i1 < len(self.v1)) or (self.i2 < len(self.v2))


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result

# medium: https://www.lintcode.com/problem/540/
