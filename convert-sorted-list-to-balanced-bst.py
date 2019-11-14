# coding: utf-8

class Solution:
    """
    @param head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        if not head:
            return None
        # 通过两个指针，一个一步一个两步将链表分为前后两段。
        first_node, second_node = head, head.next
        prev = None
        while second_node:
            if second_node:
                second_node = second_node.next
                if second_node:
                    second_node = second_node.next
                    prev = first_node
                    first_node = first_node.next
                else:
                    break
            else:
                break
        new_head = first_node.next
        if prev:
            prev.next = None
        root = TreeNode(first_node.val)
        if head != first_node:
            root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(new_head)
        return root

# medium: http://lintcode.com/zh-cn/problem/convert-sorted-list-to-balanced-bst/
