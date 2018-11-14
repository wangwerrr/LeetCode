class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic = {}
        ans = []
        if len(s) < 10:
            return ans
        
        for i in range(len(s) - 10 + 1):
            if s[i:i+10] in dic and s[i:i+10] not in ans:
                ans.append(s[i:i+10])
            dic[s[i:i+10]] = 1
        return ans
        
                
