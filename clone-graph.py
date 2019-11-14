# coding: utf-8

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.dict = {}  # 存放已复制的节点
        
    def cloneGraph(self, node):
        if not node:
            return None
        # write your code here
        if node in self.dict:
            return self.dict[node]  # 该节点已复制
        ret = UndirectedGraphNode(node.label)
        self.dict[node] = ret
        for neighbor in node.neighbors:
            ret.neighbors.append(self.cloneGraph(neighbor))
        return ret

# medium: http://lintcode.com/zh-cn/problem/clone-graph/
