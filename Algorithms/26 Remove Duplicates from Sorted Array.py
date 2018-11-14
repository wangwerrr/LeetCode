class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None or len(nums) == 0:    # corner case lol
            return 
        
        i = 0 
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i = i + 1
                nums[i] = nums[j]
        return i + 1
                
# notice that the array is sorted        
# slow & fast pointer
