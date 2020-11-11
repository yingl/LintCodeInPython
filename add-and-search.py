class Solution:
    """
    @param inputs: an integer array
    @param tests: an integer array
    @return: return true if sum of two values in inputs are in tests.
    """
    def addAndSearch(self, inputs, tests):
        # write your code here.
        si = set(tests)
        for i in range(len(inputs) - 1):
            for j in range(i + 1, len(inputs)):
                s = inputs[i] + inputs[j]
                if s in si:
                    return True
        return False
        
# easy: https://www.lintcode.com/problem/add-and-search/
