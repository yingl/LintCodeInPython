class MyContainer:
    """
    @param element: Add element into this container.
    @return: nothing
    """
    def add(self, element):
        # write your code here.
        self.data.append(element)
        self.sum += element

    """
    @return: Sum of integers.
    """
    def getSum(self):
        # write your code here.
        return self.sum
        
    def __init__(self):
        self.data = []
        self.sum = 0
        
# easy: https://www.lintcode.com/problem/container-design/
