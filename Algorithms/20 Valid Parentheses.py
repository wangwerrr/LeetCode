class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        balanced = True
        i = 0
        
        while i < len(s) and balanced:
            symbol = s[i]
            if symbol in "([{":
                stack.append(symbol)    
            else:
                if len(stack) == 0:
                    balanced = False
                else:
                    top = stack.pop()
                    if not self.matches(top,symbol):
                           balanced = False
            i = i + 1
            
        if balanced and len(stack) == 0:
            return True
        else:
            return False

    def matches(self, start, end):
        opens = "([{"
        closers = ")]}"
        return opens.index(start) == closers.index(end)

# use list as stack -- push : append(), pop: pop()
                
        
