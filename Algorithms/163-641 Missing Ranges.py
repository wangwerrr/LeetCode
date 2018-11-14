class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        # write your code here
                
        def addRange(ans, st, ed):
            if st > ed:
                return
            elif st == ed:
                ans.append(str(st))
            else:
                ans.append(str(st) + "->" + str(ed))
           
                
        output  = []
        
        # corner case
        if nums == None or len(nums) == 0:
            addRange(output, lower, upper)
            return output
            
        # usual case
        addRange(output, lower, nums[0]-1)
        for i in range(len(nums)-1):
            addRange(output, nums[i]+1, nums[i+1]-1)
        addRange(output, nums[-1]+1, upper)
        
        return output
        

                
            
# use func to make your code more clear
# first and last intervals should be calculated independently
