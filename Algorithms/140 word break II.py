from collections import defaultdict

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        self.done = defaultdict(list)
        self.done[""] = [""]
        return self.dfs(s, wordDict)
        
    def dfs(self, s, wordDict):
        if s in self.done:
            return self.done[s]
        
        ans = []
        for lenth in range(1, len(s) + 1):
            
            s1 = s[:lenth]
            s2 = s[lenth:]  # no str() will return a type of unicode

            if s1 in wordDict:
                s2_res = self.dfs(s2, wordDict)
                for item in s2_res:
                    if item == "":
                        ans.append(s1)
                    else:
                        ans.append(s1 + " " + item)
        self.done[s] = ans
        return ans
    
# depth first search(DFS) with memory                         
# done is a dict of lists that record the breaks of [all sub_strings] we've already found in certain words  
# ans is a list of strings, which record the break for the sub string we are processing in each recursion, the outmost ans will be of the entire string 
# eg. for"abcdef", the outmost ans = ["a bc def", "ab c def"]  ,    done["a bc"] : ["a bc", "ab c"], done["def"] = ["def"]
