class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        n = len(s)
        s_dict = {}
        
        for i in range(n):
            try:
                s_dict[s[i]] = s_dict[s[i]] + 1
            except:
                s_dict[s[i]] = 1
        
        for i in range(n):
            try:
                s_dict[t[i]] = s_dict[t[i]] - 1
                if s_dict[t[i]] == 0:
                    s_dict.pop(t[i])
            except:
                return False
        
        return True
    
# I love try/except
