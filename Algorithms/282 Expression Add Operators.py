class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        ans = []
        self.dfs(num, target, 0, "", 0, 0, ans)
        return ans
        
        
    # update sum and lastF at each loop
    def dfs(self, num, target, start, st, sum, lastF, ans):
        if start == len(num):
            if sum == target:
                ans.append(st)
            return
        
        for i in range(start, len(num)):
            x = int(num[start:i+1])
            
            if start == 0 :
                self.dfs(num, target, i+1, "" + str(x), x, x, ans)
            else:
                self.dfs(num, target, i+1, st + '*' + str(x), sum - lastF + lastF * x, lastF * x, ans)
                self.dfs(num, target, i+1, st + '+' + str(x), sum + x, x, ans)
                self.dfs(num, target, i+1, st + '-' + str(x), sum - x, -x, ans)
            if x == 0:
                break
        
