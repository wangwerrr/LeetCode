class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        def toInt(ans, ls):
            dic = {}
            n = 0
            for i in range(len(ls)):
                if ls[i] not in dic:
                    dic[ls[i]] = n
                    n = n + 1
                ans.append(dic[ls[i]])
        
        strList = str.split(' ')            
        ptnInt = []
        strInt = []
        toInt(ptnInt, pattern)
        toInt(strInt, strList)
        
        return ptnInt == strInt
                
# transform pattern and str in to int representations
# S2 uses map(), find() / index() to do the job
# str.find() 检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，如果包含子字符串返回开始的索引值，否则返回-1。
# ls.index() 用于从列表中找出某个值第一个匹配项的索引位置。
"""
def wordPattern(self, pattern, str):
    s = pattern
    t = str.split()
    return map(s.find, s) == map(t.index, t)
"""            
        
            
        
