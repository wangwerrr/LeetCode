class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
    
        l = max(len(num1), len(num2))
        ans = [0] * l
        
        # pading zeros, convert string to list, notice that lower index -- higher num
        a = [0] * (l - len(num1)) + [ord(item) - ord('0') for item in num1]
        b = [0] * (l - len(num2)) + [ord(item) - ord('0') for item in num2]

        # 对应位相加
        for i in range(l):
            ans[i] = a[i] + b[i] 
             
        # 一次性进位   
        for i in range(l-1, 0, -1):
            ans[i-1] = ans[i-1] + ans[i]/10
            ans[i] = ans[i] % 10
              
        return ''.join([str(item) for item in ans])
