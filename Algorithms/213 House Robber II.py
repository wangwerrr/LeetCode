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
        if len(nums) == 2:
            return max(nums[0], nums[1])
             
        opt1  = [0] * (len(nums)-1)
        opt1[0] = nums[0]
        opt1[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)-1):
            opt1[i] = max(opt1[i-1], opt1[i-2] + nums[i])
        sub1 = opt1[-1]
        
        opt2  = [0] * (len(nums)-1)
        opt2[0] = nums[1]
        opt2[1] = max(nums[1], nums[2])

        for i in range(2, len(nums)-1):
            opt2[i] = max(opt2[i-1], opt2[i-2] + nums[i+1])        
        sub2 = opt2[-1]
        
        return max(sub1, sub2)
        
    

    
    # Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money
