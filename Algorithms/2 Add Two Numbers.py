# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        head = ListNode(-1)  # initialize the head of the linked list, assign random value (here: -1) 
        curNode = head
        carryBit = 0
        
        while (l1 and l2):
            digitSum = l1.val + l2.val + carryBit
            if digitSum >= 10:
                digitSum %= 10
                carryBit = 1
            else:
                carryBit = 0
            curNode.next = ListNode(digitSum)
            curNode = curNode.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            sigSum = l1.val + carryBit
            if (sigSum >= 10):
                sigSum %= 10
                carryBit = 1
            else:
                carryBit = 0
            curNode.next = ListNode(sigSum)
            curNode = curNode.next
            l1 = l1.next
        
        # trash format, should use a function
        while l2:
            sigSum = l2.val + carryBit
            if (sigSum >= 10):
                sigSum %= 10
                carryBit = 1
            else:
                carryBit = 0
            curNode.next = ListNode(sigSum)
            curNode = curNode.next
            l2 = l2.next
        
        if carryBit == 1:
            curNode.next = ListNode(1)
            
        return head.next # don't return -1
    
