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
        result = ListNode(0)
        result_tail = result
        
        ll_to_list = []
        
        # Convert both linked lists to arrays
        while l1 != None:
            v1 = l1.val
            ll_to_list.append(v1)
            l1 = l1.next
        while l2 != None:
            v2 = l2.val
            ll_to_list.append(v2)
            l2 = l2.next
        # Sort array in increasing order
        ll_to_list.sort()
        # Convert array to linked list
        for i in ll_to_list:
            result_tail.next = ListNode(i)
            result_tail = result_tail.next
            
        return result.next
