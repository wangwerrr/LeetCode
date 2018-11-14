class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls = 0
        cows = 0
        dicS = {}
        dicG = {} 
        
        for s, g in zip(secret, guess):
            if s == g:
                bulls = bulls + 1
            try: 
                dicS[s] = dicS[s] + 1
            except:
                dicS[s] = 1
            try: 
                dicG[g] = dicG[g] + 1
            except:
                dicG[g] = 1
        
        for i in dicS.keys():
            if i in dicG:
                cows = cows + min(dicS[i], dicG[i])        # notice the min() we use 
        cows = cows - bulls
        
        return str(bulls) + 'A' + str(cows) + 'B'
            
        

