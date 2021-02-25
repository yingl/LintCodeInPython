class MyContainerII:
    def __init__(self):
        # initialize your data structure here
        self.data = []
        self.sum = 0
        
    """
    @param element: element: Add element into this container.
    @return: nothing
    """
    def add(self, element):
        # write your code here
        for i in range(len(self.data)):
            if self.data[i] == element:
                return
        self.data.append(element)
        self.sum += element
        
    """
    @param element: element: Remove element into this container.
    @return: nothing
    """
    def remove(self, element):
        # write your code here
        for i in range(len(self.data)):
            if self.data[i] == element:
                self.data.pop(i)
                self.sum -= element
                break

    """
    @return: Sum of integers.
    """
    def getSum(self):
        # write your code here
        return self.sum
      
# easy: https://www.lintcode.com/problem/container-design-ii/
