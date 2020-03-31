# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        
        # Convert to list
        ll_to_list = []
        while head != None:
            v1 = head.val
            ll_to_list.append(v1)
            head = head.next
        
        # Remove nth item from end of list 
        del ll_to_list[-n]
       
       # Convert back to linked list
        for i in ll_to_list:
            result_tail.next = ListNode(i)
            result_tail = result_tail.next
        
        return result.next
