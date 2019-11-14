class Solution:
    """
    @param cpdomains: a list cpdomains of count-paired domains
    @return: a list of count-paired domains
    """
    def subdomainVisits(self, cpdomains):
        # Write your code here
        di = {}
        for d in cpdomains:
            count, domain = d.split(' ')
            count = int(count)
            parts = domain.split('.')
            for i in range(1, len(parts) + 1): # 拆分组合
                sd = '.'.join(parts[len(parts) -i:])
                if sd not in di:
                    di[sd] = count
                else:
                    di[sd] += count
        ret = []
        for k, v in di.items():
            ret.append(str(v) + ' ' + k)
        return ret

# easy: https://www.lintcode.com/problem/subdomain-visit-count
