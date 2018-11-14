class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        output = []        

        def helper(nums, s = [], pos = 0):
            if pos == len(nums):
                output.append(s)
                return 
            
            for num in nums:
                if num in s:
                    continue
                # s.append(num)
                helper(nums, s+[num], pos+1)
                # s.pop()   # back to father node
        
        helper(nums)
        
        return output
            
# Back tracking Problems: https://segmentfault.com/a/11900000061219575
# Also: https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)
# leaf node: quit when pos reaches n, add s to the output list
# helper(): try to put every num in nums into pos when num is not already in s


"""
The problem lies with the line.pop(). If you do print res after line.pop(), you would see that the num popped from the line also gets popped from theres. The possible reason is that line + [num]creates a copy of the line while line.append(num) doesn’t.

Using line + [num] gives you an advantage that you still keep the original line for next iteration so that you don’t need to pop the new num out.

??? still don't know why append() & pop() give a list of [], but using s+[num] works fine

More Simpler solution:

def permute(self, nums):
    perms = [[]]   
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in xrange(len(perm)+1):   
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
        perms = new_perms
    return perms
"""
