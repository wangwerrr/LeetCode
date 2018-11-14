# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first = head
        while head:
            while head.next and head.val == head.next.val:     # use while instead of if to skip multiple repetition
                head.next = head.next.next
            head = head.next
        return first
