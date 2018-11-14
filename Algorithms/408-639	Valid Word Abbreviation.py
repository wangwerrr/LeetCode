import collections

class Solution:
    # @param {string[]} dict an array of n distinct non-empty strings
    # @return {string[]} an array of minimal possible abbreviations for every word
    def wordsAbbreviation(self, dict):
        # Write your code here
        self.dict = {}
        self.solve(dict, 0)
        return map(self.dict.get, dict)

    def abbr(self, word, size):   # size: the size of pre, word= firstChar + pre + num + lastChar
        if len(word) - size <= 3:
            return word
        return word[:size + 1] + str(len(word) - size - 2) + word[-1]

    def solve(self, dict, size):
        dlist = collections.defaultdict(list)
        for word in dict:
            dlist[self.abbr(word, size)].append(word)
        for abbr, wlist in dlist.iteritems():
            if len(wlist) == 1:
                self.dict[wlist[0]] = abbr
            else:
                self.solve(wlist, size + 1)   # recursion
