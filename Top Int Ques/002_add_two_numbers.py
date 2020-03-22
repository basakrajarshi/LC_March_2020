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
        result = ListNode(0)
        result_tail = result
        c = 0
        
        while l1 != None or l2 != None or c != 0:
            
            if l1 != None:
                v1 = l1.val
            else:
                v1 = 0
                
            if l2 != None:
                v2 = l2.val
            else:
                v2 = 0
            
            c, out = divmod(v1 + v2 + c, 10)
            
            result_tail.next = ListNode(out)
            result_tail = result_tail.next
            
            if l1 != None:
                l1 = l1.next
            else:
                l1 = None
            
            if l2 != None:
                l2 = l2.next
            else:
                l2 = None
                
        return result.next
