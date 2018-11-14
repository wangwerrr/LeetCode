class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
# simple solution        
#       non_zeros = [i for i in nums if i != 0]
#       nums[:len(non_zeros)] = non_zeros
#        
#       if len(non_zeros) < len(nums):
#            nums[len(non_zeros):] = [0] * (len(nums) - len(non_zeros))

# space-efficient solution
        toBeOccupied = 0
        for i in nums:
            if i != 0:
                nums[toBeOccupied] = i
                toBeOccupied = toBeOccupied + 1
                
        nums[toBeOccupied:] = [0] * (len(nums) - toBeOccupied)

# consider the problem as sitting on empty chairs,  keep tracking the position of next chair to be occupied 
