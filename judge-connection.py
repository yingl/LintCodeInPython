class Solution:
    """
    @param arr: the arr
    @param k: the k
    @return: if all instances of value k in arr are connected
    """
    def judgeConnection(self, arr, k):
        # Write your code here.
        # 如果是连通的DFS肯定可以一波带走
        marked = False
        self.rows = len(arr)
        self.cols = len(arr[0])
        for r in range(self.rows):
            for c in range(self.cols):
                if arr[r][c] == k:
                    if not marked:
                        self.mark(arr, k, r, c)
                        marked = True
                    else:
                        return False
        return True

    def mark(self, arr, k, r, c):
        if ((r >= 0) and (r < self.rows)) and ((c >= 0) and (c < self.cols)):
            if arr[r][c] == k:
                arr[r][c] = -1
                self.mark(arr, k, r - 1, c)
                self.mark(arr, k, r + 1, c)
                self.mark(arr, k, r, c - 1)
                self.mark(arr, k, r, c + 1)
                
# medium: https://www.lintcode.com/problem/judge-connection/
