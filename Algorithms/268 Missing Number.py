class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        remain = [1] * ( len(nums) + 1 )
        
        for i in range(len(nums)):
            remain[nums[i]] = 0
        
        return remain.index(1)
