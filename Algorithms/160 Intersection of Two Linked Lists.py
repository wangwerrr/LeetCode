# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """

        if headA == None or headB == None:
            return None

        curA = headA
        curB = headB

        while curA != curB:
            curA = headB if curA == None else curA.next
            curB = headA if curB == None else curB.next

        return curA


"""

[1st iteration]
We want to append linked list B after linked list A and vice versa, so that

A becomes  (A_diff + common + b_diff) + common
B becomes  (B_diff + common + A_diff) + common

Now A & B are of same length before arriving at common part for the second time (the part in parentheses)
After first iteration, curA points at headB, curB points at headA

[2nd iteration]
We go through A & B simultaneously, from the very beginning.

if there is a common part: the loop will stop, both pointer will be pointing to the starting node of the common part
if there isn't: both pointers will be pointing to None

Finally, we can return either of the pointers.

"""
