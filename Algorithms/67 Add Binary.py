class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        l = max(len(a), len(b))
        
        a = [0] * (l-len(a)) + [int(item) for item in a]
        b = [0] * (l-len(b)) + [int(item) for item in b]
        c = [0] * l
        
        for i in range(l):
            c[i] = a[i] + b[i]
        
        for i in range(l-1, 0, -1):
            c[i-1] = c[i-1] + c[i] / 2
            c[i] = c[i] % 2
        c = ''.join([str(item) for item in c])
        
        if c[0] == '2':
            return "10" + c[1:] 
        elif c[0] == '3':
            return "11" + c[1:]
        else:
            return c
            
