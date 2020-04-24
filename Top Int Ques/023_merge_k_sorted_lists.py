# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        result = ListNode(0)
        result_tail = result
        
        ll_to_list = []
        # Add all elements from linked list to an array
        for l in lists:
            while l!= None:
                ll_to_list.append(l.val)
                l = l.next
        # Sort array
        ll_to_list.sort()
        # Add all elements from array to a linked list
        for item in ll_to_list:
            result_tail.next = ListNode(item)
            result_tail = result_tail.next
            
        return result.next
