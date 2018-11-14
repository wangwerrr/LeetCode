class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        
        leftProduct = 1
        for i in range(len(nums)):
            output.append(leftProduct)
            leftProduct = leftProduct * nums[i]
        
        rightProduct = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] = output[i] * rightProduct
            rightProduct = rightProduct * nums[i]    
        
        return output
            
            
# no division, for there might be '0' in nums
# product = leftproduct * rightproduct
# use 2 loops, calculate lp from left to right ,  calculate rp from right to left
