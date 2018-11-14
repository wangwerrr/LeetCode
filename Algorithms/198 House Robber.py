class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
            
        opt  = [0] * len(nums)
        opt[0] = nums[0]
        opt[1] = max(nums[0], nums[1])
        
        if len(nums) > 2:
            for i in range(2, len(nums)):
                opt[i] = max(opt[i-1], opt[i-2] + nums[i])
        
        return opt[-1]
