class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        
        output = []
        
        lenP = len(p)
        lenS = len(s)
        
        delta = [0 for i in range(26)]   # use list instead of dict because we need to calculate the abs sum 
        
        if lenS < lenP:         # corner case
            return output
        
        for i in range(lenP): 
            delta[ord(s[i]) - ord('a')] = delta[ord(s[i]) - ord('a')] + 1
            delta[ord(p[i]) - ord('a')] = delta[ord(p[i]) - ord('a')] - 1          
                
        absList = map(abs, delta)
        absSum = sum(absList) 
        
        if absSum == 0:
            output.append(0)
        
        for i in range(lenP, lenS):
            delta[ord(s[i]) - ord('a')] = delta[ord(s[i]) - ord('a')] + 1
            delta[ord(s[i-lenP]) - ord('a')] = delta[ord(s[i-lenP]) - ord('a')] - 1
            
            absList = map(abs, delta)
            absSum = sum(absList) 
        
            if absSum == 0:
                output.append(i - lenP + 1)
        
        return output
        
# hash, sliding window
        
        
