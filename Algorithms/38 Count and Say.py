class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return
        elif n == 1:
            return "1"
        
        pre = "1"
        for _ in range(1, n):
            cur = ""
            j = 1
            count = 1
            
            while j < len(pre):
                if pre[j] == pre[j-1]:
                    count += 1
                else:
                    cur = cur + str(count) + pre[j-1]
                    count = 1
                j = j + 1     
            cur = cur + str(count) + pre[j-1]
            pre = cur
        
        return pre
            
        
