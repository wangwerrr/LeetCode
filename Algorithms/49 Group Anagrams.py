import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = collections.defaultdict(list)
        for s in strs:
            dic[tuple(sorted(s))].append(s)   
        return dic.values()
                
# sorted(str)
