class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        def helper(ans, comb, start, n, k):
            if n < 0:
                return
            if n == 0 and len(comb) == k:
                ans.append(comb)
                return
            for i in range(start, 10):    # i begin with start, not 1, to avoid using same num
                helper(ans, comb + [i], i+1, n-i, k)
       
        ans = []
        comb = []
        helper(ans, comb, 1, n, k)

        return ans
  

