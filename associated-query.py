class Solution:
    """
    @param datalist1: a list represents the employee table
    @param datalist2: a list represents the employee hours table
    @return: Returns a list of strings represents the datalist3
    """
    def getList(self, datalist1, datalist2):
        # write your code here
        ret = []
        di = {}
        for data in datalist2:
            di[data[0]] = [data[2], data[4], data[6]]
        for data in datalist1:
            uid = data[0]
            uname = data[1]
            if uid in di:
                line = [uname]
                line.extend(di[uid])
                total = 0
                for i in di[uid]:
                    total += int(i)
                line.append(str(total))
                ret.append(line)
        return ret;

# easy: https://www.lintcode.com/problem/associated-query/
