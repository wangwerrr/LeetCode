class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        phone = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        self.ans = []
        if len(digits) == 0:
            return self.ans 
        self.dfs(0, len(digits), "", digits, phone)
        return self.ans
        
        
    # x: level of for loop, l: num of level, st: currently selected characters
    def dfs(self, x, l, st, digits, phone):
        if x == l:
            self.ans.append(st)
            return
        
        d  = ord(digits[x]) - ord('0')
        for c in phone[d]:
            self.dfs(x+1, l, st + c, digits, phone)
        
# enumerate + DFS 
