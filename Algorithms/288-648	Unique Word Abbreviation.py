class ValidWordAbbr:

    # @param {str[]} dictionary a list word
    def __init__(self, dictionary):
        # Write your code here
        self.d = collections.defaultdict(set)
        for word in dictionary:
            self.d[self.getAbbr(word)].add(word)


    # @param {string} word a string
    # @return {boolean} true if its abbreviation is unique or false
    def isUnique(self, word):
        # Write your code here
        key = self.getAbbr(word)
        if key not in self.d:
            return True
        return len(self.d[key]) == 1 and (word in self.d[key])  
        # the abbr of key is unique if there's only one word correspond to it(the length of d[key] == 1)
            
    def getAbbr(self, word):
        if len(word) > 2:
            return word[0] + str(len(word) - 2) + word[-1]
        return word
