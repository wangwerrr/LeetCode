class Solution(object):
    def singleNumber(self, nums):
        nums_dict = {}
        for i in nums:
            if i in nums_dict:
                del nums_dict[i]
            else:
                nums_dict[i] = 1
        return nums_dict.keys()[0]
    
# or use try & except, pop(), popitem()
# Time Cmplxty: dict -- Hash Table, search O(1), if in O(n) --> O(n)
