class Solution:
    """
    @param base_url: the string of base_url
    @param query_params: sequence of two-element tuples by query_params
    @return: return a url query string
    """
    def urlencode(self, base_url: str, query_params: list[list[str]]) -> str:
        # write your code.
        if not query_params:
            return base_url
        qps = []
        for qp in query_params:
            qps.append(qp[0] + '=' + qp[1])
        qps.sort()
        return base_url + '?' + '&'.join(qps)
      
# easy: https://www.lintcode.com/problem/253/
