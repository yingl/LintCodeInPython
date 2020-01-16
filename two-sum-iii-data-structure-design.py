class TwoSum:
    def __init__(self):
        self.di = {}

    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        # write your code here
        if number in self.di:
            self.di[number] += 1
        else:
            self.di[number] = 1

    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        # write your code here
        for k, v in self.di.items():
            t = value - k
            if t == k:
                print(t)
                if (t in self.di) and (self.di[t] >= 2):
                    return True
            else:
                if t in self.di:
                    return True
        return False

# easy: https://www.lintcode.com/problem/two-sum-iii-data-structure-design/
