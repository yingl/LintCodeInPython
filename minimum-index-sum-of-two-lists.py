class Solution:
    """
    @param list1: a list of strings
    @param list2: a list of strings
    @return: the common interest with the least list index sum
    """
    def findRestaurant(self, list1, list2):
        # Write your code here
        ret = []
        min_index_sum = 100000000
        di, di1 = {}, {}
        for i in range(len(list1)):
            di1[list1[i]] = i
        for i in range(len(list2)):
            if list2[i] in di1:
                index_sum = di1[list2[i]] + i
                if index_sum not in di:
                    di[index_sum] = [list2[i]]
                else:
                    di[index_sum].append(list2[i])
        for k in di.keys():
            if k < min_index_sum:
                min_index_sum = k
        return di[min_index_sum]

# easy: https://www.lintcode.com/problem/minimum-index-sum-of-two-lists/
