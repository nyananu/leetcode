# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None:
            return None
        
        current = head
        dummy1 = ListNode(0)
        tracker1 = dummy1
        dummy2 = ListNode(0)
        tracker2 = dummy2

        while current is not None:
            if current.val < x:
                tracker1.next = current
                tracker1 = current
            if current.val >= x:
                tracker2.next = current
                tracker2 = current
            
            current = current.next
        
        tracker1.next = None
        tracker2.next = None
        tracker1.next = dummy2.next
        head = dummy1.next

        return head
