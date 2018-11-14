# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return
        
        head = ListNode(None)
        l = ListNode(None)
        head.next = l
        while l1 or l2:
            if not l2:
                l.val = l1.val
                l1 = l1.next
            elif not l1:
                l.val = l2.val
                l2 = l2.next            
            elif l1.val <= l2.val:
                l.val = l1.val
                l1 = l1.next
            else:
                l.val = l2.val
                l2 = l2.next
            if not l1 and not l2:
                break
            l.next = ListNode(None)
            l = l.next
        return head.next
    
    """ 
    # recursion solution: 
    
        def mergeTwoLists(self, a, b):
        if a and b:
            if a.val > b.val:
                a, b = b, a
            a.next = self.mergeTwoLists(a.next, b)
        return a or b   
        
    # The expression x or y first evaluates x; if x is true, its value is returned; otherwise, y is evaluated and the resulting value is returned.
    """
