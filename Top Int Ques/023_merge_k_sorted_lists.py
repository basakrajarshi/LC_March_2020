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
        result_array = []
        result = ListNode(0)
        result_tail = result
        # Go through each linked list
        # Add elements to an array
        for l in lists:
            while l != None:
                val = l.val
                result_array.append(val)
                l = l.next
        # Sort array
        result_array.sort()
        # Convert array to linked list
        for i in result_array:
            result_tail.next = ListNode(i)
            result_tail = result_tail.next
            
        return result.next
