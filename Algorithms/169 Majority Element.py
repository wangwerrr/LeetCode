class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        cnt = 1
        maj = nums[0]
        
        for i in range(1, len(nums)):  
            if cnt == 0:
                maj = nums[i]
                cnt = cnt + 1
            elif nums[i] == maj:
                cnt = cnt + 1
            else:
                cnt = cnt - 1
            

        
        return maj
            
# notice: use i as index or value   
