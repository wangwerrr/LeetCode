class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        # o(n)
        n = len(citations)
        if n == 0:
            return 0
        
        cnt = [0] * (n + 1)
        
        for i in range(n):
            if citations[i] >= n:
                cnt[n] = cnt[n] + 1 # there might be equal citations
            else:
                cnt[citations[i]] = cnt[citations[i]] + 1
        res = 0
        for k in range(n, -1, -1):
            res = res + cnt[k]
            if res >= k:
                return k
        return 0
# cnt[citations[i]]: nums of paper whose citations is equal to citations[i]  & cnt[citations[n]] for greater than citations[n]
# res add them up from top to low, until we find h, else return 0
        
        
        """   
        # o(nlogn)
        
         if len(citations) == 0:
            return 0
        
        if len(citations) == 1:
            if citations[0] >= 1:
                return 1
            else:
                return 0
            
        citations.sort(reverse=True)
        for i in range(len(citations)-1):
            if citations[i] < i + 1:
                return 0
            if citations[i] >= i + 1 and citations[i+1] <= i + 1:
                return i+1

        if citations[-1] >= len(citations):
            return len(citations)
        else:
            return 0      
        """


        
            
