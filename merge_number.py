class Solution:
    """
    @param numbers: the numbers
    @return: the minimum cost
    """
    def mergeNumber(self, numbers):
        # Write your code he
        """
        可以证明从最小的数开始加，
        和的话送回到队列重新排序，
        排序比较慢，所以做个最小堆。
        """
        ret = 0
        heap = Heap(numbers)
        while len(heap.data) > 1:
            a = heap.pop()
            b = heap.data[0]
            ret += (a + b)
            heap.data[0] = (a + b)
            heap.adjustDown(0)
        return ret
            

class Heap:
    def __init__(self, numbers):
        self.data = numbers
        for i in range(int((len(self.data) - 1) / 2), -1, -1):
            self.adjustDown(i)

    def adjustDown(self, i):
        data = self.data
        while i < len(data):
            left, right = i * 2 + 1, i * 2 + 2
            min_pos = i
            if (left < len(data)) and (data[left] < data[min_pos]):
                min_pos = left
            if (right < len(data)) and (data[right] < data[min_pos]):
                min_pos = right
            if min_pos != i:
                data[i], data[min_pos] = data[min_pos], data[i]
                i = min_pos
            else:
                break
            
    def pop(self):
        ret = self.data[0]
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        self.data.pop()
        if not self.empty():
            self.adjustDown(0)
        return ret

    def empty(self):
        return len(self.data) == 0
