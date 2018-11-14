from collections import defaultdict

class Solution(object):
    def longestCommonPrefix(self, strs):
            if len(strs) == 0: return ''
            prefix = strs[0]
            for i in xrange(1, len(strs)):
                while strs[i][:len(prefix)] != prefix:
                    prefix = prefix[:-1]
            return prefix
        
# use strs[0] as the baseline prefix, comparing other words with it, shorten one char every loop if the pres are not matched
