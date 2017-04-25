# coding: utf-8

class Solution:

    '''
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm 
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    '''
    def serialize(self, root):
        # write your code here
        # 分层遍历，子节点为空用#代替，最后清理尾部的所有#。
        ret = []
        if not root:
            return ret
        level = [root]
        while level:
            new_level = []
            for node in level:
                ret.append(str(node.val) if node else '#')
                if node:
                    new_level.append(node.left)
                    new_level.append(node.right)
            level = new_level
        i = len(ret) - 1
        while i >= 0:
            if ret[i] == '#':
                ret.pop()
                i -= 1
            else:
                break
        return ret

    '''
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in 
    "serialize" method.
    '''
    def deserialize(self, data):
        # write your code here
        if not data:
            return None
        root = TreeNode(data[0])
        level = [root]
        i = 1
        while i < len(data):
            new_level = []
            for node in level:
                node.left = TreeNode(data[i]) if data[i] != '#' else None
                if node.left:
                    new_level.append(node.left)
                i += 1
                if i < len(data):
                    node.right = TreeNode(data[i]) if data[i] != '#' else None
                    if node.right:
                        new_level.append(node.right)
                    i += 1
            level = new_level
        return root

# medium: http://lintcode.com/zh-cn/problem/binary-tree-serialization/
