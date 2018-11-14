class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)   # when k > len(nums), circle it
        nums[:] = nums[-k:] + nums[:-k]
        
"""
nums[:] can't be written as nums on the OJ.

The previous one can truly change the value of old nums, but the following one just changes its reference to a new nums not the value of old nums.
"""
