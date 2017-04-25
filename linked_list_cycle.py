# coding: utf-8

class Solution:
    """
    @param head: The first node of the linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        one_node, two_node = head, head
        while two_node:
            for i in xrange(2):
                if two_node:
                    two_node = two_node.next
                    if two_node == one_node:
                        return True
                else:
                    break
            one_node = one_node.next
            if not two_node:
                break
        return False

# medium: http://lintcode.com/zh-cn/problem/linked-list-cycle/
