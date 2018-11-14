class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if int(num1) == 0 or int(num2) == 0:
            return '0'
        
        l = len(num1) + len(num2) - 1
        ans = [0] * l
        
        # pading zeros, convert string to list, notice that lower index -- higher num
        a = [ord(item) - ord('0') for item in num1]
        b = [ord(item) - ord('0') for item in num2]

        # 对应位相加
        for i in range(len(num1)):
            for j in range(len(num2)):
                ans[i+j] += a[i] * b[j] 
             
        # 一次性进位   
        for i in range(l-1, 0, -1):
            ans[i-1] = ans[i-1] + ans[i]/10
            ans[i] = ans[i] % 10
              
        return ''.join([str(item) for item in ans])
   
    """
        Reference:   
        len1 = len(num1)
        len2 = len(num2)
        len3 = len1 + len2

        num3 = [0 for _ in xrange(len3)]
        for i in xrange(len1 - 1, -1, -1):
            carry = 0
            for j in xrange(len2 - 1, -1, -1):
                product = carry + num3[i + j + 1] + int(num1[i]) * int(num2[j])
                num3[i + j + 1] = product % 10
                carry = product / 10

            num3[i] = carry

        result = ""
        i = 0
        while i < len3 - 1 and num3[i] == 0:
            i += 1

        while i < len3:
            result += str(num3[i])
            i += 1

        return result
    
    """
    
        
