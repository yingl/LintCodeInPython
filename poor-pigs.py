class Solution:
    """
    @param buckets: an integer
    @param minutesToDie: an integer
    @param minutesToTest: an integer
    @return: how many pigs you need to figure out the "poison" bucket within p minutes 
    """
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        # Write your code here
        # 一次喝一桶，停m分钟再喝下一桶。
        # 先处理限制1小时的情况
        # - 一只猪1小时5桶水，没法更快了。
        # - 25桶水怎么办？排除5行5列，然后：
        #     *   *   *   *   *   Y1
        #     *   *   *   *   *   Y2
        #     *   *   *   *   *   Y3
        #     *   *   *   *   *   Y4
        #     *   *   *   *   *   Y5
        #     X1  X2  X3  X4  X5
        #  猪1确定X坐标，猪2确定Y坐标，2只搞定。
        # 那么我们现在不用关心几桶水，反过来看3只猪的情况，坐标从2维扩展到3维，能处理125桶水。
        # 下面处理通用情况，m分钟死，限制p分钟，1只猪能确定int(m / p) + 1桶水。
        # 那么考虑空间维度，一个pow函数搞定。
        n = int(minutesToTest / minutesToDie) + 1
        ret = 0
        while pow(n, ret) < buckets:
            ret += 1
        return ret

# easy: https://www.lintcode.com/problem/poor-pigs/
