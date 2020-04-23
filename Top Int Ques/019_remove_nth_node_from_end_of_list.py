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
        result_tail  = result
        
        # Convert linked list to array
        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        # Remove nth item from end of array
        del arr[-n]
        # Convert array back to linked list
        for i in arr:
            result_tail.next = ListNode(i)
            result_tail = result_tail.next
            
        return result.next
