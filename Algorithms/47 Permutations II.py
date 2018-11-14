class Solution(object):
    def permuteUnique(self, nums):
        
        nums.sort()

        def helper(nums, s = [], pos = 0, used = [False] * len(nums)):
            if pos == len(nums):
                output.append(s)
                return 
            
            for i in range(len(nums)):
                if used[i] is True or ( i > 0 and nums[i] == nums[i-1] and used[i-1] is False ) :
                    continue                    
                used[i] = True
                helper(nums, s+[nums[i]], pos+1)
                used[i] = False
                
        output = []
        helper(nums)
        
        return output
            
# i as index is more convenient
# To handle duplication, just avoid inserting a number before any of its duplicates.
# https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)
