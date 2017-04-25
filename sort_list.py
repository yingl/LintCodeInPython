# coding: utf-8

class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the sorted linked list,
                  using constant space complexity.
    """
    def sortList(self, head):
        # write your code here
        if not (head and head.next):
            return head
        # 通过向前走一步／两步将链表拆开
        prev = None
        node_one_step, node_two_step = head, head
        while node_one_step and node_two_step:
            node_two_step = node_two_step.next
            if node_two_step:
                node_two_step = node_two_step.next
                prev = node_one_step
                node_one_step = node_one_step.next
            else:
                break
        new_head = prev.next  # new_head是后半段链表的head
        prev.next = None
        # 递归后用merge合并结果
        return self.merge(self.sortList(head), self.sortList(new_head))

    def merge(self, left, right):
        head, tail = None, None
        while (left is not None) and (right is not None):
            if left.val <= right.val:
                node = left
                left = left.next
            else:
                node = right
                right = right.next
            if head is None:
                head = node
            else:
                tail.next = node
            tail = node
            tail.next = None
        if head is None:
            head = left if left is not None else right
        else:
            tail.next = left if left is not None else right
        return head

# medium: http://lintcode.com/zh-cn/problem/sort-list/
