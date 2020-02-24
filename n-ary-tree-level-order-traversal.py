class Solution:
    def levelOrder(self, root): # 坑，root[0]才是真root！
        ret = []
        if root:
            levels = [[root[0]], []]
            cur_level, next_level = 0, 1
            while levels[cur_level]:
                ret.append([])
                for node in levels[cur_level]:
                    ret[-1].append(node.label)
                    levels[next_level].extend(node.neighbors)
                levels[cur_level] = []
                cur_level, next_level = next_level, cur_level
        return ret

# easy: https://www.lintcode.com/problem/n-ary-tree-level-order-traversal/
