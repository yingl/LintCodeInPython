# coding: utf-8

class Solution:
    def __init__(self):
        self.head, self.tail = None, None

    """
    @param root, the root of tree
    @return: a doubly list node
    """
    def bstToDoublyList(self, root):
        # Write your code here
        # 还是中序遍历，然后插入双链表节点。
        if root:
            self.bstToDoublyList(root.left)
            node = DoublyListNode(root.val)
            if not self.head:
                self.head = node
            else:
                self.tail.next = node
                node.prev = self.tail
            self.tail = node
            self.bstToDoublyList(root.right)
        return self.head

# medium: http://lintcode.com/zh-cn/problem/convert-binary-search-tree-to-doubly-linked-list/
