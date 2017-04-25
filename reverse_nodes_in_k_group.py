# coding: utf-8

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverseKGroup(self, head, k):
        # Write your code here
        # 每k个做一次反转，注意边界条件。
        if (not head) or (k == 1):
            return head
        new_head, prev_tail, next_head = None, None, None
        stop_flag = False
        while head:
            _head, _tail = head, head
            i = 1
            while i < k:
                _tail = _tail.next
                if not _tail:
                    stop_flag = True
                    break
                i += 1
            if stop_flag:
                if not new_head:
                    return new_head
                else:
                    prev_tail.next = head
                break
            next_head = _tail.next
            _head, _tail = self._reverse(_head, _tail)
            if not new_head:
                new_head = _head
            if prev_tail:
                prev_tail.next = _head
            prev_tail = _tail
            head = next_head
        return new_head

    def _reverse(self, head, tail):
        new_head, new_tail = None, None
        while head != tail:
            if not new_tail:
                new_tail = head
            next_head = head.next
            head.next = new_head
            new_head = head
            head = next_head
        tail.next = new_head
        new_head = tail
        return new_head, new_tail

# hard: http://lintcode.com/zh-cn/problem/reverse-nodes-in-k-group/
