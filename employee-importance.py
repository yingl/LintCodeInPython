class Solution:
    """
    @param imput: 
    @param id: 
    @return: the total importance value 
    """
    def getImportance(self, imput, _id):
        # Write your code here.
        imput = eval(imput) # 字符串转数组...
        di = {}
        for i in imput:
            print(i)
            di[i[0]] = (i[1], i[2])
        return self._search(di, _id)
        
    def _search(self, di, _id):
        ret = di[_id][0]
        for i in di[_id][1]:
            ret += self._search(di, i)
        return ret
        
# easy: https://www.lintcode.com/problem/employee-importance/
