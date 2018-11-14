class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        output = 0
        for i in range(0, len(s) - 1):
            if roman[s[i]] < roman[s[i+1]]:
                output -= roman[s[i]]
            else:
                output += roman[s[i]]
        return output + roman[s[-1]]

# add the last element during return
# the rules are met automatically wrt input data, no need to specify I is before V,X and such 
