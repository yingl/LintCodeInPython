class Solution:
    """
    @param A: the run-length encoded sequence
    """
    def __init__(self, A):
        # do some initialization if necessary
        self.A = A
        self.i = 0
        self.char = None
        self.count = 0
    
    """
    @param n: the number of elements to exhaust
    @return: exhausts the next n elements and returns the last element exhausted 
    """
    def next(self, n):
        # write your code here
        if self.count <= 0:
            if self.i < len(self.A) - 1:
                self.count = self.A[self.i]
                self.char = self.A[self.i + 1]
                self.i += 2
            else:
               return -1
        if n > self.count:
              n -= self.count
              self.count = 0
              return self.next(n)
        else:
              self.count -= n
              return self.char

# medium: https://www.lintcode.com/problem/1741/
