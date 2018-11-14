class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        rList = []
        for i in range(rowIndex+1):
            self.addRow(rList, i)
        return rList[rowIndex]
            
    
    def addRow(self, lst, rowIndex):
        if rowIndex == 0:
            lst.append([1])
            return
        
        row = [1 for i in range(rowIndex+1)]        
        for i in range(1, rowIndex):
            row[i] = lst[rowIndex-1][i-1] + lst[rowIndex-1][i]        
        lst.append(row)
        return
        
