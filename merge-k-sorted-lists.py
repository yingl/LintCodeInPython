# coding: utf-8

class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # write your code here
        if not lists:
            return None
        heap = [list for list in lists if list] # 剔除空链表
        for i in xrange(len(heap) -1, -1, -1):  # 从后向前对每个元素做向下调整，使得满足最小堆要求。
            self.adjustDown(heap, i)
        head, tail = None, None
        while len(heap) > 0:
            node = ListNode(heap[0].val)    # 找到最小元素
            '''
            插入新节点，并更新head、tail。
            同时该节点指向它的next。
            '''
            if not head:
                head = node
            else:
                tail.next = node
            tail = node
            heap[0] = heap[0].next
            if not heap[0]: # 如果为空，则该节点与最后一个节点交换为止，并pop删除。
                heap[0], heap[-1] = heap[-1], heap[0]
                heap.pop()
            if heap:    # 向下调整第一个节点，使得满足最小堆要求。
                self.adjustDown(heap, 0)
        return head

    def adjustDown(self, heap, i):
        while i < len(heap):
            left, right = i * 2 + 1, i * 2 + 2
            min_pos = i
            if (left < len(heap)) and (heap[left].val < heap[min_pos].val):
                min_pos = left
            if (right < len(heap)) and (heap[right].val < heap[min_pos].val):
                min_pos = right
            if min_pos != i:    # 调整A[i]元素位置，继续向下调整。
                heap[i], heap[min_pos] = heap[min_pos], heap[i]
                i = min_pos
            else:   # min_pos没变，A[i]无须调整，结束循环。
                break

# medium: http://lintcode.com/zh-cn/problem/merge-k-sorted-lists/
