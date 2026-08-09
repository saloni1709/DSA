# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        t1 = head
        slow = t1
        fast = t1
        
        while fast != None and fast.next != None:
            slow = slow.next 
            fast = fast.next.next

        return slow
        