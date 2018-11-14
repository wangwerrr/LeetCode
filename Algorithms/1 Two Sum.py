class Solution(object):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i
            
# hash table look up only takes o(1), so the code runs in o(n)
# below is the brute-forth way of doing it. o(n^2)

""" 

    def twoSum(self, nums, target):

        if nums == None or len(nums) == 0:
            return
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):     # i+1 not i
                if nums[i] + nums[j] == target:
                    return [i, j]
"""

        
