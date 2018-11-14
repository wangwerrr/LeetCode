8 String to Integer (atoi)class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if len(str) == 0:
            return 0
        
        INT_MIN = -1<<31
        INT_MAX = (1<<31) - 1
        
        sign, num, i = 1, 0, 0
        # remove left space
        str = str.lstrip()
        
        # record sign
        if str[0] == '+' or str[0] == '-':
            sign = 1 if str[0] == '+' else -1
            i = i + 1
            
        # record number    
        while i < len(str) and str[i] >= '0' and str[i] <= '9':
              num  = 10 * num + ord(str[i]) - ord('0')        
              # check range exceed for every loop!!!
              x = num * sign
                
              if x > INT_MAX:
                    return INT_MAX
              if x < INT_MIN:
                    return INT_MIN
              i = i + 1
              
        return num * sign
