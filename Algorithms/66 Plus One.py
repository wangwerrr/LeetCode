class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        for i in range(len(digits)):
            num = num*10 + digits[i]
        
        return [int(i) for i in str(num+1)] 
    
# do the plus-one in int mode, then covert back to str to print
