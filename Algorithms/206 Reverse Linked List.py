# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head
        rev = self.reverseList(head.next)
        head.next.next = head
        head.next = None 
        
        return rev

        # first get to the last node, then do the linkage job backwards
        
"""
iteration ver:

    def reverseListIterative(self, head):

        rev, cur = None, head
        while cur:
            rev, rev.next, cur = cur, rev, cur.next
        return rev
"""
