class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        
        def helper(nums, start = 0, s = []):
            output.append(s)   
            for i in range(start, len(nums)):
                helper(nums, i+1, s + [nums[i]] )
        
        output = []
        
        helper(nums)
            
        return output
# no base case? when start = nums, recursion terminates

"""
my version

class Solution(object):
    def subsets(self, nums):

        def helper(nums, boundary, s = [], pos = 0):
            if pos > boundary:
                output.append(s)
                return
            for i in range(len(nums)):
                if nums[i] in s or (pos > 0 and nums[i] < s[pos-1]):
                    continue
                helper(nums, boundary, s + [nums[i]], pos+1)
        
        
        
        output = []
        
        for num_of_elements in range(len(nums)):
            helper(nums, num_of_elements)
            
        output.append([])
            
        return output
"""
