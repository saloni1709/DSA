# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        dummy = ListNode(0)
        temp = dummy

        dummy.next = head 
        t1 = head
        prev = dummy
        while t1 != None:
            if t1.val == val:
                prev.next = t1.next
            else:
                prev = t1
            t1 = t1.next
        return dummy.next