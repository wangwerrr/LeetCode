class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p1, p2, pCur = m-1, n-1, m+n-1

        while p1>-1 and p2>-1:
            if nums1[p1] >= nums2[p2]:
                nums1[pCur] = nums1[p1]
                p1 = p1 - 1
            else:
                nums1[pCur] = nums2[p2]
                p2 = p2 - 1
            pCur = pCur - 1
        if p1 == -1:
            nums1[:pCur+1] = nums2[:p2+1]
        else:
            nums1[:pCur+1] = nums1[:p1+1]
            
  
  
  # thinking reversly
