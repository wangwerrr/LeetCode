class Solution:
    # @param {string[]} strs a list of strings
    # @return {string} encodes a list of strings to a single string
    def encode(self, strs):
        # Write your code here
        output = ""
        for s in strs:
            for c in s:
                if c == ':' :
                    output = output + '::'
                else:
                    output = output + c
            output = output + ':;'     # our self-designed break sign
        return output
                    


    # @param {string} s a string
    # @return {string[]} decodes a single string to a list of strings
    def decode(self, s):
        # Write your code here
        output = []
        i = 0
        item = ""
        
        while i < len(s):
            if s[i] == ':' :
                if s[i+1] == ';' :
                    output.append(item)
                    item = ""
                    i = i + 2
                else:
                    item = item + s[i+1]
                    i = i + 2
            else:
                item = item + s[i]
                i = i + 1
            
        return output

        
    
    
