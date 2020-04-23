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
        # Add items from first linkedlist to array
        while l1 != None:
            ll_to_list.append(l1.val)
            l1 = l1.next
        # Add items from second linkedlist to array
        while l2 != None:
            ll_to_list.append(l2.val)
            l2 = l2.next
        # Sort the array
        ll_to_list.sort()
        # Convert the array to a linkedlist
        for i in ll_to_list:
            result_tail.next = ListNode(i)
            result_tail = result_tail.next
            
        return result.next
